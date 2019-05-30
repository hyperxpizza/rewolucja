from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:all_products',args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        ordering=('name',)
        index_together = (('id','slug'))

    def get_absolute_url(self):
        return reverse('store:product_detail',args=[self.id,self.slug])

    def sold_out_image(self):
        photo = Image.open(self.image)
        watermark = Image.open('../static/img/watermark.png')
        photo.paste(watermark, (25,25), watermark)
        return photo

    def __str__(self):
        return self.name

#class Images(models.Model):
#   user = models.ForeignKey(User)
#   title = models.CharField(max_length=100)
#     body = models.CharField(max_length=150)

#    def get_image_filename(instance, filename):
#        id = instance.Product.id
#        return 
