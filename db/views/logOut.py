from django.http import  HttpResponseRedirect
from django.contrib.auth import logout
def getLogOut(request):
    logout(request)
    return HttpResponseRedirect(f'/accounts/login/')