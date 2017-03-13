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
    context_dict = {"SingedIn":True, "Username":"Alice",
                    "Project":{"ProjectName":"13 bar blues",
                               "ProjectAuthor":"UnluckyCoolCat24",
                               "ProjectGenre":"Blues",
                               "NumberOfComments":2,
                               "ProjectDescription":"Like the 12 bar blues but with an added bar!",
                               "AudioFile":"13-bar-blues.mp3",
                               "ExtraFiles":[{"filename":"13-bar-blues-sheetmusic.pdf","filetype":"Sheetmusic"}]}}

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
