from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'note_list.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})
