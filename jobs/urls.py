from django.urls import path
from . import views

urlpatterns = [
    path('create-job/', views.CreateJobViewSet.as_view(), name='create-job'),
    path('get-jobs/', views.getAllJobs, name="get-all-jobs"),
    path('get-job-apps/<int:job_id>/', views.getJobView, name="get-jobs-and-apps"),
    path('delete-job/<int:job_id>/', views.deleteJobView, name="delete-job"),
    path('update-job/<int:job_id>/', views.updateJobView, name="update-job")
]