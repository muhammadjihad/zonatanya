from django.contrib import admin
from .models import Penanya

# Register your models here.
class PostPenanya(admin.ModelAdmin):
	readonly_fields = ['slug']


admin.site.register(Penanya, PostPenanya)