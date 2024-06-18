from django.db import models

# Create your models here.
class Comment(models.Model):
	postId=models.PositiveIntegerField(blank=True)
	name=models.CharField(max_length=100,blank=True)
	email=models.EmailField(blank=True)
	body=models.CharField(max_length=100,blank=True)
	

	def __str__(self):
		return self.name