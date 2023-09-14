from django.db import models

class UDB(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Contact=models.IntegerField()
    Password=models.CharField(max_length=100)
    def __str__(self):
        return self.Firstname
    
class ADB(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Contact=models.IntegerField()
    Password=models.CharField(max_length=100)
    def __str__(self):
        return self.Firstname
    
class EDB(models.Model):
    Stuname=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Enquiry=models.TextField()
    Contact=models.IntegerField()
    def __str__(self):
        self.Stuname