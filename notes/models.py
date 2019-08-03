from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class Note(models.Model):
    user = models.ForeignKey(User, related_name='notes', on_delete='PROTECT')
    created_at = models.DateTimeField(auto_now=True)
    titulo = models.CharField(max_length=150, blank=False)
    texto = models.TextField(max_length=1000, blank=False)

    def get_absolute_url(self):
        return reverse('notes:single', kwargs={'username':self.user.username, 'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = []

    def __str__(self):
        return self.texto