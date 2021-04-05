from django.db import models
from .github import GithubUserScraping
# Create your models here.
class GithubUser(models.Model):
	"""docstring for GithubUser"""

	def get_user(self,username):
		github_user = GithubUserScraping(username)
		profile_image = github_user.get_profile_image()
		context = {
			'profile_image': github_user.get_profile_image(),
			'profile_bio': github_user.get_profile_bio(),
			'vcard_names': github_user.get_vcard_names(),
			'nav_body': github_user.get_nav_body(),
		}
		return context
		