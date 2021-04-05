from django import forms
from .github import GithubUserScraping

class GithubForm(forms.Form):
	"""docstring for GithubForm"""
	username = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Ex: spiderbbc'}))

	def clean_username(self):
		username = self.cleaned_data['username']
		github_user = GithubUserScraping(username)
		if github_user.get_status_code() == 404:
			raise forms.ValidationError("username return 404")
		return username

			
