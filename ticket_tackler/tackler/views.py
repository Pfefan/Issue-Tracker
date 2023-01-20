from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EditTicketForm, RegisterForm, ReplyForm
from .models import Ticket, Ticket_Replies


def index(request):
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    
    return render(request, 'index.html', context)


def create_ticket(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            title = request.POST.get('title')
            description = request.POST.get('description')
            topic = request.POST.get('topic')
            relevance = request.POST.get('relevance')
            ticket_instance = Ticket.objects.create(title=title, content=description, topic = topic, relevance = relevance, resolved=False, user_id=request.user.id)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, 'create_ticket.html')


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    replies = Ticket_Replies.objects.filter(ticket_id=ticket_id)

    if request.method == 'POST':
        if request.user == ticket.user_id:
            if 'edit' in request.POST:
                ticket.title = request.POST.get('title')
                ticket.content = request.POST.get('content')
                ticket.save()
            elif 'close' in request.POST:
                ticket.resolved = True
                ticket.save()
        print(request.POST)
        if 'Reply' in request.POST:
            
            reply = Ticket_Replies.objects.create(ticket_id=ticket, user_id=request.user, content=request.POST.get('content'))
    context = {
        'ticket': ticket,
        'replies': replies,
    }
    return render(request, 'view_ticket.html', context)


def login_view(request):
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

def register_view(request):
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
