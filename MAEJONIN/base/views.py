from django.shortcuts import render
from .models import Category, Photo
# Create your views here.
def home(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories':categories, 'photos':photos}
    return render(request, 'base/index.html', context)