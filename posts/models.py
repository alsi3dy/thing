from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length = 50)
	content = models.TextField()
	updated = models.DateTimeField(auto_now = True) 
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title 

	def absurd(self):
		return reverse("posts:id" , kwargs ={"post_id": self.id})

class Post_1(models.Model):
	email = models.EmailField()
	duration = models.DurationField(null=True, blank=True)



