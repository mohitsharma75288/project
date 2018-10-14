from django.urls import path
from . import views
urlpatterns=[
  
  path('', views.index, name='index'),
  path('display', views.display, name='display'),
  path('delete/<int:id>', views.deletefun, name='deletefun'),
  path('edit/<int:id>', views.editfunction, name='editfunction'),
  path('update/<int:id>', views.updatefunction, name='updatefunction'),
  ]