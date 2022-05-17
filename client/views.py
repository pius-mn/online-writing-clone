import string

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser, Jobs
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random


# Create your views here.
def LandingPage(request):
    jobsPosted = Jobs.objects.all()
    completedjobs = Jobs.objects.filter(is_completed = True)
    freelancers = CustomUser.objects.filter(is_admin=False,is_super=False,is_client=False)
    clients = CustomUser.objects.filter(is_client= True)
    coverjob = Jobs.objects.filter( is_approved = True,is_denied = False,is_completed = False,is_regected =False,)
    context = {
        'jobs' : len(jobsPosted),
        'completedJobs' : len(completedjobs),
        'freelancers': len(freelancers),
        'clients' : len(clients),
        'noOfCoverJobs' : len(coverjob),
        'coverJob': coverjob
    }
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admindashboard')
        elif request.user.is_client:
            return redirect('dashboard')
    return render(request, 'landingpage.html',context)

def registration(request):
    if(request.user.is_authenticated):
        return redirect('landingpage')
    form = CustomUserCreationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            otp = random.randint(1000, 9999)
            user.otp = otp
            user.save()
            login(request, user)
            return redirect('otp')
    return render(request, 'registration.html', context)


@login_required(login_url='login')
def otp(request):
    if request.method == 'POST':
        userOtp = int(request.POST['otp'])
        otpDb = request.user.otp
        if userOtp == otpDb:
            try:
                user = request.user
                user.is_verified = True
                user.save()
            except Exception as e:
                print(e)
                messages.error(request, 'Something went wrong')
                return redirect('otp')
            return redirect('landingpage')
        else:
            messages.error(request, 'Invalid otp')
            return redirect('otp')
    return render(request, 'otp.html')


def loginclient(request):
    if(request.user.is_authenticated):
        return redirect('landingpage')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = CustomUser.objects.get(email=email)
        except Exception as e:
            print(e)
            messages.error(request, 'Email does not exist')
            return redirect('login')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_admin:
                return redirect('admindashboard')
            return redirect('landingpage')
        else:
            messages.error(request, 'Email or password incorrect')
            return redirect('login')
    return render(request, 'login.html')


def logoutClient(request):
    logout(request)
    return redirect('landingpage')


@login_required(login_url='login')
def dashboard(request):
    if not request.user.is_client:
        return redirect('landingpage')
    jobs = request.user.jobs_set.all()
    number_of_pending_jobs = 0
    number_of_completed_jobs = 0
    orders = 0
    number_of_jobs = len(jobs) 
    if number_of_jobs != 0:
        completed_jobs = request.user.jobs_set.filter(is_completed=True, )
        pending_jobs = request.user.jobs_set.filter(is_completed=False, is_regected=False)
        number_of_pending_jobs = len(pending_jobs)
        number_of_completed_jobs = len(completed_jobs)
        orders = request.user.funds_set.all()
    context = {
        'no_of_jobs': number_of_jobs,
        'no_of_completed_jobs': number_of_completed_jobs,
        'no_of_pending_jobs': number_of_pending_jobs,
        'orders': orders
    }
    return render(request, 'client/dashboard.html', context)


@login_required(login_url='login')
def chatClient(request):
    
    return render(request, 'client/messages.html')


@login_required(login_url='login')
def addfunds(request):
    return render(request, 'client/payments.html')


@login_required(login_url='login')
def invoice(request):
    return render(request, 'client/invoice.html')


@login_required(login_url='login')
def pendingJobs(request):
    jobs_created = request.user.jobs_set.all()
    pending_jobs = 0
    if len(jobs_created) != 0:
        pending_jobs = request.user.jobs_set.filter(is_completed=False)
    print(pending_jobs)
    context={
        'pendingJobs': pending_jobs
    }
    return render(request, 'client/pending-jobs.html', context)


@login_required(login_url='login')
def completedjobs(request):
    jobs_created = request.user.jobs_set.all()
    completed_jobs = 0
    if len(jobs_created) != 0:
        completed_jobs = request.user.jobs_set.filter(is_completed=True)

    context = {
        'completedJobs': completed_jobs
    }
    return render(request, 'client/completed-jobs.html', context)


@login_required(login_url='login')
def postjob(request):
    if request.method == 'POST':
        client = CustomUser.get_username()
        jobid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        title = request.POST['title']
        type = request.POST['type']
        category = request.POST['category']
        minSalary = request.POST['minsal']
        maxSalary = request.POST['maxsal']
        description = request.POST['description']
        file = request.FILES['uploadedfile']
        
        job = Jobs(title=title, username=client, jobId=jobid, type=type, category=category,
                   max_salary=maxSalary, min_salary=minSalary,
                   description=description, uploadedfile=file)
        try:
            job.save()
         
        except Exception as e:
            print(e)
            messages.error(request, 'Something went wrong please contact customer care')
            return redirect('add-job')
        messages.success(request,
                         'Job successfully posted please chat with one of our admins to complete assignment use the job id : ' + jobid)
        return redirect('pending-jobs')
    return render(request, 'client/post-a-job.html')




@login_required(login_url='login')
def settingsclient(request):
    if request.method == 'POST':
        user = request.user
        user.profile_image = request.FILES['userimage']
        user.save()
    return render(request, 'client/settings.html')
