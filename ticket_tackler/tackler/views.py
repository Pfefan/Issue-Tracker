from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegisterForm
from .models import Ticket, Ticket_Comments


@login_required(login_url='login')
def index(request):
    """
    Render the index page and display all tickets from the database.

    Args:
        request (HttpRequest): The incoming request object.

    Returns:
        HttpResponse: The rendered index page with a context containing all tickets.
    """
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}

    return render(request, 'index.html', context)

@login_required(login_url='login')
def create_ticket(request):
    """
    Handle the creation of a new ticket.

    Args:
        request (HttpRequest): The incoming request object.

    Returns:
        HttpResponse: A redirect to the index page if the ticket was created successfully,
        or a redirect to the login page if the user is not authenticated.
        Otherwise, it returns the create_ticket.html template.
    """
    users = User.objects.all()
    context = {'users': users}
    if request.method == 'POST':
        if request.user.is_authenticated:
            title = request.POST.get('title')
            description = request.POST.get('description')
            ticket_type = request.POST.get('type')
            relevance = request.POST.get('relevance')
            assigned_users_ids = request.POST.getlist('assigned_users')
            ticket_instance = Ticket.objects.create(
                title=title,
                content=description,
                type=ticket_type,
                relevance=relevance,
                is_open=True,
                user=request.user
            )
            ticket_instance.assigned_users.set(User.objects.filter(id__in=assigned_users_ids))
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, 'create_ticket.html', context)



@login_required(login_url='login')
def view_ticket(request, ticket_id):
    """
    A view for viewing the details of a ticket and handling the actions performed on the ticket. 
    Actions include editing the ticket and closing the ticket. It also allows replying to the ticket.

    Parameters:
     request (HttpRequest): The request object used for handling user inputs.
    ticket_id (int): The primary key of the ticket to be viewed.
    
    Returns:
    render: Renders the view_ticket.html template with the context containing the details of the ticket and its replies.
    """
    users = User.objects.all()
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    replies = Ticket_Comments.objects.filter(ticket_id=ticket_id)

    if request.method == 'POST':
        if 'Reply' in request.POST:
            reply = Ticket_Comments.objects.create(ticket=ticket, user=request.user, content=request.POST.get('content'))
        elif request.user.id == ticket.user.id and 'close' in request.POST:
            ticket.resolved = True
            ticket.save()
        elif 'ticket-title' in request.POST:
            ticket.title = request.POST.get('ticket-title')
            if request.POST.getlist('ticket-assigned-users') != []:
                ticket.assigned_users.set(User.objects.filter(id__in=request.POST.getlist('ticket-assigned-users')))
            ticket.type = request.POST.get('ticket-type')
            ticket.relevance = request.POST.get('ticket-relevance')
            ticket.content = request.POST.get('ticket-content')
            ticket.save()
    
    context = {
        'ticket': ticket,
        'replies': replies,
        'users' : users,
    }
    return render(request, 'view_ticket.html', context)



def login_view(request):
    """
    A view for handling user login requests. 
    If the request method is POST, the form data is processed and if the form is valid, the user is authenticated and logged in. 
    If the request method is GET, a blank form is displayed for the user to fill.
    
    Parameters: 
    request (HttpRequest): The request object used for handling user inputs.
    
    Returns:
    render: Renders the login.html template with the form for authentication.
    redirect: Redirects to the index page if the user is successfully authenticated.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    """View function that logs out the user and redirects them to the login page."""
    logout(request)
    return redirect('login')

def register_view(request):
    """View function that handles user registration.
    If the request method is POST, the form data is processed and a new user is created and authenticated.
    If the request method is GET, an empty form is displayed for the user to fill out.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
