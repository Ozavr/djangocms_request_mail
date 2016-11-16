from django.contrib import admin
from request_mail.models import RequestList

class RequestlistAdmin( admin.ModelAdmin ):
	'''
	Class for display the list of request in the admin panel
	'''
	list_display = ( 'date', 'name', 'phone', 'description', )
	search_fields = ( 'name', 'phone' )
	

admin.site.register( RequestList, RequestlistAdmin )

# Register your models here.
