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


# get a single book by id
@api_view(["GET"])
def getBookById(request, primaryKey):
    # retrieve from the db the object with the requested id
    book = Book.objects.get(id=primaryKey)

    # serialize the object to send them in the response of the api
    serializer = BookSerializer(book, many=False)

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


# update a book
@api_view(["PUT"])
def updateBook(request, primaryKey):
    # retrieve from the db the object with the requested id
    book = Book.objects.get(id=primaryKey)

    # get the requested data
    data = BookForm(request.data, instance=book)

    if data.is_valid():
            data.save()
            serializer = BookSerializer(book)
            return Response(serializer.data, status=201)
    else:
        return Response(data.errors, status=400)

    # if data.is_valid():
    #     # access the validated data
    #     validate_data = data.cleaned_data

    #     # update the book object with the field requested
    #     book.title = validate_data["title"]
    #     book.author = validate_data["author"]
    #     book.pub_year = validate_data["pub_year"]
    #     book.category = validate_data["category"]
    #     book.additional_details = validate_data["additional_details"]

    #     # save the new values in the db
    #     book.save()

    #     # serializer the object and return in response with the appropriate satus
    #     serializer = BookSerializer(book)
    #     return Response(serializer.data, status=200)

    # else:
    #     return Response(data.errors, status=400)
