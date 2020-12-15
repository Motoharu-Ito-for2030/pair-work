from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import User, Work
from urllib.parse import urlencode
from datetime import datetime
# Create your views here.


def pairwork(request):
  
  return render(request, 'index.html')

def home(request):
  return render(request, 'pages/home.html')

def login(request):
  return render(request, 'pages/login.html')

def postwork(request, id):
  the_user = User.objects.get(id= id)
  user_name = the_user.name
  user_email = the_user.email
  data = {
      'user_id': id,
      'name': user_name,
  }
  return render(request, 'pages/postwork.html', data)


def process_form_user(request):
  if request.POST.get('name'):
      name = request.POST['name']
      email = request.POST['email']
      password = request.POST['password']
      con_password = request.POST['con_password']

      if name.strip() == '' or email.strip() == '':
          print('<script>window.alert("error 1");</script>')
          return render(request, 'pages/error.html')

      if con_password != password:
          print('<script>window.alert("error");</script>')
          return render(request, 'pages/error.html')

      if User.objects.filter(email=email).exists():
          # email already registered
          return render(request, 'pages/error.html')

      new_user = User(name=name, email=email, password=password)
      new_user.save()
  else:
      email = request.POST['email']
      password = request.POST['password']
      # user_info = user.objects.values()
      
      if User.objects.filter(email=email).exists() and User.objects.filter(password=password).exists():
      # sign in
          pass
      else:
          return render(request, 'pages/error.html')
  
  
  the_user = User.objects.get(email=email)
  return redirect(the_user)

def process_form_work(request):
  name = request.POST['name']
  text = request.POST['text']
  user_id = request.POST['user_id']
  dateTime = datetime.now()
  
  if name.strip() == '' or text.strip() == '':
      print('<script>window.alert("error 1");</script>')
      return render(request, 'pages/error.html')
  if user_id == None:
    return render(request, 'pages/error.html')

  if Work.objects.filter(text=text).exists():
      # text already registered
      return render(request, 'pages/error.html')

  new_work= Work(user_id=user_id, name=name, text=text, created_at=dateTime)
  new_work.save()
  
  
  the_user= User.objects.get(id=user_id)
  return redirect(the_user)

def redirect_user(request, id):
  the_user = User.objects.get(id=id)
  return redirect(the_user)

def mywork(request, id):
  the_works = Work.objects.filter(user_id=id)
  the_user = User.objects.get(id=id)
  user_name = the_user.name
  user_email = the_user.email
  data = {
      'user_id': id,
      'email': user_email,
      'name': user_name,
      'works': the_works
  }
  return render(request, 'pages/mywork.html', data)

    
    

def detail(request):
  return render(request, 'pages/detail.html')

def users(request, user_id):
  all_users = User.objects.all().values()
  data = {
      'user_id': id,
      'users': all_users,
  }
  return render(request, 'pages/users.html', data)

def in_(request):
  return render(request, 'pages/in.html')


