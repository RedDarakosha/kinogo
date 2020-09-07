from django.urls import path
from . import views as local_views
from django.contrib.auth.views import LoginView

app_name = 'usrauth'

urlpatterns = [
	path("login/", LoginView.as_view(), name='login'),
	path('logout/', local_views.LogoutView.as_view(), name='logout'),
	path('profile/', local_views.profile, name='profile'),
]