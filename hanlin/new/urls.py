from django.urls import path
from new import views


app_name = 'new'
urlpatterns = [
    path('', views.new, name='new'),
    path('articleCreate/', views.articleCreate, name='articleCreate'),
    path('articleRead/<int:articleId>', views.articleRead, name='articleRead'),
    path('articleUpdate/<int:articleId>', views.articleUpdate, name='articleUpdate'),
    path('articleDelete/<int:articleId>', views.articleDelete, name='articleDelete'),
]