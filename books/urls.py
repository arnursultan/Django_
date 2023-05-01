from django.urls import path
from books import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("category/<str:name>", views.category_detail, name="category-detail"),
]