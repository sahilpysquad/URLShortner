from django.contrib import admin

from url_shortner.models import URLShortner


@admin.register(URLShortner)
class URLShortnerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_url')
