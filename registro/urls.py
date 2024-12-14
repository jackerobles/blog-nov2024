from django.urls import path, include
from registro.views import SignUpView

urlpatterns = [
    path("accounts/",include('django.contrib.auth.urls')),
    path("",SignUpView.as_view(),name="signup")
    ]