from django.shortcuts import render
from django.shortcuts import render, redirect
from . import models
# from manga.form import FormManga
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def index (request):
    return render(request, 'pengguna/index.html')

def user(request):
   
    return render(request, 'pengguna/user.html')

def tabel (request):
   
    return render(request, 'pengguna/tabel.html')

def icon (request):
   
    return render(request, 'pengguna/icon.html')


def typo (request):
   
    return render(request, 'pengguna/typo.html')

# PENGAJAR

# def tampilguru(request):
#     if request.POST:
#         models.pengajar.objects.all()
        
#     ptampil = models.pengajar.objects.all()
#     return render(request, 'pengajar.html',
# 		{ 'data': ptampil,
# 		})

# def detailguru(request, id):
# 	gdetail = models.pengajar.objects.filter(pk=id).first()
# 	return render(request, 'detailpengajar.html',
# 		{ 'data': gdetail,
# 		})

# # MURID

# def tampilmurid(request):
#     if request.POST:
#         models.murid.objects.all()
        
#     mtampil = models.murid.objects.all()
#     return render(request, 'murid.html',
# 		{ 'data': mtampil,
# 		})

# def detailmurid(request, id):
# 	mdetail = models.murid.objects.filter(pk=id).first()
# 	return render(request, 'detailmurid.html',
# 		{ 'data': mdetail,
# 		})