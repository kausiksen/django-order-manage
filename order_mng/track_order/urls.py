from django.urls import path
from . import views
urlpatterns = [
    path("", views.order_index, name="order_index"),
    path("<int:pk>/", views.order_detail, name="order_detail"),
    path("make_fav/<int:pk>/", views.make_fav, name="make_fav"),
]
