from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact  # Import the Contact model
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, '../templates/index.html')

def about(request):
    return render(request, '../templates/about.html')

def contact(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
    
        # Hash the password before saving it
        hashed_password = make_password(password)
        
        # Save the contact in the Contact model (not the User model)
        contact = Contact.objects.create(username=username, email=email, password=hashed_password)
        contact.save()

        # Redirect to the index page after registration
        return redirect('login')

    return render(request, 'contact.html')

    

def course_outline(request):
    return render(request, '../templates/course_outline.html')

def faculty(request):
    return render(request, '../faculty.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Find the contact by username
        try:
            contact = Contact.objects.get(username=username)
        except Contact.DoesNotExist:
            contact = None
        
        if contact and check_password(password, contact.password):  # Check the hashed password
            # User is authenticated successfully
            return redirect('index')  # Redirect to index page after successful login
        else:
            # If authentication failed
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')
