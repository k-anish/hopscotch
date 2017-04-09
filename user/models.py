from django.db import models
from django.core.validators import RegexValidator
from retailer.models import Products

class Info(models.Model):

    phone_checker=RegexValidator(r'^[7,8,9]{1}[0-9]{9}$','The given phone number does not exist in India')

    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
    )

    fname=models.CharField(max_length=31)
    lname=models.CharField(max_length=31)
    email=models.EmailField(max_length=31, unique=True)
    phone=models.IntegerField( unique=True, validators=[phone_checker])
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    password=models.CharField(max_length=31)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Review(models.Model):
    ## Changes needed after creating product table
    REVIEW_CHOICES = (
    ('W', 'Website'),
    ('R', 'Retailer'),
    ('P', 'Product'),
    )

    rating_checker=RegexValidator(r'^[1,2,3,4,5]$','Rating must be between 1-5')
    comment=models.CharField(max_length=4095)
    rating = models.IntegerField(validators=[rating_checker])
    review_holder = models.CharField(max_length=1, choices=REVIEW_CHOICES, default='W')
    user = models.ForeignKey(Info, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):

    user = models.ForeignKey(Info, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
