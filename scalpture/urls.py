from django.urls import path
from . import views

urlpatterns = [
    path('execute_purchase/<str:password>/<str:product_url>/', views.execute_purchase_script, name='execute_purchase'),
    path('purchase/', views.purchase_view, name='purchase'),
    path('success/', views.success_view, name='success'),
    path('error/', views.error_view, name='error'),
    path('', views.homepage_view, name='homepage'),
]
