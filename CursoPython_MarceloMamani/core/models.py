from django.db import models

# Create your models here.
# author, book, bookload, category, partner
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    nationality = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=200)
    recommended_age = models.IntegerField(blank=False, null=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

class Book(models.Model):
    name = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

class Partner(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    dni = models.IntegerField(blank=False, null=False)
    Book = models.ManyToManyField(Book, through='BookLoad')
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


class BookLoad(models.Model):
    status = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)