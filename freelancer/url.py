from django.urls import path
from . import views

urlpatterns=[
    path('availablejobs/', views.availablejobs, name='freelanceravailablejobs'),
    path('completedjobs/', views.completedjobs, name='freelancercompletedjobs'),
    path('disputedjobs/', views.disputedjobs, name='freelancerdisputedjobs'),
    path('myjobs/', views.myJobs, name='freelancermyjobs'),
    path('job/<str:id>', views.jobdescription, name='freelancerspesificjob'),
    path('profile/', views.profile, name='freelancerprofile'),
    path('settings/', views.setting, name='freelancersettings'),
    path('bind/', views.binds, name='placeBind')
]