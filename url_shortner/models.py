from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from utils.helper_methods import create_shorted_url


class URLShortner(models.Model):
    long_url = models.URLField(verbose_name='Original URL')
    short_url = models.CharField(verbose_name='Short URL', max_length=15, unique=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Created On', auto_now_add=True)
    hit_count = models.PositiveIntegerField(verbose_name='How many times hit', default=0)
    password = models.CharField(verbose_name='Password', max_length=200)

    def __str__(self):
        return f'{self.long_url} --> {self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_shorted_url(self)
        super().save(*args, **kwargs)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
