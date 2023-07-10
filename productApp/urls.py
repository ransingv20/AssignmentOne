from django.contrib import admin
from django.urls import path
from .views import Index, addCategory
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('addcategory', addCategory, name='addCategory')

]