


from rest_framework import serializers
from .models import Book,BookReview


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        # feilds='__all__'
        fields=('book_id','title','price') 



class BookReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model= BookReview
        fields='__all__'
        # fields=('book_id','title','price')  