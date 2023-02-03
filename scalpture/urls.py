from django.urls import include, path
from . import views

app_name = 'scalpture'

urlpatterns = [
    path('execute_purchase/<str:email>/<str:password>/<str:product_url>/<str:cvv>/', views.execute_purchase_script, name='execute_purchase'),
    path('purchase/', views.purchase_view, name='purchase'),
    path('success/', views.success_view, name='success'),
    path('error/', views.error_view, name='error'),
    path('', views.homepage_view, name='homepage'),
    path('', include('gamestop.urls')),
]
