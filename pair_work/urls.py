from django.urls import path
from pair_work import views

urlpatterns = [
    path('', views.pairwork, name='pairwork'),
    path('home', views.home, name='home'),
    path('postwork', views.postwork, name='postwork'),
    path('process_form_user', views.process_form_user, name='process_form_user'),
    path('detail', views.detail, name='detail'),
    path('users', views.users, name='users'),
    path('in_', views.in_, name='in_'),
]
