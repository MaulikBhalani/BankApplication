from contextlib import nullcontext
import re
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import customer,transaction_details
#from django.http import HttpResponse
from django.db.models import F, query
from datetime import datetime

# Create your views here.

def index(request):
    return render(request,'index.html')


def customer_details(request):
    all_entries = customer.objects.all()
    context = {
        "cust_details" : all_entries
    }
    return render(request, 'customer.html', context)

def view(request):
    if request.method == "POST":
         cust = request.POST.get('submit')
         query1 = customer.objects.get(name = cust)
         query2 = customer.objects.exclude(name = cust)

         #query3 = customer.objects.get(account_number = query1.account_number)
         #print(query3)

         #query3 = customer.objects.get(name = cust)

         context = {
             "cust_name" : query1,
             "all_details" : query2,
             }    

    return render(request, 'view.html', context)


def transaction(request):
    if request.method =="POST":
        receiver= request.POST.get('to')
        money = request.POST.get('amount2')
        sender = request.POST.get('submit')
        query2 = customer.objects.get(name = sender)
        query2.amount= F('amount')- money
        query2.save()
        query1 = customer.objects.get(name= receiver)       
        query1.amount= F('amount')+ money
        query1.save()
        result = customer.objects.get(name = sender)
        transact = transaction_details()
        transact.source_name = sender
        transact.source_acc_no = result.account_no
        transact.Current_balance = result.amount
        transact.money_deposit = money
        transact.destination_name = receiver
        transact.date = datetime.today()
        transact.save()
        return redirect('customer')
    all_entries = transaction_details.objects.all()
    context = {
            "history" : all_entries
        }
    return render(request, 'transaction.html', context)

def about_us(request):
    return render(request, 'about_us.html')