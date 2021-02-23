import json

from django.shortcuts import render

# Create your views here.

from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
import datetime
from ubs_project import models



def CORSResp(response):
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1000'
    response['Access-Control-Allow-Headers'] = '*'


def registrationPage(request):
    return render(request, 'registration_page.html')

def loginPage(request):
    return render(request, 'login_page.html')


@csrf_exempt
def registrationStudent(request):
    if request.method != 'POST':
        response = HttpResponse(content={}, content_type='application/json', status=400)
        return response

    respContent = {
        'status': 0,
        'desc': ''
    }

    email = request.POST.get('email')
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    password = request.POST.get('password')

    if email == '' or firstName == '' or lastName == '' or password == '':
        respContent['status'] = -1
        respContent['desc'] = 'Incorrect user input format'
        response = HttpResponse(json.dumps(respContent), content_type='application/json', status=400)
        return response

    if email is None or firstName is None or lastName is None or password is None:
        respContent['status'] = -1
        respContent['desc'] = 'Incorrect user input format'
        response = HttpResponse(json.dumps(respContent), content_type='application/json', status=400)
        return response

    studentData = {
        'first_name': firstName,
        'last_name': lastName,
        'email': email,
        'password': password,
        'created_at': datetime.datetime.now()
    }

    if models.Student.objects.filter(email=studentData['email']).count() != 0:
        respContent['status'] = -1
        respContent['desc'] = 'The email has been registered'
        response = HttpResponse(json.dumps(respContent), content_type='application/json', status=400)
        return response

    student = models.Student(**studentData)
    student.save()
    response = HttpResponse(content=json.dumps(respContent), content_type='application/json', status=200)

    CORSResp(response)
    return response
