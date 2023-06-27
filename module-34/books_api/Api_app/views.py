from django.shortcuts import render
from django.views import View
from django.http import JsonResponse , Http404,HttpResponseBadRequest
from .data import books
from .serializers import BooksSerializer, BookReviewsSerializer
import json
# from http import 


book_reviews =[]

class BooksApi(View):
    def get(self, request):
        serializedData= BooksSerializer(books,many=True).data
        return JsonResponse(serializedData,safe=False)
       

class BooksDetails(View):
    def get(self, request, book_id):
        book_found = None
        for book in books:
            if book['book_id']==book_id:
                book_found=book
                break
        if book_found:
            return JsonResponse(BooksSerializer(book_found).data,safe=False)
        else:
            raise Http404("Page not found")
        


class BookReview(View):
    def post(self, request, book_id):
        review_data=json.loads(request.body)
        review_data["book_id"]=book_id
        review_data["review_id"]=len(book_reviews)+1 

        review_serialized = BookReviewsSerializer(data=review_data )
        if (review_serialized.is_valid()):
            book_reviews.append(review_serialized.data)
            # review_data.append

            return JsonResponse(review_serialized.data, status=201)


        else:
            return HttpResponseBadRequest()



# Create your views here.
