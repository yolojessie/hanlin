from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls.base import reverse
from shop.models import Plant
from django.db.models.query_utils import Q
# Create your views here.



def main(request):
    plants = Plant.objects.filter(Q(hot__icontains=True))
    dicPlants = Plant.objects.filter(Q(discount__lte=5) & Q(discount__gt=0))
    context = {'plants':plants,'dicPlants':dicPlants}
    return render(request, 'main/main.html', context)

def contact(request):
    return render(request, 'main/contact.html')

def news(request):
    return render(request, 'main/news.html')

def admin_required(func):
    def auth(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, '請以管理者身份登入')
            return redirect(reverse('account:login') + '?next=' + request.get_full_path())
        return func(request, *args, **kwargs)
    return auth