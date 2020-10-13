from django.db import models

class Post(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_added=True)

    class Meta:
        ordering = ['created']

    def __unicode__(self):
        return self.text+' - '+self.author.username
