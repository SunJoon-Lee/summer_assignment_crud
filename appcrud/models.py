from django.db import models

# Create your models here.
class Appcrud(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    post = models.ForeignKey('appcrud.Comment', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
