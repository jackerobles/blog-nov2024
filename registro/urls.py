from django.urls import path, include
from registro.views import SignUpView,Home

urlpatterns = [
    path("accounts/",include('django.contrib.auth.urls')),
    path("signup/",SignUpView.as_view(),name="signup"),
    path("",Home,name="Home")
    ]