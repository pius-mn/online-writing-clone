from email import message
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages
from django.db.models import Q


from client.models import Bids, Jobs
# Create your views here.


@login_required(login_url='login')
def availablejobs(request):
    job = Jobs.objects.all()
    context = {
        'allJobs': job
    }

    if request.user.is_admin:
        return redirect('admindashboard')
    return render(request, 'freelancer/available-jobs.html', context)


@login_required(login_url='login')
def completedjobs(request):
    if request.user.is_admin:
        return redirect('admindashboard')
    return render(request, 'freelancer/completed-jobs.html')


@login_required(login_url='login')
def disputedjobs(request):
    if request.user.is_admin:
        return redirect('admindashboard')
    return render(request, 'freelancer/disputed-jobs.html')


@login_required(login_url='login')
def myJobs(request):
    if request.user.is_admin:
        return redirect('admindashboard')
    
    job=Bids.objects.all().filter(username=request.user.username)
    print(job)
   
    job={
        'job':job
    } 
        
        
    # 
    return render(request, 'freelancer/my-jobs.html',job)


@login_required(login_url='login')
def binds(request):
    if request.method == 'POST':
        if request.user.is_admin:
            return redirect('admindashboard')
        else:

            job = request.POST['jobId']
            
            freelancer = request.user.username
            #created_at = request.POST['jobId']
            #is_accepted = request.POST['jobId']
            amount = request.POST['amount']

            workingDays = request.POST['qtyInput']+' '+request.POST['dayORhours']
            bind = Bids(username=freelancer,jobId=job,amount=amount,workingDays=workingDays)
            try:
                bind.save()
            
            except Exception as e:
                print(e)
                messages.error(request, 'Something went wrong please contact customer care')
                return redirect('availablejobs')
            messages.success(request,
                            'Job successfully posted please chat with one of our admins to complete assignment use the job id : ' + job)
            return redirect('freelancermyjobs')


        


@login_required(login_url='login')
def profile(request):
    if request.user.is_admin:
        return redirect('admindashboard')
    return render(request, 'freelancer/profile.html')


@login_required(login_url='login')
def setting(request):
    if request.user.is_admin:
        return redirect('admindashboard')
    return render(request, 'freelancer/settings.html')


@login_required(login_url='login')
def jobdescription(request, id):
    if request.user.is_admin:
        return redirect('admindashboard')
    if id is None:
        message.error(request, "no job was found")
        return redirect('freelanceravailablejobs')
    job = Jobs.objects.get(jobId=id)
    bids=Bids.objects.all().filter(jobId=id)
    # remaining_time = job.created_at - job.due_date;
    context = {
        'job': job,
        'bids':bids
        # 'remtime': remaining_time,
    }
    return render(request, 'freelancer/job-description.html', context)
