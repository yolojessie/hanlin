from django.shortcuts import render, redirect, get_object_or_404
from new.models import New
from new.forms import NewForm
from django.contrib import messages
from main.views import admin_required
# Create your views here.

def new(request):
    articles = New.objects.all()
    context = {'articles':articles}
    return render(request, 'new/new.html', context)

@admin_required
def articleCreate(request):
    template = 'new/articleCreateUpdate.html'
    if request.method == 'GET':
        return render(request, template, {'newForm':NewForm()})
    
    # POST
    newForm = NewForm(request.POST)
    if not newForm.is_valid():
        return render(request, template, {'newForm':newForm})
    newForm.save()
    messages.success(request, '文章已新增')
    return redirect('new:new')

def articleRead(request, articleId):
    article = get_object_or_404(New, id=articleId)
    context = {
        'article': article,
    }
    return render(request, 'new/articleRead.html', context)

@admin_required
def articleUpdate(request, articleId):
    article = get_object_or_404(New, id=articleId)
    template = 'new/articleCreateUpdate.html'
    if request.method == 'GET':
        newForm = NewForm(instance=article)
        return render(request, template, {'newForm':newForm})
    
    #POST
    newForm = NewForm(request.POST, instance=article)
    if not newForm.is_valid():
        return render(request, template, {"newForm":newForm})
    newForm.save()
    messages.success(request, '公告已修改')
    return redirect('new:articleRead', articleId=articleId)

@admin_required
def articleDelete(request, articleId):
    if request.method == 'GET':
        return new(request)
    #POST
    article = get_object_or_404(New, id=articleId)
    article.delete()
    messages.success(request, '公告已刪除')
    return redirect('new:new')


