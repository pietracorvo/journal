# Blog post for example, we would need a 
#   title, slug, intro, body
# and maybe a time stamp.
#
# https://codewithstein.com/build-a-simple-blog-using-django-3-in-under-20-minutes/


from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'({self.pk}) {self.date_added} {self.title}'

    class Meta:
        ordering = ['-date_added']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)