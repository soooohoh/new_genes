<<<<<<< HEAD
#from typing import Any, Optional
#from django.db import models
#from django.shortcuts import render, redirect
#from .models import Property, Gene, Eating_Habits
#from Gene.models import User
#from .forms import GeneForm, User_Profile_Form
#from Gene.models import LifeStyle
#from django.views.generic import DetailView, UpdateView
#from django.urls import reverse
from typing import Any, Optional
from django.db import models
from django.shortcuts import render, redirect ,get_object_or_404
from django.urls import reverse
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView,
                                  DeleteView)
from allauth.account.models import EmailAddress
from Gene.models import  User, Property
from Gene.forms import User_Profile_Form
from .models import Property, Gene, Eating_Habits, LifeStyle
from allauth.account.views import PasswordChangeView




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

def gene_info(request, property_id):
    context = dict()
    gene_data = Gene.objects.filter(property_id=property_id)
    context['gene_data'] = gene_data
    return render(request, 'Gene/gene_info.html', context=context)


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





#프로필 Read
class ProfileReadView(DetailView):
    model = User
    template_name = 'Profile/profile_detail.html'
    pk_url_kwarg = "user_id"
    context_object_name = "profile_user"




#프로필 Create
class ProfileSetView(UpdateView):
    model = User
    form_class = User_Profile_Form
    template_name = "Profile/profile_set_form.html"

    def get_object(self, queryset=None):        
        return self.request.user
    
    def get_success_url(self):
        return reverse("home")
    




#프로필 Update
#class ProfileUpdateView(UpdateView):
 #   model = User
  #  form_class = User_Profile_Form
   # template_name = 'Profile/profile_form.html'
   # pk_url_kwarg = 'user_id'


    #def get_success_url(self):
    #    return reverse("home")     
    #def get_success_url(self):
    #    user_id = self.kwargs.get("user_id")
    #    return reverse('profile', kwargs={ "user_id" : user_id })

def ProfileUpdateView(request, user_id):
    object = User.objects.get(id=user_id)
    if request.method=="POST":
        user_form = User_Profile_Form(request.POST, instance=object)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile', user_id=object.id)
                
    else:
        user_form = User_Profile_Form(instance=object)
        
    return render(request, "Profile/profile_form.html", {'form' : user_form})



# 패스워드 변경 뷰
class CustomPasswordChangeView(PasswordChangeView):
    
    def get_success_url(self):
        return reverse('profile', kwargs={'user_id' : self.request.user.id})



=======
#from typing import Any, Optional
#from django.db import models
#from django.shortcuts import render, redirect
#from .models import Property, Gene, Eating_Habits
#from Gene.models import User
#from .forms import GeneForm, User_Profile_Form
#from Gene.models import LifeStyle
#from django.views.generic import DetailView, UpdateView
#from django.urls import reverse
from typing import Any, Dict, Optional
from django.db import models
from django.shortcuts import render, redirect ,get_object_or_404
from django.urls import reverse
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView,
                                  DeleteView)
from allauth.account.models import EmailAddress
from Gene.models import  User, Property, Diary
from Gene.forms import User_Profile_Form, User_Diary_Form
from .models import Property, Gene, Eating_Habits, LifeStyle
from allauth.account.views import PasswordChangeView




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

def gene_info(request, property_id):
    context = dict()
    gene_data = Gene.objects.filter(property_id=property_id)
    context['gene_data'] = gene_data
    return render(request, 'Gene/gene_info.html', context=context)


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







#프로필 Read
class ProfileReadView(DetailView):
    model = User
    template_name = 'Profile/profile_detail.html'
    pk_url_kwarg = "user_id"
    context_object_name = "profile_user"



#프로필 Create
class ProfileSetView(UpdateView):
    model = User
    form_class = User_Profile_Form
    template_name = "Profile/profile_set_form.html"

    def get_object(self, queryset=None):        
        return self.request.user
    
    def get_success_url(self):
        return reverse("home")
    


#프로필 Update
def ProfileUpdateView(request, user_id):
    object = User.objects.get(id=user_id)
    if request.method=="POST":
        user_form = User_Profile_Form(request.POST, instance=object)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile', user_id=object.id)
                
    else:
        user_form = User_Profile_Form(instance=object)
        
    return render(request, "Profile/profile_form.html", {'form' : user_form})



# 패스워드 변경 뷰
class CustomPasswordChangeView(PasswordChangeView):
    
    def get_success_url(self):
        return reverse('profile', kwargs={'user_id' : self.request.user.id})



# 다이어리 Read 뷰
class Gene_Diary_List_View(ListView):
    model = Diary
    template_name = "Diary/diary_list.html"
    pk_url_kwarg = "user_id"
    paginate_by = 4
    #ordering = ["dt_created"]
    context_object_name = "all_diary"


    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Diary.objects.filter(user__id=user_id).order_by("dt_created")
    

    #특정 유저가 작성한 다이어리만을 뽑는다.
    def get_context_data(self, **kargs):
        context = super().get_context_data(**kargs)
        context['profile_user'] = get_object_or_404(User, id=self.kwargs.get("user_id"))
        return context
    

class Gene_Diary_Detail_View(DetailView):
    model = Diary
    template_name = "Diary/diary_detail.html"
    context_object_name = "diary"
    pk_url_kwarg = "diary_id"


class Gene_Diary_Create_View(CreateView):
    model = Diary
    form_class = User_Diary_Form
    template_name = "Diary/diary_form.html"

    # 생성 중인 다이어리의 외래키가 현재 로그인 한 유저로 설정.
    def form_valid(self, form): 
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('gene_diary_detail', kwargs={"diary_id" : self.object.id})
    

class Gene_Diary_Update_View(UpdateView):
    model = Diary
    pk_url_kwarg = "diary_id"
    template_name = "Diary/diary_form.html"
    form_class = User_Diary_Form

    def get_success_url(self):
        return reverse("gene_diary_detail", kwargs={"diary_id" : self.object.id})


class Gene_Diary_Delete_View(DeleteView):
    model = Diary
    pk_url_kwarg = "diary_id"
    get_object_name = "diary"
    template_name = "Diary/diary_delete.html"

    def get_success_url(self):
        return reverse("gene_diary_list", kwargs={"user_id" : self.request.user.id})
>>>>>>> 4ca6192e24e793c4a9b51441f48dee89750917f2
