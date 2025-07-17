from django.db import models

# Create your models here.

class Member(models.Model):
	name = models.CharField(max_length=50)
	phone =models.CharField(max_length=20)
	email = models.EmailField()
	address = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)   


class Detail(models.Model):
	member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
	birth_date = models.CharField(max_length=50)
	gender = models.CharField(max_length=10, null=True, blank=True)
	memo = models.TextField(null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True)

