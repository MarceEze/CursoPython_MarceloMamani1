from datetime import datetime
from django.core.serializers import serialize
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.status import *
import json
from core.models import *

# Create your views here.
class AuthorView(APIView):
    def get(self, request, author_id=None):
        if author_id:
            if Author.objects.filter(pk=author_id).exists():
                author_response = Author.objects.filter(pk=author_id) #Queryset
            else:
                return HttpResponse(content_type='application/json',
                           content=json.dumps({'detail': 'Author not fount'}),
                            status=HTTP_404_NOT_FOUND)
        else:
            author_response = list(Author.objects.all())
        author_response = serialize('json', author_response)
        return HttpResponse(content_type='application/json',
                           content=author_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        author, created = Author.objects.get_or_create(**body)      # dupla de (Author, created)
        if created:
            author.save()
            return HttpResponse(content_type='application/json',
                           content=json.dumps({'detail': 'Author created successfully',
                                               'data': body}),
                            status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                           content=json.dumps({'detail': 'Author already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request,author_id):
        author = Author.objects.filter(pk=author_id)
        if not author.exists():
            return HttpResponse(content_type='application/json',
                           content=json.dumps({'detail': 'Author not found'}),
                            status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        author.update(**body)
        return HttpResponse(content_type='application/json',
                           content=json.dumps({'detail': 'Auhtor updated successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, author_id):
        author = Author.objects.filter(pk=author_id)
        if not author.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author not found'}),
                                status=HTTP_404_NOT_FOUND)
        author.delete()
        return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author deleted successfully'}),
                                status=HTTP_200_OK)

class AuthorViewWtihOrm(APIView):
    def get(self, request):
        queryset_icontains_field = list(Author.Objects.filter(name__icotains=all()))

        queryset_iexact_field = list(Author.Objects.filter(name__icontains=all()).values("last_name"))
        response = {
            'icontains_field': queryset_icontains_field,
            'iexact_field': queryset_iexact_field,
        }
        return HttpResponse(content_type='application/json',
                            content=serialize('json', response),
                            status=HTTP_200_OK)

class CategoryView(APIView):
    def get(self, request, category_id=None):
        if category_id:
            if Category.objects.filter(pk=category_id).exists():
                category_response = Category.objects.filter(pk=category_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'category not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            category_response =list(Category.objects.all())
        category_response = serialize('json', category_response)
        return HttpResponse(content_type='application/json',
                            content=category_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        category, created = Category.objects.get_or_create(**body)      # dupla de (Author, created)
        if created:
            category.save()
            return HttpResponse(content_type='application/json',
                           content=json.dumps({'detail': 'Category created successfully',
                                               'data': body}),
                            status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                           content=json.dumps({'detail': 'Category already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, category_id):
        category = Category.objects.filter(pk=category_id)
        if not category.exists():
            return HttpResponse(content_type='application/json',
                           content=json.dumps({'detail': 'Category not found'}),
                            status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        category.update(**body)
        return HttpResponse(content_type='application/json',
                           content=json.dumps({'detail': 'category updated successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, category_id):
        category = Category.objects.filter(pk=category_id)
        if not category.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category not found'}),
                                status=HTTP_404_NOT_FOUND)
        category.delete()
        return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category deleted successfully'}),
                                status=HTTP_200_OK)

class CategoryViewWtihOrm(APIView):
    def get(self, request):
        queryset_icontains_field = list(Category.Objects.filter(name__icotains=all()))

        queryset_iexact_field = list(Category.Objects.filter(name__icontains=all()).values("first_name"))
        response = {
            'icontains_field': queryset_icontains_field,
            'iexact_field': queryset_iexact_field,
        }
        return HttpResponse(content_type='application/json',
                            content=serialize('json', response),
                            status=HTTP_200_OK)

class PartnerView(APIView):
    def get(self, request, partner_id=None):
        if partner_id:
            if Partner.objects.filter(pk=partner_id).exists():
                partner_response = Partner.objects.filter(pk=partner_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Partner not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            partner_id = list(Partner.objects.all())
        partner_response = serialize('json', partner_response)
        return HttpResponse(content_type='application/json',
                            content=partner_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        partner, created = Partner.objects.get_or_create(**body)      # dupla de (Author, created)
        if created:
            partner.save()
            return HttpResponse(content_type='application/json',
                           content=json.dumps({'detail': 'Partner created successfully',
                                               'data': body}),
                            status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                           content=json.dumps({'detail': 'Partner already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, partner_id):
        partner = Partner.objects.filter(pk=partner_id)
        if not partner.exists():
            return HttpResponse(content_type='application/json',
                           content=json.dumps({'detail': 'Partner not found'}),
                            status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        partner.update(**body)
        return HttpResponse(content_type='application/json',
                           content=json.dumps({'detail': 'Partner updated successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, partner_id):
        partner = Partner.objects.filter(pk=partner_id)
        if not partner.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner not found'}),
                                status=HTTP_404_NOT_FOUND)
        partner.delete()
        return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner deleted successfully'}),
                                status=HTTP_200_OK)

class PartnerViewWtihOrm(APIView):
    def get(self, request):
        queryset_icontains_field = list(Partner.Objects.filter(name__icotains=all()))

        queryset_iexact_field = list(Partner.Objects.filter(dni__contains='').values("firdt_name"))
        response = {
            'icontains_field': queryset_icontains_field,
            'iexact_field': queryset_iexact_field,
        }
        return HttpResponse(content_type='application/json',
                            content=serialize('json', response),
                            status=HTTP_200_OK)

class BookView(APIView):
    def get(self, request, book_id=None):
        if book_id:
            if Book.objects.filter(pk=book_id).exists():
                book_response = Book.objects.filter(pk=book_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Book not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            book_id = list(Book.objets.all())
        book_response = serialize('json', book_response)
        return HttpResponse(content_type='application/json',
                            content=book_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        body['author'] = Author.objects.get(pk=body['author'])
        body['category'] = Category.objects.get(pk=body['category'])
        book, created = Book.objects.get_or_create(**body)
        if created:
            book.save()
            return HttpResponse(content_type='application/json',
                           content=json.dumps({'detail': 'Book created successfully',
                                               'data': body}),
                            status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                           content=json.dumps({'detail': 'Book already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, book_id):
        book = Book.objects.filter(pk=book_id)
        if not book.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        book.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book update successfully'}),
                            status=HTTP_200_OK)

    def delete(self,request, book_id):
        book = Book.objects.filter(pk=book_id)
        if not book.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book not found'}),
                                status=HTTP_404_NOT_FOUND)
        book.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book delete successfully'}),
                            status=HTTP_200_OK)

class BookViewWtihOrm(APIView):
    def get(self, request):
        queryset_icontains_field = list(Book.Objects.filter(name__icotains=all()).valued('name'))

        queryset_iexact_field = list(Book.Objects.filter(Author__icontains=all()).values("name"))
        response = {
            'icontains_field': queryset_icontains_field,
            'iexact_field': queryset_iexact_field,
        }
        return HttpResponse(content_type='application/json',
                            content=serialize('json', response),
                            status=HTTP_200_OK)

class BookLoadView(APIView):
    def get(self, request, bookload_id=None):
        if bookload_id:
            if BookLoad.objects.filter(pk=bookload_id).exists():
                bookload_response = Book.objects.filter(pk=bookload_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'BookLoad not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            bookload_id = list(BookLoad.objects.all())
        bookload_response = serialize('json', bookload_response)
        return HttpResponse(content_type='application/json',
                            content=bookload_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        body['Partner'] = Partner.objects.get(pk=body['Partner'])
        body['Book'] = Book.objects.get(pk=body['Book'])
        bookload, created = BookLoad.objects.get_or_create(**body)
        if created:
            bookload.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'BookLoad created successfully',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'BookLoad already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, bookload_id):
        bookload = BookLoad.objects.filter(pk=bookload_id)
        if not bookload.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'BookLoad not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        bookload.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'BookLoad update successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, bookload_id):
        bookload = BookLoad.objects.filter(pk=bookload_id)
        if not bookload.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'BookLoad not found'}),
                                status=HTTP_404_NOT_FOUND)
        bookload.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'BookLoad delete successfully'}),
                            status=HTTP_200_OK)

class BookLoadViewWtihOrm(APIView):
    def get(self, request):
        queryset_icontains_field = list(BookLoad.Objects.filter(name__icotains=all()).valued('Partner__first_name'))

        queryset_iexact_field = list(BookLoad.Objects.filter(status__icontains=all()).values("Partner__dni"))
        response = {
            'icontains_field': queryset_icontains_field,
            'iexact_field' : queryset_iexact_field,
        }
        return HttpResponse(content_type='application/json',
                            content=serialize('json', response),
                            status=HTTP_200_OK)