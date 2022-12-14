"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Authors/', AuthorView.as_view(), name='Authors'),
    path('Authors/<int:Author_id>', AuthorView.as_view(), name='Authors'),
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<str:category_id>', CategoryView.as_view(), name='category'),
    path('partner/', PartnerView.as_view(), name='partner'),
    path('partner/int:<partner_id>', PartnerView.as_view(), name='partner'),
    path('book/', BookView.as_view(), name='book'),
    path('book/str:<book_id>', BookView.as_view(), name='book'),
    path('bookload/', BookLoadView.as_view(), name='bookload'),
    path('bookload/str:<bookload_id>', BookLoadView.as_view(), name='bookload'),
    path('orm/', AuthorViewWtihOrm.as_view(), name='orm_Author'),
    path('orm/', CategoryViewWtihOrm.as_view(), name='orm_Category'),
    path('orm/', PartnerViewWtihOrm.as_view(), name='orm_Partner'),
    path('orm/', BookViewWtihOrm.as_view(), name='orm_Book'),
    path('orm/', BookLoadViewWtihOrm.as_view(), name='orm_BookLoad'),
]
