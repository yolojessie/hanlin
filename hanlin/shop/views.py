from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from shop.models import Branch, Plant
from shop.forms import BranchForm,PlantForm
from django.db.models.query_utils import Q


# Create your views here.

def shop(request):
    branches = {}
    for branch in Branch.objects.all():
        branches.update({branch:Plant.objects.filter(branch=branch)})
    context = {'branches':branches}
    
    return render(request, 'shop/shop.html',context)

def branchCreate(request):
    template = 'shop/branchCreateUpdate.html'
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

def plantCreate(request, branchId):
    template = 'shop/plantCreateUpdate.html'
    branch = get_object_or_404(Branch, id=branchId)
    if request.method == 'GET':
        return render(request, template, {'plantForm':PlantForm(),'branch':branch})
    
    #POST
    plantForm = PlantForm(request.POST)
    if not plantForm.is_valid():
        return render(request, template, {'plantForm':plantForm})
    plant = plantForm.save(commit=False)
    plant.branch = branch
    plant.save()
    messages.success(request, '商品已新增')
    return redirect('shop:shop')

def branchUpdate(request, branchId):
    branch = get_object_or_404(Branch, id=branchId )
    template = 'shop/branchCreateUpdate.html'
    if request.method == 'GET':
        branchForm = BranchForm(instance=branch)
        return render(request, template, {'branchForm':branchForm})
    
    #POST
    branchForm = BranchForm(request.POST, instance=branch)
    if not branchForm.is_valid():
        return render(request, template, {'branchForm':branchForm})
    branchForm.save()
    messages.success(request, '類別名修改成功')
    return redirect('shop:branchRead', branchId=branchId)

def plantUpdate(request, branchId, plantId):
    branch = get_object_or_404(Branch, id=branchId)
    plant = get_object_or_404(Plant, id=plantId)
    context = {'branch':branch, 'plant':plant}
    template = 'shop/plantCreateUpdate.html'
    if request.method == 'GET':
        context.update({'plantForm':PlantForm(instance=plant)})
        return render(request, template, context)
    
    #POST
    plantForm = PlantForm(request.POST, instance=plant)
    if not plantForm.is_valid():
        return render(request, template, {'plantForm':plantForm})
    plantForm.save()
    messages.success(request, '商品已修改')
    return redirect('shop:plantRead', branchId=branchId, plantId=plantId)


def branchDelete(request, branchId):
    if request.method == 'GET':
        return shop(request)
    
    #POST
    branch = get_object_or_404(Branch, id=branchId)
    branch.delete()
    messages.success(request, '類別已刪除')
    return redirect('shop:shop')

def plantDelete(request, plantId):
    if request.method == 'GET':
        return shop(request)
    
    #POST
    plant = get_object_or_404(Branch, id=plantId)
    plant.delete()
    messages.success(request, '類別已刪除')
    return redirect('shop:shop')

def plantSearch(request):
    searchTerm = request.GET.get('searchTerm')
    plants = Plant.objects.filter(Q(plantName__icontains=searchTerm) | Q(code__icontains=searchTerm))
    context = {'plants':plants, 'searchTerm':searchTerm}
    return render(request, 'shop/plantSearch.html', context)
