from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, Http404
from museapp.forms import UserForm, UserProfileForm, ProjectForm, CommentForm
from museapp.models import MusicProject, Comment
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.core import serializers

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
                return render ( request, "muse/message.html", {"message":"Your account is disabled"})
        else:
            return render ( request, "muse/message.html", {"message":"Invalid username or password"})


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
			update_session_auth_hash(request, user)
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

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()#updates password and logs user out
            update_session_auth_hash(request, user)#logs user back in
            return render ( request, "muse/message.html", {"message":"Your password has been changed"})
        else:
            return render ( request, "muse/message.html", {"message":"There was an error changing your password"})
    else:
        form = PasswordChangeForm(request.user)
    context_dict = {"form":form}
    return render(request, "muse/changePassword.html",context_dict)

def user_delete(request, user_id):
    user = User.objects.get(id__exact=int(user_id))

    #check user can edit
    if request.user.id == user.id:

        if (request.method == "POST"):
            user.delete()
            return render ( request, "muse/message.html", {"message":"user " + user_id + " deleted"})

    return render ( request, "muse/message.html", {"message":"Delete failed"})
	
def getProjectPreviews(request):
    response = getUserInfo(request)
    number = request.GET.get('number')

    project_list = MusicProject.objects

    user_id = request.GET.get('user_id', default = False)

    if (user_id.isdigit()):
        user_id = int(user_id)
    else:
        user_id = -1

    
    
    #print user_id
    if (user_id != -1):
        #get only owner's projects
        project_list = project_list.filter(user__id__exact=user_id)
    else:
        #return random projects
        project_list = project_list.all()

        #workout number of projects to return
    if (not number.isdigit()):
        number = 5
    else:
        number = int(number)
    if number < len(project_list):
        project_list = project_list[:number]

    projects = []
    for project in project_list.iterator():
        next_project = {"name":project.name,
                        "slug":project.slug,
                        "genre":project.genre,
                        "PageDescription":project.PageDescription}        
        number_of_comments = Comment.objects.filter(project__slug=project.slug).count()
        next_project["NumberOfComments"] = number_of_comments
        next_project["Author"] = {"name": project.user.username,
                                  "id": project.user.id}

        rendered_project = render(request,'muse/projectPreview.html',next_project)
        del rendered_project["Content-Type"]
        print rendered_project
        projects.append(str(rendered_project))
    print projects
        

        
    


    #return projects JSON
    response["ProjectPreviews"] = projects

    #print response
    
    return JsonResponse(response)

def project(request, project_name_slug):
    context_dict = getUserInfo(request)
    if (request.method == "GET"):
        #get a project
        try:
            musicProject = MusicProject.objects.get(slug=project_name_slug)
        except:
            #project doesn't exist
            raise Http404("User does not exist")
        context_dict["Project"] = musicProject
        context_dict["commentForm"] = CommentForm()
##        {"ProjectName":"13 bar blues",
##                               "ProjectAuthor":"UnluckyCoolCat24",
##                               "ProjectGenre":"Blues",
##                               "NumberOfComments":2,
##                               "ProjectDescription":"Like the 12 bar blues but with an added bar!",
##                               "AudioFile":"13-bar-blues.mp3",
##                               "ExtraFiles":[{"filename":"13-bar-blues-sheetmusic.pdf","filetype":"Sheetmusic"}]}

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
        return render ( request, "muse/message.html", {"message":"Found no projects"})

def createProject(request):

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return HttpResponseRedirect("/muse/users/%d/" %request.user.id)
        else:
            print form.errors
    else:
        form = ProjectForm()

    return render (request, "muse/newProject.html", {"projectForm":form})

def userPage(request, user_id):
    context_dict = getUserInfo(request)
    try:
        pageOwner = User.objects.get(id__exact=int(user_id)).username
        context_dict["owner"] = pageOwner
    except:
        #user doesn't exist 404 error
        raise Http404("User does not exist")
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

def comments(request, project_name_slug):

    comments = Comment.objects.filter(project__slug__exact=project_name_slug)


    comment_list = []
    for comment in comments.iterator():
        print comment.user == request.user
        print comment.project.user == request.user
        can_Edit = (comment.user == request.user or comment.project.user == request.user)
        next_comment = render(request, "muse/comment.html",{"comment":comment,"canEdit":can_Edit})
##        {"id":comment.id,
##                        "author":comment.user.username,
##                        "commentText":comment.text,
##                        "musicfile":comment.audio.url,
##                        "canEdit":can_Edit,}
        del next_comment["Content-Type"]
        print next_comment
        comment_list.append(str(next_comment))

    if len(comment_list) == 0:
        comment_list = ["There are no comments here!"]
    response = {"comments":comment_list}
    print response
    #comments = serializers.serialize("json", comments)
    
    
    #comments = [{"author":"Alice","commentText":"Cool, I like the chord change between the 4th and 5th bars"},
    #                        {"author":"Huffbert","commentText":"Perhaps it should be D Major 7 instead of D Major after the E Major"},
    #                        ]
    #response = {"comments":comments}
    #response = serializers.serialize("json", response)
    return JsonResponse(response)

def newComment(request, project_name_slug):
    try:
        project = MusicProject.objects.get(slug=project_name_slug)
    except MusicProject.DoesNotExist:
        project = None

    author = request.user

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = author
            comment.project = project
            #comment.date = now???
            comment.save()

    return HttpResponseRedirect("/muse/projects/"+project_name_slug+"/")
##	registered = False
##	
##	if request.method == 'POST':
##		user_form = UserForm(data=request.POST)
##		#profile_form = UserProfileForm(data=request.POST)
##		
##		if user_form.is_valid(): # and profile_form.is_valid():
##			user = user_form.save()
##			user.set_password(user.password)
##			user.save()
##			#profile = profile_form.save(commit=False)
##			#profile.user = user
##			#if 'picture' in request.FILES:
##			#	profile.picture = request.FILES['picture']
##			#profile.save()
##			registerd = True
##		else:
##			print(user_form.errors)#, profile_form.errors)
##	else:
##	    user_form = UserForm()
##	    #profile_form = UserProfileForm()
##            return render ( request, 'muse/register.html', {'user_form': user_form,  'registered': registered})#'profile_form': profile_form,})

def deleteComment(request, project_name_slug, comment_id):

    comment = Comment.objects.get(id__exact=int(comment_id))
    print "deleting comment" + comment_id
    print request.user.id == comment.user.id
    print request.user.id == comment.project.user.id
    print request.method

    #check user can edit
    if ((request.user.id == comment.user.id) or (request.user.id == comment.project.user.id)):

        print 
        

        if (request.method == "POST"):
            comment.delete()
            return HttpResponseRedirect("/muse/projects/"+project_name_slug+"/")

    render ( request, "muse/message.html", {"message":"Delete failed"})   
        

def getUserInfo(request):

    signedIn = bool(request.user.is_authenticated)

    username = request.user.username
    userid = request.user.id
    return {"SignedIn":signedIn, "Username":username, "UserId":userid}
    
        
