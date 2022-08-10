from django.shortcuts import render, redirect
from .models import Vete

# Create your views here.
def list_vete(request):
    vete = Vete.objects.all()
    return render(request, 'vete.html', {"vete":vete})

def create_vete(request):
    vete = Vete(dueño=request.POST['dueño'], apellido=request.POST['apellido'], mascota=request.POST['mascota'], raza=request.POST['raza'], agencia=request.POST['agencia'])
    vete.save()
    return redirect('/vete/')

def delete_vete(request, vete_id):
    vete = Vete.objects.get(id=vete_id)
    vete.delete()
    return redirect('/vete/')