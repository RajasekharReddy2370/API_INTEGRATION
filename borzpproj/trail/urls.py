from django.urls import path
from .views import place_order_t,place_order_p,price,Edit_order_p,CreateOrderBlowhorn

urlpatterns = [
    path("place_order_t/",place_order_t.as_view(),name = "place_order"),
    path("place_order_p/",place_order_p.as_view(),name = "place_order"),
    path("price/",price.as_view(),name = "price_estimation"),
    path("edit_order_p/",Edit_order_p.as_view(),name = "edit_order"),
    path("cobh/",CreateOrderBlowhorn.as_view(),name = "place_blowhorn_order"),

]
