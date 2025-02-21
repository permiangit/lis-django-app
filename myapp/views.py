from django.shortcuts import render, redirect
from .forms import EntryForm
from .models import Entry

def home(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmation')
    else:
        form = EntryForm()
    return render(request, 'myapp/home.html', {'form': form})

def confirmation(request):
    entries = Entry.objects.all().order_by('-created_at')
    return render(request, 'myapp/confirmation.html', {'entries': entries})