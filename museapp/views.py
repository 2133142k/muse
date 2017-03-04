from django.shortcuts import render

# Create your views here.
def testBase(request):
    context_dict = {"SignedIn":False, "Username": "Alice"}
    return render( request, "muse/base.html", context_dict)
