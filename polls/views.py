import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core import serializers

from django.core.checks.security import csrf

from django.http.response import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from polls.models import UserForm

@csrf_exempt
def index(request):
    print "hola"
    #     if request.user.is_authenticated():
    #         lista_imagenes = Imagen.objects.filter(user=request.user)
    #     else:
    #         lista_imagenes = Imagen.objects.all()
    # #1.    context = {'lista_imagenes': lista_imagenes}
    # #1.    return render(request, 'polls/index.html', context)
    #return HttpResponse(serializers.serialize("json", lista_imagenes))

@csrf_exempt
def add_image(request):
    if request.method == 'POST':
        print "hola"
        #1.form = ImagenForm(request.POST, request.FILES)
        #1.if form.is_valid():
            # new_image = Imagen(url=request.POST['url'],
            #                    title=request.POST['title'],
            #                    description=request.POST['description'],
            #                    type=request.POST['type'],
            #                    imageFile=request.FILES['imageFile'],
            #                    user=request.user)
            # new_image.save()
            #1.return HttpResponseRedirect(reverse('images:index'))
    #1.else:
        #1.form = ImagenForm()

    #1.return render(request,'polls/image_form.html',{'form':form})
    #return HttpResponse(serializers.serialize("json", [new_image]))
    return render(request, "polls/index.html")

@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        first_name = jsonUser['first_name']
        last_name = jsonUser['last_name']
        password = jsonUser['password']
        email = jsonUser['email']

        user_model = User.objects.create_user(username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))

@csrf_exempt
def login_view(request):
    mensaje = ''
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            mensaje = "ok"
        else:
            mensaje = 'Nombre de usuario o clave no valido'
    return JsonResponse({"mensaje": mensaje})

@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"mensaje": "ok"})

@csrf_exempt
def islogged_view(request):
    if request.user.is_authenticated():
        mensaje = 'ok'
    else:
        mensaje = 'no'

    return JsonResponse({"mensaje": mensaje})

def is_logged_view(request):
    if request.user.is_authenticated():
        mensaje = 'ok'
    else:
        mensaje = 'no'
    return JsonResponse({'mensaje':mensaje})

def ir_index(request):
    return render(request,"polls/index.html")

def agregar_imagen(request):
    return render(request, "polls/image_form.html")

def agregar_usuario(request):
    return render(request, "polls/registro.html")

def ingresar(request):
    return render(request, "polls/login.html")