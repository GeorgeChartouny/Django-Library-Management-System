from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes),
    path("books/", views.getAllBooks),
    path("book/create", views.addBook),
    path("book/<str:primaryKey>", views.getBookById),
]
