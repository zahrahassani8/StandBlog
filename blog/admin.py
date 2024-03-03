from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Post)
admin.site.register(Message)
admin.site.register(Tip)