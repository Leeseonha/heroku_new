from django.shortcuts import get_object_or_404, render, redirect
from .forms import DetailForm
from .models import Detail
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.conf.urls.static import static
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

def index(request):
        return render(request, 'index.html')

def layout(request):
        return render(request, 'layout.html')

# '자세히' 페이지 입니다.
def detail(request, board_id):
        board_detail = get_object_or_404(Detail , pk = board_id)
        return render(request, 'detail.html', {'board' : board_detail})

# 홈입니다.
#def home(request):
#      boards = Detail.objects
#        return render(request, 'home.html', {'board' :boards})

# 페이지를 생성하기 위한 함수입니다.
def new(request):
        return render(request,'new.html')
                  
def create(request, detail=None):
        if request.method =='POST':
                form = DetailForm(request.POST,instance=detail)
                if form.is_valid():
                        detail = form.save(commit=False)
                        detail.pub_date=timezone.now()
                        detail.save()
                        return redirect('home2')
        else:
                form = DetailForm(instance=detail)
                return render(request, 'new.html', {'form':form})       

def update(request, board_id):
        detail = Detail()
        detail.title = request.GET['title']
        detail.content = request.GET['content']
        detail.pub_date = timezone.datetime.now()
        detail.save()
        return redirect('/detail/')

def home2(request):
        details = Detail.objects
        return render(request, 'home2.html',{'details' :details})

def edit(request,pk):
    detail=get_object_or_404(Detail,pk=pk)
    return create(request,detail)

def remove(request,pk):
    detail=get_object_or_404(Detail,pk=pk)
    detail.delete()
    return redirect('home2')
        

