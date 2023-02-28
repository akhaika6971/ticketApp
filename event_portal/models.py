from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
import uuid
# Create your models here.


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    slug = models.SlugField(db_index=True, editable=False)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    
class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250)
    event_date = models.DateField()
    event_time = models.TimeField(null=True)
    location = models.CharField(max_length=300)
    address = models.CharField(max_length=100, null=True)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(db_index=True, editable=False)
    tags = models.ManyToManyField(Category)
    about = models.TextField(null=True)
    expired = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    

class Ticket(models.Model):
    ticket_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket_type = models.CharField(max_length=25)
    ticket_price = models.FloatField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ticket_id
    
    
class SocialMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedIn = models.URLField(null=True, blank=True)
    event = models.ForeignKey(Event, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.event.title}"
        
