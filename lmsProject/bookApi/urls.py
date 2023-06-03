from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes),
    path("books/", views.getAllBooks),
    path("book/create", views.addBook),
    path("book/<int:primaryKey>", views.getBookById),
    path("book/<int:primaryKey>/update", views.updateBook),
    path("book/<int:primaryKey>/delete", views.deleteBook),
]
