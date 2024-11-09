from django.shortcuts import render

def homepage(request):
    return render(request, 'Project_05_3/homepage.html')