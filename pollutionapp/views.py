import json

import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth

from pollutionapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from pollutionapp.models import Contact, Donate, WaterData, Register


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def resources(request):
    return render(request, 'resources.html')

def blogdetails(request):
    return render(request, 'blog-details.html')

def contact(request):
    if request.method == 'POST':
        contactus=Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        contactus.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')


def token(request):
    consumer_key = 'NRtduCNIFmM5L9i02lwdIJUFUw2LQWGwoMqh0m4w05SFlw8V'
    consumer_secret = 'ZNrKHhgkr6IMHLuJPgGeISYj09koXR29rAsEAZ4HH58H1OJ7fdqEEUyneDAtzETt'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})


def donate(request):
    if request.method == 'POST':
        donatetous=Donate(
            name = request.POST['name'],
            date = request.POST['date'],
            email = request.POST['email'],
            amount = request.POST['amount'],
            phone = request.POST['phone'],
            message = request.POST['message'],
        )
        donatetous.save()
        return redirect('/donate')
    else:
        return render(request, 'donate.html')

def stk(request):
    if request.method =="POST":
        amount = request.POST['amount']
        phone = request.POST['phone']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "CleanSphere",
            "TransactionDesc": "Donation"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Thank you for supporting our work!!")

@login_required
def watertracker(request):
    if request.method == "POST":
        allwaterdata=WaterData(
            name = request.POST['name'],
            latitude = request.POST['latitude'],
            longitude = request.POST['longitude'],
            date = request.POST['date'],
            time = request.POST['time'],
            waterbody = request.POST['waterbody'],
            water_colour= request.POST['watercolour'],
            smell = request.POST['unusualsmell'],
            odor_description = request.POST['odor'],
            pollution_evidence= request.POST['pollutiontype'],
            turbidity= request.POST['turbidity'],
            ph=request.POST['ph'],
            nitrates=request.POST['nitrates'],
            phosphates=request.POST['phosphates'],
            oxygen=request.POST['oxygen'],
            algae_blooms=request.POST['algaeblooms'],
            aquatic_life=request.POST['aquaticlife'],

        )
        allwaterdata.save()
        return redirect('/watertracker')
    else:
        return render(request, 'watertracker.html')



def waterdata(request):
    waterdataall=WaterData.objects.all()
    return render(request, 'waterdata.html', {'waterdata':waterdataall})

def delete(request,id):
    water = WaterData.objects.get(id=id)
    water.delete()
    return redirect('/waterdata')

def register(request):
    if request.method == "POST":
        register=Register(
            username = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password'],

        )
        register.save()
        return redirect('/login')
    else:
        return render(request, 'Register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            return redirect('/watertracker')  # Redirect to water tracker page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')
