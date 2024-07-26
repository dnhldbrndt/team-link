# core/urls.py

from django.urls import path
from .views import home_view, profile_view, project_create_view, project_list_view, bookmark_project_view, dashboard_view, search_view

urlpatterns = [
    path('', home_view, name='home'),  # Home page
    path('profile/', profile_view, name='profile'),
    path('create-project/', project_create_view, name='create_project'),
    path('projects/', project_list_view, name='project_list'),
    path('bookmark/<int:project_id>/', bookmark_project_view, name='bookmark_project'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('search/', search_view, name='search'),
]
