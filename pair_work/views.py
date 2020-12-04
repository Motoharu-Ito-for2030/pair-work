from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import User, Work
# Create your views here.


def pairwork(request):
  return render(request, 'index.html')

def home(request):
  return render(request, 'pages/home.html')

def postwork(request):
  return render(request, 'pages/postwork.html')

def process_form_user(request):
  if request.POST.get('name'):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    con_password = request.POST['con_password']

    if name.strip() == '' or email.strip() == '' or password.strip() == '':
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
        return render(request, 'pages/in.html')
    
  
  me = User.objects.get(email=email)
  user_id = me.id
  user_name = me.name
  user_email = me.email
  data = {
      'id': user_id,
      'email': user_email,
      'name': user_name,
  }
  
  def mywork(request):
    response = redirect('mywork')
    get_params = request.GET.urlencode()
    response['location'] += '?'+get_params
    return response
  
  return mywork(request)

    
    

def detail(request):
  return render(request, 'pages/detail.html')

def users(request):
  return render(request, 'pages/users.html')

def in_(request):
  return render(request, 'pages/in.html')


