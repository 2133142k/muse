from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from museapp.forms import UserForm, UserProfileForm, ProjectForm
from museapp.models import MusicProject, Comment
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def testBase(request):
    context_dict = {"SignedIn":False, "Username": "Alice"}
    return render( request, "muse/base.html", context_dict)

def homePage(request):
    context_dict = {"SignedIn":False, "Username": "Alice",
                    "IntrductionText":"Welcome to Muse a website to share your musical ideas",
                    "ProjectPreviews":[{"ProjectName":"13 bar blues",
                                        "ProjectAuthor":"UnluckyCoolCat24",
                                        "ProjectGenre":"Blues",
                                        "NumberOfComments":2,
                                        "ProjectDescription":"Like the 12 bar blues but with an added bar!"},
                                       ],}
    return render ( request, "muse/home.html", context_dict)
	
def testAccountPage(request):
    #should only be accessible while logged in
    context_dict = {"SignedIn":True, "Username": "Alice",
                    "IntrductionText":"Welcome to Muse a website to share your musical ideas",
                    "ProjectPreviews":[{"ProjectName":"13 bar blues",
                                        "ProjectAuthor":"UnluckyCoolCat24",
                                        "ProjectGenre":"Blues",
                                        "NumberOfComments":2,
                                        "ProjectDescription":"Like the 12 bar blues but with an added bar!"},
                                       ],}
    return render ( request, "muse/accountPage.html", context_dict)

def testProjectViewPage(request):
    #should only be accessible while logged in
    context_dict = {"SignedIn":True, "Username":"Alice",
                    "Project":{"ProjectName":"You Deserve The Sun",
                               "ProjectAuthor":"GOO",
                               "ProjectGenre":"Folk",
                               "NumberOfComments":0,
                               "ProjectDescription":"I wrote this a while back I think its a nice song but I don't think my singing can do it justice. I would welcome anyone who wants to try to cover it",
                               "AudioFile":"/media/YoudeservetheSun.mp3",
                               "ExtraFiles":[{"filename":"YoudeservetheSun.txt","location":"/media/","filetype":"Lyrics"}]
                               }}

    return render ( request, "muse/projectView.html", context_dict)

def jsonComments(request):
    #should only be accessible while logged in
    response = {"comments":[{"author":"Alice","commentText":"Cool, I like the chord change between the 4th and 5th bars"},
                            {"author":"Huffbert","commentText":"Perhaps it should be D Major 7 instead of D Major after the E Major"},
                            ]
                }
    return JsonResponse(response)

def about(request):
    context_dict = {"SignedIn":False}

    return render ( request, "muse/about.html", context_dict)

def user_login(request):
    context_dict = {"SignedIn":False}

    if request.method == "POST":
        #get credentials
        username = request.POST.get("username")
        password = request.POST.get("password")

        #check credentials
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                #user credentials correct and user is active log them in
                login(request, user)

                #redirect to users page
                user_id = user.id
                return HttpResponseRedirect("/muse/users/%d/" %user_id)
            else:
                #user disabled
                return HttpResponse("Your account is disabled")
        else:
            return HttpResponse("Invalid username or password")


    return render ( request, "muse/login.html", context_dict)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/muse/")
	
def register(request):
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		#profile_form = UserProfileForm(data=request.POST)
		
		if user_form.is_valid(): # and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			#profile = profile_form.save(commit=False)
			#profile.user = user
			#if 'picture' in request.FILES:
			#	profile.picture = request.FILES['picture']
			#profile.save()
			registerd = True
		else:
			print(user_form.errors)#, profile_form.errors)
	else:
	    user_form = UserForm()
	    #profile_form = UserProfileForm()
            return render ( request, 'muse/register.html', {'user_form': user_form,  'registered': registered})#'profile_form': profile_form,})
	
def getProjectPreviews(request):
    response = getUserInfo(request)
    number = request.GET.get('number')



    project_list = MusicProject.objects
    if (request.GET.get('owned') == 'true'):
        #get only owner's projects
        project_list = project_list.filter(user__exact=request.user)
    else:
        #return random projects
        pass #randomise

        #workout number of projects to rerturn
    if (not number.isdigit()):
        number = 5
    else:
        number = int(number)
    if number < len(project_list):
        project_list = project_list[:number]
    


    #return projects JSON
    response["ProjectPreviews"] = list(project_list.values())#add wanted fields

    print response
    
    return JsonResponse(response)

def project(request, project_name_slug):
    context_dict = getUserInfo(request)
    if (request.method == "GET"):
        #get a project
        context_dict["Project"] = {"ProjectName":"13 bar blues",
                               "ProjectAuthor":"UnluckyCoolCat24",
                               "ProjectGenre":"Blues",
                               "NumberOfComments":2,
                               "ProjectDescription":"Like the 12 bar blues but with an added bar!",
                               "AudioFile":"13-bar-blues.mp3",
                               "ExtraFiles":[{"filename":"13-bar-blues-sheetmusic.pdf","filetype":"Sheetmusic"}]}

        return render ( request, "muse/projectView.html", context_dict)

    elif (request.method == "DELETE"):
        #not yet implemented
        #delete project
        return HttpResponseNotModified()

    elif (request.method == "PUT"):
        #not yet implemented
        #edit project
        return HttpResponseNotModified()

    else:
        #not a valid request
        return HttpResponseBadRequest()

def createProject(request):

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return httpResponseRedirect("/muse/users/%d/" %request.user.id)
        else:
            print form.errors
    else:
        form = ProjectForm()

    return render (request, "muse/newProject.html", {"projectForm":form})

def userPage(request, user_id):
    context_dict = getUserInfo(request)
    return render(request, "muse/accountPage.html", context_dict)
    
##    if (request.method == "GET"):
##        #get an accountPage
##        #check username_slug == page's username
##        return render(request, "muse/accountPage.html", context_dict)
##
##    elif (request.method == "DELETE"):
##        #not yet implemented
##        #delete account
##        return HttpResponseBadRequest()
##
##    elif (request.method == "PUT"):
##        #not yet implemented
##        #change password
##        return HttpResponseBadRequest()

def getUserInfo(request):

    signedIn = bool(request.user.is_authenticated)

    username = request.user.username
    userid = request.user.id
    return {"SignedIn":signedIn, "Username":username, "UserId":userid}
    
        
