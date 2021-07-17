from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class DetailView(TemplateView):
    template_name='theme/company-detail.html'

class LoginView(TemplateView):
    template_name='theme/company-login.html'

class PeopleView(TemplateView):
    template_name='theme/company-people.html'

class SettingsView(TemplateView):
    template_name='theme/company-settings.html'

class SignupView(TemplateView):
    template_name='theme/company-signup.html'

class TaskDetailView(TemplateView):
    template_name='theme/company-task-detail.html'

class TaskView(TemplateView):
    template_name='theme/company-task.html'