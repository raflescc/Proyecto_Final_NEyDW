from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Artwork
from .forms import ArtworkForm

# Create your views here.

def artwork_list(request):
    artworks = Artwork.objects.filter(is_available=True)
    return render(request, 'marketplace/list.html', {'artworks': artworks})

def artwork_detail(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    return render(request, 'marketplace/detail.html', {'artwork': artwork})

@login_required
def create_artwork(request):

    # Solo artistas
    if request.user.role != 'artist':
        return redirect('artwork_list')

    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist = request.user
            artwork.save()
            return redirect('artwork_detail', artwork.id)
    else:
        form = ArtworkForm()

    return render(
        request,
        'marketplace/create_artwork.html',
        {'form': form}
    )

@login_required
def my_artworks(request):

    if request.user.role != 'artist':
        return redirect('artwork_list')

    artworks = Artwork.objects.filter(artist=request.user)

    return render(
        request,
        'marketplace/my_artworks.html',
        {'artworks': artworks}
    )