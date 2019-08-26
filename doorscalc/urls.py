from django.urls import path
# from doorscalc.views import MyView
from . import views


urlpatterns = [
    path('', views.doors_list, name='doors_list'),

    path('calc/', views.ajax, name='ajax'),
    path('ord/', views.ajax_ord, name='ajax_ord'),
    path('delorder/', views.delete_order, name='delete_order'),

]