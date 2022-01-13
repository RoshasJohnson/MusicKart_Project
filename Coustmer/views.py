from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request,'User_templates/signin.html')
    #  return render(request,'User_templates/Home.html')
   