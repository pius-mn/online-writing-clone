from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Create your views here.
import client.models

from client.models import Jobs


@login_required(login_url='login')
def AdminDashboard(request):
    if not request.user.is_admin:
        return redirect('landingpage')
    alljobs = Jobs.objects.all()
    allPendinJobs = 0
    allCompletedJobs = 0
    if len(alljobs) != 0:
        allPendinJobs = len(Jobs.objects.filter( is_denied=False))
        allCompletedJobs = len(Jobs.objects.filter(is_completed=True))

    context = {
        'all_jobs': len(alljobs),
        'all_pending_jobs': allPendinJobs,
        'all_completed_jobs': allCompletedJobs
    }
    return render(request, 'admins/dashboard.html', context)


@login_required(login_url='login')
def PendingJobs(request):
    if not request.user.is_admin:
        return redirect('landingpage')
    alljobs = Jobs.objects.all()
    allPendinJobs = 0
    if len(alljobs) != 0:
        allPendinJobs = Jobs.objects.filter(is_denied=False, is_completed=False)
    context = {
        'allPendingJobs': allPendinJobs
    }
    return render(request, 'admins/pending-jobs.html', context)


@login_required(login_url='login')
def ApproveJob(request, id):
    if not request.user.is_admin:
        return redirect('landingpage')
    if id is None:
        messages.error(
            request, 'error cant find your job')
        return redirect('adminpendingjobs')
    job = Jobs.objects.get(id=id)
    if job is None:
        messages.error(
            request, 'error cant find your job')
        return redirect('adminpendingjobs')
    if request.method == 'POST':
        min_salary = request.POST['min_price']
        delivary_qty = request.POST['qtyInput']
        print(delivary_qty)
        delivery_type = request.POST['delivery']
        job.min_salary = min_salary
        job.delivery_qty = delivary_qty
        job.delivery_type = delivery_type
        job.is_approved = True
        print(job.delivery_qty)
        job.save()
        messages.success(
            request, 'Successfully apprioved Job')
        return redirect('adminpendingjobs')

@login_required(login_url='login')
def deleteJob (request,id):
    if not request.user.is_admin:
        return redirect('landingpage')
    if id is None:
        messages.error(
            request, 'error cant find your job')
        return redirect('adminpendingjobs')
    job = Jobs.objects.get(id=id)
    job.is_denied = True
    job.save()
    messages.success(
        request, 'Successfully apprioved Job')
    return redirect('adminpendingjobs')

@login_required(login_url='login')
def CompletedJobs(request):
    if not request.user.is_admin:
        return redirect('landingpage')
    alljobs = Jobs.objects.all()
    allComplitedJobs = 0
    if len(alljobs) != 0:
        allComplitedJobs = Jobs.objects.filter(is_completed=True, )
    context = {
        'allCompletedJobs': allComplitedJobs
    }
    return render(request, 'admins/completed-jobs.html', context)

@login_required(login_url='login')
def chat(request):
    return render(request, 'admins/messages.html')