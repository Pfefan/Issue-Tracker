from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from .models import Ticket, Ticket_Replies
from .forms import RegisterForm
from django.contrib.auth.models import User


def index(request):
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    
    return render(request, 'index.html', context)


def create_ticket(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            title = request.POST.get('title')
            content = request.POST.get('description')
            topic = request.POST.get('topic')
            relevance = request.POST.get('relevance')
            ticket_instance = Ticket.objects.create(title=title, content=content, topic=topic, relevance=relevance, resolved=False, user_id=request.user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, 'create_ticket.html')



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
