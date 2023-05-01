from django.shortcuts import render
from .models import Gene
from .models import Property
# Create your views here.

def main(request):
    return render(request, 'Gene/main.html')

def gene_info(request):
    context = dict()
    context['property'] = Property.objects.all()
    return render(request, 'Gene/gene_info.html', context=context)

def avatar_game(request):
    return render(request, 'Gene/avatar_game.html')

def gene_list(request, property_id):
    context = dict()
    genes = Gene.objects.filter(property_id_id=property_id)
    context['genes'] = genes
    return render(request, 'Gene/gene_list.html', context=context)

def habits(request, gene_name):
    return render(request, 'Gene/habits.html')

def daily_question(request):
    return render(request, 'Gene/daily_question.html')

def my_page(request):
    return render(request, 'Gene/my_page.html')