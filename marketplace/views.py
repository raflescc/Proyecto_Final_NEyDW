from django.shortcuts import render, get_object_or_404, redirect
from .models import Artwork

# Create your views here.

def artwork_list(request):
    artworks = Artwork.objects.filter(is_available=True)
    return render(request, 'marketplace/list.html', {'artworks': artworks})

def artwork_detail(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    return render(request, 'marketplace/detail.html', {'artwork': artwork})
