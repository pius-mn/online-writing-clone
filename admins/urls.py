from django.urls import path
from . import views

urlpatterns=[
    path('dashboard/', views.AdminDashboard, name='admindashboard'),
    path('pendingjobs/', views.PendingJobs, name='adminpendingjobs'),
    path('pendingjob/approve/<str:id>/', views.ApproveJob, name='adminaprovejob'),
    path('pendingjob/deny/<str:id>/', views.deleteJob, name='admindeletejob'),
    path('completedjobs/' ,views.CompletedJobs, name='admincompletedjobs'),
    path('messages/', views.chat, name='adminchat')
]