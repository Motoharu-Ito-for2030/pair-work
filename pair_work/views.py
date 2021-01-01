from monthdelta import monthmod  # エラー出たら pip install MonthDelta
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import User, Work, Goal
from urllib.parse import urlencode
from datetime import datetime, date
import calendar
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
  will_reach_at = request.POST['will_reach_at']
  dateTime = datetime.now()
  
  if name.strip() == '' or text.strip() == '':
      print('<script>window.alert("error 1");</script>')
      return render(request, 'pages/error.html')
  if user_id == None:
    return render(request, 'pages/error.html')


  new_work= Work(user_id=user_id, name=name, text=text, created_at=dateTime,will_reach_at=will_reach_at)
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

    
    

def detail(request, user_id,id):
  the_detail = Work.objects.get(id=id)
  the_goals = Goal.objects.filter(work_id=id)
  dt1 = the_detail.created_at
  dt2 = the_detail.will_reach_at
  # ２つの日付の差を、月単位/年単位で求める -----------
  # (monthdelta(20), datetime.timedelta(days=25)) <-タプル（リストみたいなもん）
  mmod = monthmod(dt1, dt2)

  ## 月数差（余りは切り捨て）
  months = mmod[0].months # 20

  ## 年数差（余りは切り捨て）月数差を12で割ります。月の日数は色々ですが、年の月数は常に12なのでこれでok
  years = mmod[0].months//12  # 1
  created_at = the_detail.created_at. strftime ( '%Y年%m月%d日' ) 
  will_reach_at = the_detail.will_reach_at. strftime ( '%Y年%m月%d日' ) 
  data = {
      'user_id': user_id,
      'detail': the_detail,
      'months': range(months),
      'years': years,
      'created_at': created_at,
      'will_reach_at': will_reach_at,
      'the_goals': the_goals,
  }
  return render(request, 'pages/detail.html', data)

def users(request, user_id):
  all_users = User.objects.all().values()
  data = {
      'user_id': id,
      'users': all_users,
  }
  return render(request, 'pages/users.html', data)

def in_(request):
  return render(request, 'pages/in.html')

def delete(request):
  name = request.POST['name']
  user_id = request.POST['user_id']
  the_pastime = Work.objects.get(name=name,user_id=user_id)
  the_pastime.delete()
  the_user = User.objects.get(id=user_id)
  return redirect(the_user)


def post_goal(request):
  months = request.POST['months']
  work_id = request.POST['work_id']
  goals = request.POST.getlist('goal')
  for index, i in enumerate(goals):
    if i != '':
      month_id = index
      goal = i
      new_goal = Goal(work_id=work_id, goal=i, month_id=month_id)
      new_goal.save()
    else:
      continue
  work = Work.objects.get(id=work_id)
  return redirect(work)
