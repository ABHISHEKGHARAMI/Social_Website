from django.db import models

# Create your models here.
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse


# creating the model
class Image(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='images_created',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/',max_length = 500)
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='images_liked',
                                       blank=True)
    
    
    #  meta class
    class Meta:
        indexes = [
            models.Index(fields=['-created'])
        ]
        ordering = ['created']
    
    def __str__(self):
        return self.title
    
    
    def save(self,*args,**kargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kargs)
        
        
    # get absolute url
    def get_absolute_url(self):
        return reverse('images:detail',args=[self.id,self.slug])


    