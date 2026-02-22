from django.db import models

class GroceryItem(models.Model):
    session_key = models.CharField(max_length=40, null=True, blank=True)  
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']