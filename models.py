from django.db import models

# Create your models here.
class Author(models.Model):
    
    AuthorID = models.CharField(primary_key = True,max_length=10)
    Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=10)
    Country = models.CharField(max_length=20)

    def __unicode__(self):
        return self.AuthorID
    
class Book(models.Model):
    
    ISBN = models.CharField(primary_key = True,max_length=10)
    Title = models.CharField(max_length=100)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=100)
    Publishdate = models.DateField()
    Price = models.CharField(max_length=10)

    def __unicode__(self):
        return self.Title
