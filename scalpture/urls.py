from django.urls import include, path
from . import views

app_name = 'scalpture'

urlpatterns = [
    path('execute_purchase/<str:email_address>/<str:firstName>/<str:lastName>/<str:title>/<str:product_url>/<str:address>/<str:postcode>/<str:fullName>/<str:cardNumber>/<str:cvv>/<str:expiration>/<str:mobileNumber>/', views.execute_purchase_script, name='execute_purchase'),
    path('purchase/', views.purchase_view, name='purchase'),
    path('success/', views.success_view, name='success'),
    path('error/', views.error_view, name='error'),
    path('game/', views.game_view, name='game'),
    path('signin/', views.signin_view, name='signin'),
    path('script-services/', views.script_services, name='script-service'),
    path('', views.homepage_view, name='homepage'),
    path('', include('gamestop.urls')),
]
