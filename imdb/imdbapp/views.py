from email.mime import image
from multiprocessing import context
from django.shortcuts import render, redirect
from imdbapp.forms import Movie_Form
from imdbapp.models import Movie

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request,'index.html', context)

def details(request,id):
    movie = Movie.objects.get(id=id)
    return render(request, 'details.html', {'movie':movie})

def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        year = request.POST.get('year')
        image = request.FILES['image']
        app = Movie(name=name, description=description, year=year, image=image)
        app.save()
    return render(request, 'add.html')

def update(request,id):
    movie = Movie.objects.get(id=id)
    form = Movie_Form(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form':form, 'movie':movie})

def delete(request,id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')