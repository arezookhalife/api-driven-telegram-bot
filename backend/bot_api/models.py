from django.db import models

class MessageHistory(models.Model):
    user_id = models.CharField(max_length=50)
    username = models.CharField(max_length=150, blank=True, null=True)
    user_message = models.TextField()
    bot_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username or self.user_id} - {self.created_at}"