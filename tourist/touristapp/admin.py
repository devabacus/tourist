from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Channel, Location, Category, Tag, Flag, Message

# Register your models here.
admin.site.register(User)
admin.site.register(Channel)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Flag)
admin.site.register(Message)