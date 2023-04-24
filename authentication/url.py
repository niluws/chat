from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('activation/<active_code>/',views.ActivationView.as_view(),name='activation'),
    path('Logout/', views.LogoutView.as_view(), name='logout'),
    path('ForgotPassword/', views.ForgotPassword.as_view(), name='ForgotPassword'),
    path('reset_pass/<active_code>/',views.ResetPassword.as_view(),name='ResetPassword'),
]
