from django.db import models
from accounts.models import CustomUser

class Connection(models.Model):
    user1 = models.ForeignKey(CustomUser, related_name='connections_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(CustomUser, related_name='connections_user2', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user1} & {self.user2}'

class Message(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender} to {self.receiver}'

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.user}'
