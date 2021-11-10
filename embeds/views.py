from django.db.models import query
from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import Embed

def signup(request):
    if request.user.is_authenticated:
        return redirect('embed:index')
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfullly')
            return redirect('signup')
    else:
        f = UserCreationForm()
    return render(request, 'embeds/signup.html', {'form': f})

def index(request):
    
    try:
        last_embed = Embed.objects.order_by('-creation_date')[0]
        latest_embed_list = Embed.objects.order_by('-creation_date')[1:6]
        context = {
            'last_embed': last_embed,
            'latest_embed_list': latest_embed_list,
        }
        return render(request, 'embeds/index.html', context)
    except IndexError:
        raise Http404('There are no embeds')

def detail(request, embed_id):
    embed = get_object_or_404(Embed, pk=embed_id)
    return render(request, 'embeds/detail.html', {'embed': embed})

def list(request):
    embed_list = Embed.objects.all()
    return render(request, 'embeds/list.html', {'embed_list': embed_list}) 

def add(request, embed_id):
    return render(request, 'embeds/add.html', {'embed_id': embed_id})