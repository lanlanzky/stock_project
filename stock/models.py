from django.db import models

# Create your models here.
class New_stock(models.Model):
        name = models.CharField(max_length=30)
        date= models.DateField()
        open= models.CharField(max_length=30)
        high= models.CharField(max_length=30)
        low= models.CharField(max_length=30)
        close= models.CharField(max_length=30)
        volume= models.CharField(max_length=50)
        adjclose= models.CharField(max_length=50)
class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField(blank=True )
