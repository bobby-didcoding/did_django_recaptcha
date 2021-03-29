from django.contrib import admin

from .models import (
		Contact,
	)

class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'telephone')
admin.site.register(Contact,ContactAdmin)
