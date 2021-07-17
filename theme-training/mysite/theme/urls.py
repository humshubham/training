from django.urls import path, include
from . import views

app_name = 'theme'

urlpatterns = [
    path('detail/', views.DetailView.as_view(), name='detail'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('people/', views.PeopleView.as_view(), name='people'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('task-detail/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/', views.TaskView.as_view(), name='task'),
]