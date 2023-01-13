from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def create_ticket(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        # Save the data to the database
        #...
        # Redirect to a success page
        return redirect('success')
    else:
        return render(request, 'create_ticket.html')

def success(request):
    return render(request, 'success.html')
