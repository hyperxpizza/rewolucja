from django.db import models
from time import timezone
from django.urls import reverse 
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    #text = RichTextField(blank=True, null=True)
    #text = RichTextUploadingField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=('title',)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])
   
    def __str__(self):
        return self.title