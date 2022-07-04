from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
import requests
import json


def vue_test(request):
    return render(request, 'vueTest.html')

def homepage(request):
  userResult = requests.get('http://localhost:8000/api/usernotes?username=jeff')
#  userResult = requests.get('http://localhost:8000/api/notes?user=jeff')
  print(userResult)
  print(userResult.status_code)
  print(userResult.text)
  print(userResult.json())

  params = {
    'token': '6a13b32ec7b4d657413e112318720ad81cffd31cccccc',
    'user': 'jeff2'
  }

  
  '''
  testResult = requests.post('http://localhost:8000/api/notes/', data=params)

  print(testResult)
  print(testResult.status_code)
  print(testResult.text)
  print(testResult.json())
  '''
  current_user = request.user
  print(current_user)

  return render(request, "home.html")

def register(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f"New account created: {username}")
      login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    else:
      messages.error(request,"Account creation failed")

    return redirect("main:homepage")

  form = UserCreationForm()
  return render(request,"register.html", {"form": form})

# This should maybe be renamed Git_Redirect?
def auth_git(request):
    #check if user has a token
    current_user = request.user
    print(current_user)

    client_id = '7016049256e3a53a9d63'
    scope = 'read:user'
    state = 'somerandomstring123'  # to prevent csrf
    return redirect(
        'https://github.com/login/oauth/authorize?client_id={}&scope={}&state={}'.format(client_id,
                                                                                         scope, state,
                                                                                         ))


def authgit_callback(request):
    # verify the state variable value for csrf
    code = request.GET.get('code', None)
    print(request)
   # print(request.access_token)

     # after redirect
    params = {
        'client_id': '7016049256e3a53a9d63',
        'client_secret': '',
        'code': code,
        'Content-Type': 'application/json'
    }

    headers = {
        'Accept': 'application/json'
    }

    result = requests.post('https://github.com/login/oauth/access_token', data=params, headers=headers)
    print(result)
    print(result.text)
    print(result.json())
    print(result.status_code)


    accessToken = result.json()['access_token']


    print(accessToken)

    ##store token in database

    tokenHeader = 'token '
    authHeaderValue = tokenHeader + accessToken


    userParams = {
        'Authorization': authHeaderValue,
    }

    userHeaders = {
        'Authorization': authHeaderValue,
    }
    userResult = requests.get('https://api.github.com/user', headers=userHeaders)

    print(userResult)
    print(userResult.text)
    print(userResult.json())
    print(userResult.status_code)

    if "error" in userResult.json():
        print("Key exist in JSON data")


    if userResult.status_code == 401:
        client_id = '7016049256e3a53a9d63'
        scope = 'read:user'
        state = 'somerandomstring123'  # to prevent csrf
        return redirect(
            'https://github.com/login/oauth/authorize?client_id={}&scope={}&state={}'.format(client_id,
                                                                                         scope, state,
                                                                                         ))


    userLogin = userResult.json()['login']


    return render(request, "auth_git_callback.html", {"response": userResult, "userLogin": userLogin})




def auth_git_callback(request):
  return render(request, "auth_git_callback.html")