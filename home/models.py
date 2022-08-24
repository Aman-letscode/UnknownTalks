from django.db import models

# Create your models here.
class Contact(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=13)
    content = models.TextField()
    timestamp= models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return "Query from "+self.name
    