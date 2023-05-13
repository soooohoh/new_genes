from typing import Any, Optional
from django.db import models
from django.shortcuts import render, redirect, reverse
from .models import Property, Gene, Eating_Habits
from Gene.models import User
from .forms import GeneForm, User_Profile_Form
from Gene.models import LifeStyle
from django.views.generic import DetailView, UpdateView

# Create your views here.
def home(request):
    return render(request, 'Gene/home.html')

def my_page(request):
    context=dict()
    data = Property.objects.all()
    context['property']=data

    return render(request, 'Gene/my_page.html', context=context)

def property_confirm(request):
    context=dict()
    data = Property.objects.all()
    context['property'] = data
    
    return render(request, 'Gene/property_confirm.html', context=context)

def gene_register(request, property_id):
    if request.POST=="POST":
        return render(request, 'Gene/property_confirm.html')
                    
    else:
        data = Gene.objects.filter(property=property_id)
        context=dict()
        context['gene']=data
        return render(request, 'Gene/gene_register.html', context=context)

def habits(request, gene_name):    
    data = Eating_Habits.objects.filter(gene_name=gene_name) # get방식으로 가져오면 multiple에러???
    style_data = LifeStyle.objects.filter(gene_name=gene_name)
    context=dict()
    context['data'] = data
    context['style_data'] = style_data
    return render(request, 'Gene/habits.html', context=context)


def avatar_game(request):
    return render(request, 'Gene/avatar_game.html')


def daily_question(request):
    return render(request, 'Gene/daily_question.html')




class ProfileReadView(DetailView):
    model = User
    template_name = 'Profile/profile_detail.html'
    pk_url_kwarg = "user_id"


class ProfileUpdateView(UpdateView):
    model = User
    form_class = User_Profile_Form
    template_name = 'Profile/profile_form.html'
    pk_url_kwarg = "user_id"

    def get_success_url(self):
        return reverse('profile', kwargs={ "user_id" : self.object.id })









