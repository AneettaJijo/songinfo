from django.http import HttpResponse
from django.shortcuts import render, redirect

from artist.forms import SongForm
from artist.models import Songs



def tracks(request):
    songs=Songs.objects.all()
    content={'song_list':songs}
    return render(request,'index.html',content)

def details(request, song_id):
    songs=Songs.objects.get(id=song_id)
    return  render(request,'details.html',{'songs':songs})

def add(request):
    if request.method == "POST":
        name=request.POST.get('name',)
        artist=request.POST.get('artist',)
        year=request.POST.get('year',)
        image=request.FILES['image']
        song=Songs(name=name,artist=artist,year=year,image=image)
        song.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    song=Songs.objects.get(id=id)
    form=SongForm(request.POST or None,request.FILES, instance=song)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'song':song})

def delete(request,id):
    if request.method=="POST":
        song=Songs.objects.get(id=id)
        song.delete()
        return redirect('/')
    return render(request,'delete.html')
