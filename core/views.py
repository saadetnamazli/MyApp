

# Create your views here.
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')  # No need to include the folder name here



from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'my_templates/home.html')

def about(request):
    return render(request, 'my_templates/about.html')

def contact(request):
    return render(request, 'my_templates/contact.html')

def submit_contact(request):
    if request.method == "POST":
        # Process form data (optional: save or send)
        return HttpResponse("Thank you for your message!")
    else:
        return HttpResponse("Invalid request")






