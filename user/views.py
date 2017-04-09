from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Info
from django.db import models
from django.db import connection
import hashlib


def user(request):
    return render(request,'user/index.html',{})

def sub(request):

    user_data=Info(fname=request.POST['fname'], lname=request.POST['lname'], email=request.POST['email'], password=request.POST['password'])
    user_data.save()
    cursor=connection.cursor()
    key=str(user_data.id)+"69"
    hashed_key=hashlib.sha1(key.encode('utf-8')).hexdigest()
    cursor.execute('CREATE TABLE %s ( cart varchar(31) )'%hashed_key)


def cart(request):
    cursor=connection.cursor()
    cursor.execute("CREATE TABLE %s ( cart varchar(31) )"%request.POST['fname'])
