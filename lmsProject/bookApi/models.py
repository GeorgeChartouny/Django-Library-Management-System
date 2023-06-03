from django import forms
from django.db import models

#


# SQL database schema for Book
class Book(models.Model):
    # title column with max characters of 50
    title = models.CharField(max_length=50)

    # author column with max characters of 50
    author = models.CharField(max_length=50)

    # pub_year(publication year)
    pub_year = models.DateField()

    # category field with max characters of 50
    category = models.CharField(max_length=50)

    # additional_details is a non required column
    additional_details = models.JSONField(null=True, blank=True)

    # timestamp field gets modified whenever the entry is saved/updated
    # auto_now = True will do that automatically
    updated_at = models.DateTimeField(auto_now=True)

    # timestamp field to know when this record has been created
    # auto_now_add = True will automatically fill in the value on creation
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # default ordering system by attribute of updated. -updated will set is asc
    class Meta:
        ordering = ["-updated"]


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
