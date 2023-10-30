from django.db import models

# Create your models here.
class tag(models.Model):
    caption = models.CharField(max_length=30)


class author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(_(""), max_length=254)

class post(models.Model):
    title = models.CharField(max_length=50)
    excerpt= models.CharField(max_length=80)
    image = models.ImageField()
    date = models.DateTimeField()
    slug = models.SlugField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(author)
    tag = models.ManyToManyField(tag)
