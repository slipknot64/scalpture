from django.urls import path
from . import views

app_name = 'gamestop'

urlpatterns = [
    path('execute_purchase/<str:email>/<str:first_name>/<str:last_name>/<str:state>/<str:city>/<str:product_url>/<str:street_address>/<str:zip_code>/<str:card_number>/<str:cvv>/<str:expiration_date>/<str:phone_number>/', views.execute_purchase_script, name='execute_purchase'),
    path('gamestop/purchase/', views.purchase_view, name='purchase'),
    path('gamestop/success/', views.success_view, name='success'),
    path('gamestop/error/', views.error_view, name='error'),
    path('gamestop/', views.gamestop_view, name='gamestop'),
]
