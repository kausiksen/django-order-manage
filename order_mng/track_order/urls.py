from django.urls import path
from . import views
urlpatterns = [
    path("", views.order_index, name="order_index"),
    path("favs/", views.order_fav, name="order_fav"),
    path("<int:pk>/", views.order_detail, name="order_detail"),
    path("search/<str:q>", views.order_index, name="order_search"),
    path("make_fav/<int:pk>/", views.make_fav, name="make_fav"),
]
