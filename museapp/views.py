from django.shortcuts import render
from django.http import JsonResponse

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
	
def getProjectPreviews(request):
    response = getUserInfo(request)
    number = request.GET.get('number')
    if (not number.isdigit()):
        number = 5
    else:
        number = int(number)
    if (request.GET.get('owned') == 'true'):
        #get only owner's projects
        #reduce to number responses
        pass
    else:
        #return number random projects
        pass


    #return projects JSON
    response["ProjectPreviews"] = [{"ProjectName":"13 bar blues",
                               "ProjectAuthor":"UnluckyCoolCat24",
                               "ProjectGenre":"Blues",
                               "NumberOfComments":2,
                               "ProjectDescription":"Like the 12 bar blues but with an added bar!"}]
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

    elif (request.method == "POST"):
        #not yet implemented
        #new project
        return HttpResponseNotModified()

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

def userPage(request):
    context_dict = getUserInfo(request)
    if (request.method == "GET"):
        #get an accountPage
        #check username_slug == page's username
        return render(request, "muse/accountPage.html", context_dict)
    
    elif (request.method == "POST"):
        #not yet implemented
        #new user
        return HttpResponseBadRequest()

    elif (request.method == "DELETE"):
        #not yet implemented
        #delete account
        return HttpResponseBadRequest()

    elif (request.method == "PUT"):
        #not yet implemented
        #change password
        return HttpResponseBadRequest()

def getUserInfo(request):
    return {"SignedIn":True, "Username":"Alice"}
    
        
