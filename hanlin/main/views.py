from django.shortcuts import render
from shop.models import Plant
from django.db.models.query_utils import Q
# Create your views here.



def main(request):
    plants = Plant.objects.filter(Q(hot__icontains=True))
    context = {'plants':plants}
    return render(request, 'main/main.html', context)

def contact(request):
    return render(request, 'main/contact.html')