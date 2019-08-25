from django.contrib import admin
from .models import Games


class GamesAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'score', 'genre', 'editors_choice')


admin.site.register(Games, GamesAdmin)
# Register your models here.
