from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from shop.models import Branch, Plant
from shop.forms import BranchForm


# Create your views here.

def shop(request):
    branches = {}
    for branch in Branch.objects.all():
        branches.update({branch:Plant.objects.filter(branch=branch)})
    context = {'branches':branches}
    
    return render(request, 'shop/shop.html',context)

def branchCreate(request):
    template = 'shop/branchCreate.html'
    if request.method == 'GET':
        return render(request, template, {'branchForm':BranchForm()})
    
    #POST
    branchForm = BranchForm(request.POST)
    if not branchForm.is_valid():
        return render(request, template,{'branchForm':branchForm})
    branchForm.save()
    messages.success(request, '類別已新增')
    return redirect('shop:shop')

def branchRead(request, branchId):
    branch = get_object_or_404(Branch, id=branchId)
    context = {
        'branch':branch,
        'plants':Plant.objects.filter(branch=branch)
    }
    return render(request, 'shop/branchRead.html', context)

def plantRead(request, plantId, branchId):
    branch = get_object_or_404(Branch, id=branchId)
    plant = get_object_or_404(Plant, id=plantId)
    context = {
        'plants':Plant.objects.filter(branch=branch),
        'plant':plant,
        'branch':branch
    }
    return render(request, 'shop/plantRead.html', context)

