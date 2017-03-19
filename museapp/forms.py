from django import forms
from django.contrib.auth.models import User
from museapp.models import MusicProject, UserProfile, Comment, ExtraFile



class CommentForm(forms.ModelForm):
	text = forms.CharField(max_length=500,widget=forms.Textarea,help_text="Comment")
	
	#date = forms.DateTimeField()
	audio = forms.FileField(required = False)

	class Meta:
		model=Comment
		fields = ('text','audio')

class ProjectForm(forms.ModelForm):
        name = forms.CharField(max_length=128, help_text="Please input name of the project.")
        genre = forms.CharField(max_length=128,help_text="Please input the genre.")
        PageDescription = forms.CharField(max_length=500,widget=forms.Textarea,help_text="Please enter the description for the project")
	MusicFile = forms.FileField(help_text="Please input the file to upload.", required=False)
	#tab = forms.FileField(help_text="Please input the file to upload.",required=False)
	#LyricAndChord = forms.FileField(help_text="Please input the file to upload.",required=False)
	#ClassicalNotation = forms.FileField(help_text="Please input the file to upload.",required=False)
	
	#date = forms.DateTimeField.auto_now_add(widget=forms.Hiddentinput())
	
	

	class Meta:
		model = MusicProject
		fields =('name','genre','PageDescription','MusicFile')#,'tab','LyricAndChord','ClassicalNotation')

class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=128,help_text="Please enter your username.")
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput(),help_text="Please enter a password.")
	name = forms.CharField(max_length=128,help_text="Please enter your name.")

	class Meta:
		model = User
		fields = ('username','password','email','name')

class UserProfileForm(forms.ModelForm):
	picture = forms.ImageField(help_text="Select a profile picture to upload.",required=False)
	class Meta:
		model = UserProfile
		fields=['website', 'picture']

class ExtraFileForm(forms.ModelForm):
        file_type = forms.ChoiceField(choices = ExtraFile.FILE_TYPE_CHOICES)
        extra = forms.FileField(help_text="Please input the file to upload.", required=False)

        class Meta:
                model = ExtraFile
                fields= ["file_type", "extra"]
        
