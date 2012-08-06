from emkaystudios.models import Announcement
from django.contrib import admin
from emkaystudios.settings import STATIC_URL

class AnnouncementAdmin(admin.ModelAdmin):
	fields = ['title', 'body']
	list_display = ('title', 'body', 'created_on')
	search_fields = ['title', 'body']

class CommonMedia:
	js = (
    	'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    	STATIC_URL + 'admin/js/editor.js',
  	)
  	css = {
    	'all': (STATIC_URL + 'admin/css/editor.css',),
	}

admin.site.register(Announcement, AnnouncementAdmin, Media = CommonMedia)