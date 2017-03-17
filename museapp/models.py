from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	pictre = models.ImageField(upload_to='profile_images',blank=true)
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=128)
	slug = models.SlugField(unique=True)
	
	def _unicode_(self):
		return self.user.username

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(User, self).save(*args, **kwargs)

class MusicProject(models.Model):
	musicFile = models.FileField()
	tab = models.FileField()
	LyricAndChord = models.FileField()
	ClassicalNotation = models.FileField()
	PageDescription = models.CharField(max_length=500)
	date = models.DateTimeField()
	genre = models.CharField(max_length=128)
	name = models.CharField(max_length=128, unique=True)
	user = models.ForeignKey(User)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
        if not self.id:
            self.date = timezone.now()
        super(MusicProject, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'MusicProject'

	def __str__(self):
		return self.name

class Comment(models.Model):
	text = models.CharField(max_length=500)
	user = models.ForeignKey(User)
	project = models.ForeignKey(MusicProject)
	date = models.DateTimeField()
	audio = models.FileField()
    id = models.IntegerField()

	def __str__(self):
		return self.user

    def save(self,*args,**kwargs):
        if not self.id:
            self.date = timezone.now()
        return super(Comment, self).save(*args,**kwargs)