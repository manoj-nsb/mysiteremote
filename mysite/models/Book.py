from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        """String to represent the model object"""
        return self.title