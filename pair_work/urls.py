from django.urls import path
from pair_work import views
urlpatterns = [
    path('', views.pairwork, name='pairwork'),
    path('home', views.home, name='home'),
    path('postwork/<int:id>', views.postwork, name='postwork'),
    path('process_form_user',views.process_form_user, name='process_form_user'),
    path('process_form_work',views.process_form_work, name='process_form_work'),
    path('delete',views.delete, name='delete'),
    path('detail/<int:user_id>/<int:id>/', views.detail, name='detail'),
    path('post_goal', views.post_goal, name='post_goal'),
    path('users/<int:user_id>/', views.users, name='users'),
    path('in_', views.in_, name='in_'),
    path('login', views.login, name='login'),
    path('redirect_user/<int:id>/', views.redirect_user, name='redirect_user'),
    path('mywork', views.mywork, name='mywork'),
    path('mywork/<int:id>/', views.mywork, name='myownwork'),
]
