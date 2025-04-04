from django.shortcuts import render
from django.http import HttpResponse # For feedback submission

def landing(request):
    return render(request, 'myapp/landing.html')

def about(request):
    return render(request, 'myapp/about.html')

def team(request):
    return render(request, 'myapp/team.html')

def demo(request):
    return render(request, 'myapp/demo.html')

def feedback(request):
    if request.method == 'POST':    

        # Handle form submission (e.g. save feedback or email it)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # for now, well print ot console, later we'll save to our Database or email
        print(f"Feedback from {name} | {email}: {message}")
        return HttpResponse ("Thank you for your feedback! The team will review it shortly.")
    
    return render(request, 'myapp/feedback.html')


# Create your views here.
