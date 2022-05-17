from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.LandingPage,name='landingpage'),
    path('register/', views.registration, name='register'),
    path('login/', views.loginclient, name='login'),
    path('otp/', views.otp, name='otp'),
    path('logout/', views.logoutClient, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='forgot-password.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='success_forgot_password.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='reset_password.html'), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name="password_reset_complete"),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('chat1/', views.chatClient, name='chat'),
    path('addfunds/', views.addfunds, name='add-funds'),
    path('invoice/', views.invoice, name='invoice'),
    path('pendingjobs/', views.pendingJobs, name='pending-jobs'),
    path('completedjobs/', views.completedjobs, name='completed-jobs'),
    path('addjob/', views.postjob, name='add-job'),
    path('settings/', views.settingsclient, name='settings'),
]
