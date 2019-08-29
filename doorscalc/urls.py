from django.urls import path
# from doorscalc.views import MyView
from . import views


urlpatterns = [
    path('', views.doors_list, name='doors_list'),

    path('calc/', views.ajax, name='ajax'),
    path('c/', views.ajax_calc, name='ajax_calc'),
    path('ord/', views.ajax_ord, name='ajax_ord'),
    path('ord2/', views.ajax_ord2, name='ajax_ord2'),
    path('delorder/', views.delete_order, name='delete_order'),

]