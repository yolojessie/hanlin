from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect, get_object_or_404

from account.forms import UserForm
from account.models import User
from main.views import admin_required
from shop.forms import BranchForm, PlantForm
from order.forms import OrderForm
from shop.models import Branch, Plant



# Create your views here.
def shop(request):
    branches = {}
    for branch in Branch.objects.all():
        branches.update({branch:Plant.objects.filter(branch=branch)})
    context = {'branches':branches}
    
    return render(request, 'shop/shop.html',context)
@admin_required
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
@admin_required
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

@admin_required
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

@admin_required
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

@admin_required
def branchDelete(request, branchId):
    if request.method == 'GET':
        return shop(request)
    
    #POST
    branch = get_object_or_404(Branch, id=branchId)
    branch.delete()
    messages.success(request, '類別已刪除')
    return redirect('shop:shop')

@admin_required
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

@admin_required
def plantDiscount(request, plantId, branchId):
    branch = get_object_or_404(Branch, id=branchId)
    discount = int(request.GET.get('discount'))
    plant = get_object_or_404(Plant, id=plantId)
    
    if not discount:
        discountPrice = 0
    else:
        plant.discount = discount
        discountPrice = plant.price*discount/10
        plant.newPrice = discountPrice
        plant.save()
   
    
    context = {
        'plants':Plant.objects.filter(branch=branch),
        'plant':plant,
        'branch':branch,
    }

    return render(request, 'shop/plantRead.html', context)

@login_required
def plantBuy(request, plantId):
    template = 'shop/buyInfo.html'
    plant = get_object_or_404(Plant, id=plantId)
    context = {}
    if request.method == 'GET':
        context.update({'plant':plant,'orderForm':OrderForm(initial={'name':request.user.fullName, 
                                                                     'email':request.user.email, 
                                                                     'address':request.user.address, 
                                                                     'plantName':plant.plantName})})
        return render(request, template, context)

    # POST
    orderForm = OrderForm(request.POST)
    print(orderForm)
    if not orderForm.is_valid():
        return render(request, template, {'plant':plant,'orderForm':orderForm})
    if plant.newPrice:
        realPrice = plant.newPrice
    else:
        realPrice = plant.price
    order = orderForm.save(commit=False)
    order.plant = plant
    order.customer = request.user
    order.totalPrice = realPrice
    order.save()
    messages.success(request, '購買成功')
    if request.user not in plant.buyes.all():
        plant.buyes.add(request.user)
        plant.inventory = plant.inventory-1
        plant.save()
    return redirect('shop/shop.html')

   
#     else:
#         plant.buyes.remove(request.user)
#         plant.inventory = plant.inventory+1
#         plant.save()
    #TODO:完成OderForm的對應購買成工頁面以及查看訂單   
    

