from django.urls import path

from . import views

app_name = 'embeds'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:embed_id>/', views.detail, name='detail'),
    path('<int:embed_id>/', views.add, name='add'),
    path('list', views.list, name='list'),
    path('signup', views.signup, name='signup'),
]