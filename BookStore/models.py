from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    comment = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='', null=True)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,
                             related_name='post_comment')
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)