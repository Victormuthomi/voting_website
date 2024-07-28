from django.shortcuts import render

# Create your views here.
def voting(request):
   """Return the voting page"""
   return render(request, 'voting/voting.xhtml',)
