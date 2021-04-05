from django.urls import path

from .views import GithubView

urlpatterns = [
    # ex: /
    path('', GithubView.as_view(), name='index'),
]