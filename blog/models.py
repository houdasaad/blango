from django.db import models
from django.conf import settings
<<<<<<< HEAD
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# other imports ommited




# Create your models here.

=======

# Create your models here.
>>>>>>> 2813ec5e2876bcf7914d967a2f36a82e68ea41e2
class Tag(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value

<<<<<<< HEAD

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)



=======
>>>>>>> 2813ec5e2876bcf7914d967a2f36a82e68ea41e2
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts")
<<<<<<< HEAD
    comments = GenericRelation(Comment)

    
    def __str__(self):
        return self.title
=======

    def __str__(self):
        return self.title
>>>>>>> 2813ec5e2876bcf7914d967a2f36a82e68ea41e2
