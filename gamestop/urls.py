from django.urls import path
from . import views

app_name = 'gamestop'

urlpatterns = [
    path('gamestop/purchase/', views.purchase_view, name='purchase'),
    path('gamestop/success/', views.success_view, name='success'),
    path('gamestop/error/', views.error_view, name='error'),
    path('gamestop/', views.gamestop_view, name='gamestop'),
]
