from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class Mem(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    user = models.ForeignKey(User, 
            related_name='mems_created',
            on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, blank=True,  unique_for_date='publish' )
    url = models.URLField()
    mem = models.ImageField(upload_to='mems/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, 
                db_index=True)
    publish = models.DateTimeField(default=timezone.now)
    users_like = models.ManyToManyField(User, 
                    related_name='mems_liked', 
                    blank=True)
    status = models.CharField(max_length=10,
                    choices=STATUS_CHOICES, 
                    default='draft')
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Mem, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('post_detail',
                        args=[self.publish.year,
                            self.publish.strftime('%m'),
                            self.publish.strftime('%d'),
                            self.slug])

class Meta:
    ordering = ('-publish',)