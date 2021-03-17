from django.urls import path
from accounts import views
urlpatterns = [
    # path('', views.home),
    path('register', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

]
