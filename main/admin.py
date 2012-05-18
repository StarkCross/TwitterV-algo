from django.contrib import admin
from main.models import User, Tweet

class UserAdmin(admin.ModelAdmin):
    list_display = ('nick_name', 'first_name', 'last_name', 'email', 'birth_date', 'place', 'biography', 'place_birth',)
    search_field = ('first_name',)


class TweetAdmin(admin.ModelAdmin):
    list_display = ('owner', 'status', 'created_at',)


admin.site.register(User, UserAdmin)
admin.site.register(Tweet, TweetAdmin)
