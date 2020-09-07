from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
# Create your views here.

class LogoutView(LogoutView):
	next_page = '../../accounts/profile'


def profile(request):
	if request.user.is_authenticated:
		template = loader.get_template("usrauth/profile.html")
		content = {'user': request.user}
		return HttpResponse(template.render(content, request))
	else:
		return redirect('../login')

