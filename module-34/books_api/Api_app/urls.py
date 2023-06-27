


from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns=[
    path('books/',BooksApi.as_view(),name='Books-api'),
    path('books/<int:book_id>/',BooksDetails.as_view(), name='Books-details'),
    path('books/<int:book_id>/reviews',csrf_exempt(BookReview.as_view()), name='Books-reviews')
]