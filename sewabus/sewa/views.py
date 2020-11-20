from django.shortcuts import render
# from . import models

def index(req):
    # task = models.Pasien.objects.all()
    return render(req, 'sewa/index.html')