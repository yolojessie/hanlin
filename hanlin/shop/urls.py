from django.urls import path
from shop import views


app_name = 'shop'
urlpatterns = [
    path('', views.shop, name='shop'),
    path('branchCreate/', views.branchCreate, name='branchCreate'),
    path('branchRead/<int:branchId>', views.branchRead, name='branchRead'),
    path('plantRead/<int:branchId>/<int:plantId>', views.plantRead, name='plantRead'),
]