from django.urls import path
from pair_work import views
urlpatterns = [
    path('', views.pairwork, name='pairwork'),
    path('home', views.home, name='home'),
    # path('postwork', views.postwork, name='postwork'),
    path('postwork/<int:id>', views.postwork, name='postwork'),
    path('process_form_user',views.process_form_user, name='process_form_user'),
    path('process_form_work',views.process_form_work, name='process_form_work'),
    path('detail', views.detail, name='detail'),
    path('users', views.users, name='users'),
    path('in_', views.in_, name='in_'),
    path('login', views.login, name='login'),
    path('mywork', views.mywork, name='mywork'),
    path('mywork/<int:id>/', views.mywork, name='myownwork'),
]
