from django.shortcuts import render
from .models import Property, Gene, Eating_Habits
from .forms import GeneForm
from .models import Lifestyle
# Create your views here.
def home(request):
    return render(request, 'Gene/home.html')

def my_page(request):
    context=dict()
    data = Property.objects.all()
    context['property']=data

    return render(request, 'Gene/my_page.html', context=context)

def daily_question(request):
    return render(request, 'Gene/daily_question.html')

def gene_register(request, property_id):
    if request.POST=="POST":
        pass
                    
    else:
        data = Gene.objects.filter(property_id_id=property_id)
        context=dict()
        context['gene']=data
        form = GeneForm()
        context['form']=form
        return render(request, 'Gene/gene_register.html', context=context)

def habits(request, gene_name):    
    data = Eating_Habits.objects.filter(gene_name=gene_name) # get방식으로 가져오면 multiple에러???
    style_data = Lifestyle.objects.filter(gene_name=gene_name)
    context=dict()
    context['data'] = data
    context['style_data'] = style_data
    return render(request, 'Gene/habits.html', context=context)


def avatar_game(request):
    return render(request, 'Gene/avatar_game.html')
