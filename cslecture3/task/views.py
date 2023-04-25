from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# task = []

class NewTaskForm(forms.Form):
    taskk = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    if "task" not in request.session:
        request.session["task"] = []
    return render(request, 'task/index.html', {
        "task": request.session["task"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            taskk = form.cleaned_data["taskk"]
            # task.append(taskk)
            request.session["task"] += [taskk]
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(request, 'task/add.html', {
        "form": form
    })
    return render(request, 'task/add.html', {
        "form": NewTaskForm()
    })