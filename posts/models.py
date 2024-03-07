from django.db import models
from accounts.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.CharField(max_length = 400)

    def __str__(self):
        return self.user.username + " - "+ str(self.id)
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')
    
    def __str__(self):
        return self.user.username + " likes "+ self.post.user.username + " - "+ str(self.post.id)