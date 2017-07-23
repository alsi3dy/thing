from django.contrib import admin

from .models import Post 

from .models import Post_1

class PostModelAdmin(admin.ModelAdmin):
	
	list_display = ['title','timestamp','updated']
	search_fields = ['title']
	list_filter = ['timestamp']
	list_display_links = ['timestamp']
	list_editable = ['title'] 

	class Meta: 
	   model = Post 

admin.site.register(Post,PostModelAdmin) 

class Post_1ModelAdmin(admin.ModelAdmin):
	list_display = ['email','duration']

	class Meta:
		model = Post_1

admin.site.register(Post_1, Post_1ModelAdmin)

