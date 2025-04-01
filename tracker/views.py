from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Job
from .forms import JobForm

def home(request):
    form = JobForm()

    stages = [
        {
            "stage": "Applied",
            "emoji": "📝",
            "color": "bg-blue-100",
            "dark_color": "dark:bg-blue-700",
            "text_color": "dark:text-blue-100",
            "jobs": Job.objects.filter(stage="applied")
        },
        {
            "stage": "Interview",
            "emoji": "🤝",
            "color": "bg-yellow-100",
            "dark_color": "dark:bg-yellow-700",
            "text_color": "dark:text-yellow-100",
            "jobs": Job.objects.filter(stage="interview")
        },
        {
            "stage": "Offer",
            "emoji": "💰",
            "color": "bg-green-100",
            "dark_color": "dark:bg-green-700",
            "text_color": "dark:text-green-100",
            "jobs": Job.objects.filter(stage="offer")
        },
        {
            "stage": "Rejected",
            "emoji": "❌",
            "color": "bg-red-100",
            "dark_color": "dark:bg-red-700",
            "text_color": "dark:text-red-100",
            "jobs": Job.objects.filter(stage="rejected")
        },
    ]

    return render(request, 'base.html', {
        'columns': stages,
        'form': form,
    })


@require_POST
def add_job(request):
    form = JobForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('home')


def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobForm(instance=job)
    return render(request, 'edit_job.html', {'form': form, 'job': job})


@require_POST
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    job.delete()
    return redirect('home')


@csrf_exempt
def update_job_stage(request, job_id):
    if request.method == 'POST':
        job = get_object_or_404(Job, id=job_id)
        new_stage = request.POST.get('stage')

        if new_stage in ['applied', 'interview', 'offer', 'rejected']:
            job.stage = new_stage
            job.save()

        updated_jobs = Job.objects.filter(stage=new_stage)

        return render(request, 'partials/column_body.html', {
            'column': {
                'stage': new_stage,
                'jobs': updated_jobs,
            }
        })

    return HttpResponse(status=405)

