from django.urls import path
from .views import JobListView, JobDetailView, JobCreateView, ApplicantCreateView, RankResumesView

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('jobs/create/', JobCreateView.as_view(), name='job_create'),
    path('applicants/create/', ApplicantCreateView.as_view(), name='applicant_create'),
    path('rank_resumes/', RankResumesView.as_view(), name='rank_resumes'),  # Add this line
]
