from django.db import models
from django.core.validators import RegexValidator

class Data(models.Model):

    phone_checker=RegexValidator(r'^[7,8,9]{1}[0-9]{9}$','The given phone number does not exist in India')

    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
    )

    fname=models.CharField(max_length=31)
    lname=models.CharField(max_length=31)
    email=models.EmailField(max_length=31, unique=True)
    phone=models.IntegerField(unique=True, validators=[phone_checker])
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    bank_account_number=models.IntegerField()
    password=models.CharField(max_length=31)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Shortcomings(models.Model):


    priority_checker=RegexValidator(r'^[1,2,3,4,5]$','Rating must be between 1-5')
    priority = models.IntegerField(validators=[priority_checker])
    comment = models.CharField(max_length=127)
    review_holder = models.ForeignKey(Data, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Products(models.Model):


    name = models.CharField(max_length=31)
    price=models.IntegerField()
    stock=models.IntegerField()
    manufacturig_time=models.IntegerField()
    delivery_time=models.IntegerField()
    description=models.CharField(max_length=1023)
    score=models.IntegerField()
    retailer= models.ForeignKey(Data, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Same_day(models.Model):
    product=models.ForeignKey(Products, on_delete=models.CASCADE)

class Packages(models.Model):
    combo_price=models.IntegerField()

class Packages_pack(models.Model):
    product=models.ForeignKey(Packages, on_delete=models.CASCADE)
    product=models.ForeignKey(Products, on_delete=models.CASCADE)

class Occasion(models.Model):
    submenu = models.CharField(max_length=15)

class Men(models.Model):
    submenu = models.CharField(max_length=15)

class Women(models.Model):
    submenu = models.CharField(max_length=15)

class Men_product(models.Model):
    submenu=models.ForeignKey(Men, on_delete=models.CASCADE)
    product=models.ForeignKey(Products, on_delete=models.CASCADE)

class Women_product(models.Model):
    submenu=models.ForeignKey(Women, on_delete=models.CASCADE)
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
