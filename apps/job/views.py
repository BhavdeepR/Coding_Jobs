from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import AddJobForm, ApplicationForm
from .models import Job, Application

from apps.notification.utilities import create_notification

def search(request):
    return render(request, 'job/search.html')

def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)

    return render(request, 'job/job_detail.html', {'job': job})

@login_required
def apply_for_job(request, job_id):
    job = Job.objects.get(pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()

            create_notification(request, job.created_by, 'application', extra_id=application.id)
            return redirect('view_application', application_id=application.id)
    else:
        form = ApplicationForm()
    if request.GET.get('submitted') == '1':
        messages.success(request, 'Your application has been submitted successfully!')
    return render(request, 'job/apply_for_job.html', {'form': form, 'job': job})

@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return redirect('dashboard')
    else:
        form = AddJobForm()
    
    return render(request, 'job/add_job.html', {'form': form})

@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)

    if request.method == 'POST':
        form = AddJobForm(request.POST, instance=job)

        if form.is_valid():
            job = form.save(commit=False)
            job.status = request.POST.get('status')
            job.save()

            return redirect('dashboard')
    else:
        form = AddJobForm(instance=job)
    
    return render(request, 'job/edit_job.html', {'form': form, 'job': job})

@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')
        return redirect('dashboard')
    return render(request, 'job/delete_job_confirm.html', {'job': job})