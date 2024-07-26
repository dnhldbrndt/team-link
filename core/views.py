# core/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Bookmark
from .forms import ProfileForm, ProjectForm

def home_view(request):
    return render(request, 'core/home.html')

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'core/profile.html', {'form': form})

@login_required
def project_create_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'core/project_form.html', {'form': form})

@login_required
def project_list_view(request):
    projects = Project.objects.all()
    return render(request, 'core/project_list.html', {'projects': projects})

@login_required
def bookmark_project_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    Bookmark.objects.get_or_create(user=request.user, project=project)
    return redirect('project_list')

@login_required
def dashboard_view(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'core/dashboard.html', {'bookmarks': bookmarks})

def search_view(request):
    query = request.GET.get('q')
    if query:
        users = Profile.objects.filter(user__username__icontains(query))
        projects = Project.objects.filter(title__icontains(query))
    else:
        users = Profile.objects.none()
        projects = Project.objects.none()
    return render(request, 'core/search.html', {'users': users, 'projects': projects})
