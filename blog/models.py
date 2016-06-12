from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    context = models.TextField()
    timestamp = models.DateTimeField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
