from rest_framework.serializers import ModelSerializer

# serializer is used to converts the data type into JSON format

from .models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
