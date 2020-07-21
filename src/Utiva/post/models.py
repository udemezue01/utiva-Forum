from django.db import models

# Create your models here.

from django.conf import settings



class Post(models.Model):

	user 		= models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)

	text 		= models.CharField(max_length = 4000)

	images 		= models.ImageField(blank = True, null = True)

	videos 		= models.FileField(blank = True, null = True)

	created_at  = models.DateTimeField(auto_now_add = True)

	def __str__(self):

		return self.text + " - " + str(self.user)

