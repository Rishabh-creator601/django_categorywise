from django.db import models

# Create your models here.



class product(models.Model):
	product_id = models.AutoField
	product_name = models.CharField(max_length=20,default="")
	category = models.CharField(max_length=20,default="")
	product_price = models.IntegerField()
	desc = models.CharField(max_length=200,default="")
#	image = models.ImageField(upload_to='sample/images',default="")
	
	def __str__(self):
		return self.product_name 
		
	
	
	
	