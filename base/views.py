from django.shortcuts import render, redirect
from .models import Notes
from .forms import notesform


# from django.http import HttpResponse


def homepage(request):
    notes = Notes.objects.all()
    dict = {'notes': notes}
    # return HttpResponse('homepage')
    return render(request, 'base/homepage.html', dict)


def notespage(request, pk):
    note = Notes.objects.get(id=pk)
    dict = {'note': note}
    return render(request, 'base/notespage.html', dict)


def newnote(request):
    form = notesform
    if request.method == 'POST':
        form = notesform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    dict = {'form': form}
    return render(request, 'base/notesform.html', dict)


def modifiednote(request, pk):
    note = Notes.objects.get(id=pk)
    form = notesform(instance=note)
    if request.method == 'POST':
        form = notesform(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    dict = {'form': form}
    return render(request, 'base/notesform.html', dict)
