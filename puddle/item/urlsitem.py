from django.urls import path

from . import views

app_name='item'

urlpatterns=[
    path('<int:pk>/',views.detail,name='detail'),
    #tambahan url untuk mengakses tambah item
    path('new/',views.new,name='new'),
    #untuk menghapus data
    path('<int:pk>/delete/',views.delete,name='delete'),
    #untuk mengedit data
    path('<int:pk>/edit/',views.edit,name='edit'),
    #untuk mencari data
    path('',views.items,name='items'),

]