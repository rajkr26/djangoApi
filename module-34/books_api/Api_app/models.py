from django.db import models

class Book(models.Model):
    book_id=models.IntegerField()
    title=models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    publishDate= models.DateTimeField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    image=models.CharField(max_length=100)



class BookReview(models.Model):
    review_id=models.IntegerField()
    book_id=models.IntegerField()
    user_id=models.IntegerField()
    comment=models.CharField(max_length=1000)
    rating=models.DecimalField(max_digits=2, decimal_places=2)


# Create your models here.
