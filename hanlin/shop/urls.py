from django.urls import path
from shop import views


app_name = 'shop'
urlpatterns = [
    path('', views.shop, name='shop'),
    path('branchCreate/', views.branchCreate, name='branchCreate'),
    path('branchRead/<int:branchId>', views.branchRead, name='branchRead'),
    path('plantRead/<int:branchId>/<int:plantId>', views.plantRead, name='plantRead'),
    path('plantCreate/<int:branchId>', views.plantCreate, name='plantCreate'),
    path('branchUpdate/<int:branchId>', views.branchUpdate, name='branchUpdate'),
    path('plantUpdate/<int:branchId>/<int:plantId>', views.plantUpdate, name='plantUpdate'),
    path('branchDelete/<int:branchId>', views.branchDelete, name='branchDelete'),
    path('plantDelete/<int:plantId>', views.plantDelete, name='plantDelete'),
    path('plantSearch/', views.plantSearch, name='plantSearch'),
    path('plantDiscount/<int:branchId>/<int:plantId>', views.plantDiscount, name='plantDiscount'),
    path('plantBuy/<int:branchId>/<int:plantId>', views.plantBuy, name='plantBuy'),
]