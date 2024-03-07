from django.db import models
from accounts.models import User

# Create your models here.
connection_choices = [('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')]

class Connection(models.Model):
    from_user = models.ForeignKey(User, related_name='connections_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='connections_received', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=connection_choices)

    def __str__(self):
        return self.from_user.username + " - "+ self.to_user.username + " - "+ self.status
    
    class Meta:
        unique_together = ('from_user', 'to_user')