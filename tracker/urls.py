from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-job/', views.add_job, name='add_job'),  
    path('edit-job/<int:job_id>/', views.edit_job, name='edit_job'),  
    path('delete-job/<int:job_id>/', views.delete_job, name='delete_job'),  
    path('update-job-stage/<int:job_id>/', views.update_job_stage, name='update_job_stage'),
]