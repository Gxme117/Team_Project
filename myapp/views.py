from django.shortcuts import redirect, render

from .forms import FeedbackForm # For feedback submission

def landing(request):
    return render(request, 'myapp/landing.html')

def about(request):
    return render(request, 'myapp/about.html')

def team(request):
    return render(request, 'myapp/team.html')

def demo(request):
    return render(request, 'myapp/demo.html')

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'myapp/feedback.html', {'form': form})

def thank_you(request):
    return render(request, 'myapp/thank_you.html')


# Create your views here.
