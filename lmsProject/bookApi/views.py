from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book
from .models import BookForm


# decorator from rest_framework with method passed in parameters
@api_view(["GET"])
# documentation for all endpoints and methods
def getRoutes(request):
    routes = [
        {
            "Endpoint": "/books/",
            "method": "GET",
            "body": None,
            "description": "Get all books(array)",
        },
        {
            "Endpoint": "/book/id",
            "method": "GET",
            "body": None,
            "description": " Get a single book(object)",
        },
        {
            "Endpoint": "/book/create",
            "method": "POST",
            "body": {"body": ""},
            "description": "Create a new book with data sent in post request",
        },
        {
            "Endpoint": "/book/id/update",
            "method": "PUT",
            "body": {"body": ""},
            "description": "Update an existing book with data sent in put request",
        },
        {
            "Endpoint": "/book/id/delete",
            "method": "DELETE",
            "body": None,
            "description": "Delete an existing book",
        },
    ]
    return Response(routes)


# get all available books
@api_view(["GET"])
def getAllBooks(request):
    # get all the books from the database
    books = Book.objects.all()

    # serializer the objects in order to pass them in the api
    # many= True to serialize all objects, otherize = false to serialize one object
    serializer = BookSerializer(books, many=True)

    # return within the response all the books(data) in JSON format
    return Response(serializer.data, status=200)


# add a new book
@api_view(["POST"])
def addBook(request):
    # get the request
    data = BookForm(request.data)

    # validation if the data passed from the request
    if data.is_valid():
        # if true, create a new instance of Book and save the data in the database
        book = data.save()

        serializer = BookSerializer(book)
        return Response(serializer.data, status=201)
    else:
        return Response(data.errors, status=400)
