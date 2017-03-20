from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	pictre = models.ImageField(upload_to='profile_images',blank=True)
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=128)
	slug = models.SlugField(unique=True)
	
	def _unicode_(self):
		return self.user.username

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(User, self).save(*args, **kwargs)
	def __str__(self):
		return self.user.username

class MusicProject(models.Model):
	musicFile = models.FileField()
	#tab = models.FileField()
	#LyricAndChord = models.FileField()
	#ClassicalNotation = models.FileField()
	PageDescription = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)
	genre = models.CharField(max_length=128)
	name = models.CharField(max_length=128, unique=True)
	user = models.ForeignKey(User)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(MusicProject, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'MusicProject'

	def __str__(self):
		return str(self.name) + " by " + str(self.user.username)

class Comment(models.Model):
	text = models.CharField(max_length=500)
	user = models.ForeignKey(User)
	project = models.ForeignKey(MusicProject)
	date = models.DateTimeField(auto_now_add=True)
	audio = models.FileField()

	def __str__(self):
		return "comment on "+ self.project.name +" by " + str(self.user.username)

class ExtraFile(models.Model):
        project = models.ForeignKey(MusicProject)
        user = models.ForeignKey(User)
        TAB = "tb"
        LYRIC = "ly"
        CHORD = "ch"
        LYRICANDCHORD = "lc"
        CLASSICAL = "cn"
        OTHER = "ot"
        FILE_TYPE_CHOICES = (
                (TAB, "Tab"),
                (LYRIC, "Lyrics"),
                (CHORD, "Chords"),
                (LYRICANDCHORD, "Lyrics and Chords"),
                (CLASSICAL, "Classical Notation"),
                (OTHER, "Other"),
                )
        file_type = models.CharField(max_length = 2,
                                     choices = FILE_TYPE_CHOICES,
                                     default = OTHER,
                                     blank = False,
                                     )
        extra = models.FileField()

        def __str__(self):
                return project.name + file_type
        
