from django.views import View
from django.shortcuts import render,redirect
from .forms import GithubForm
from .models import GithubUser

# Create your views here.
class GithubView(View):
	"""docstring for GithubView"""
	def get(self,request):
		form = GithubForm();
		return render(request,'gitgub/index.html',{'form': form})
	def post(self,request):
		form = GithubForm(request.POST)	
		context = {}
		if form.is_valid():
			username = form.cleaned_data.get('username', None)
			github_user = GithubUser(username)
			context = github_user.get_user(username = username)
		return render(request,'gitgub/index.html',{'form': form,'context': context})	
