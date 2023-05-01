from django.shortcuts import render
from .models import Property, Gene
from .forms import GeneForm

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
            data = Gene.objects.filter(property_id_id=property_id)
            context=dict()
            context['gene']=data
            return render(request, 'Gene/gene_register.html', context=context)
    else:
        data = Gene.objects.filter(property_id_id=property_id)
        context=dict()
        context['gene']=data
        form = GeneForm()
        context['form']=form
        return render(request, 'Gene/gene_register.html', context=context)