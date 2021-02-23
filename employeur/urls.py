from django.urls import path,include
from employeur import views

urlpatterns=[
    # path('', views.listEmployeur)
    path('', views.listEmployeur, name='employeurlist'),
    path('employeuradd', views.addEmployeur, name='employeuradd'),
    path('employeurdelete/<str:pk>/', views.deleteEmployeur, name='employeurdelete')


]
