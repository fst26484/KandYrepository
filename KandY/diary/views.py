from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import White,Question
from .forms import WhiteForm,QuestionForm,ViewForm

# トップページの作成
@login_required(login_url='/admin/login/')
def index(request):
    params = {
        'title':'日記',
        'message':'かずきとゆめみ',
    }
    return render(request, 'diary/index.html', params)

# 日記を書くページの作成
@login_required(login_url='/admin/login/')
def white(request):
    if (request.method == 'POST'):
        obj = White()
        white = WhiteForm(request.POST, instance=obj)
        if (white.is_valid):
            white.save()
        return redirect(to='/diary/view')
    params = {
        'title':'日記を書く',
        'message':'共有したいことを書いてね。',
        'form':WhiteForm(),
    }
    return render(request, 'diary/white.html', params)




# 日記を見るページの作成
@login_required(login_url='/admin/login/')
def view(request):
    if (request.method == 'POST'):
        form = ViewForm(request.POST)
        find = request.POST.get('find')
        data = White.objects.filter(content__contains=find)
    else:
        form = ViewForm()
    data = White.objects.all()
    params = {
        'title':'日記を見る',
        'message':'過去の日記を見ることができるお。',
        'form':form,
        'data':data,
    }
    return render(request, 'diary/view.html', params)
    
# 相手に質問するページを作成(DBに反映されることが確認できた。)
def question(request):
    params = {
        'title':'質問する',
        'message':'相手に直接聞けないことを聞いてみよう。',
        'form':QuestionForm()
    }
    if (request.method == 'POST'):
        obj = Question()
        question = QuestionForm(request.POST, instance=obj)
        question.save()
        return redirect(to='/diary')
    return render(request, 'diary/question.html', params)

    ###test
    ###testtest