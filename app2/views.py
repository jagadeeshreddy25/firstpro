from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse('good finsher')
def jaddu(request):
    return HttpResponse('<h1><marquee>best allrounder</marquee></h1>')