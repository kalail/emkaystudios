from blog.models import Post
from django.contrib import admin
from emkaystudios.settings import STATIC_URL

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['title', 'user']}),
	(None, {'fields': ['body']}),

	]

	list_display = ('title', 'user', 'created_on')
	search_fields = ['title', 'user', 'body']
	list_filter = ['user']

class CommonMedia:
	js = (
    	'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    	STATIC_URL + 'admin/js/editor.js',
  	)
  	css = {
    	'all': (STATIC_URL + 'admin/css/editor.css',),
	}

admin.site.register(Post, PostAdmin, Media = CommonMedia)