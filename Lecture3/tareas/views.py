from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class NewTaskForm( forms.Form):
    tarea = forms.CharField( label = "New Task")
    #priority = forms.IntegerField( label = "Priority", min_value=1, max_value=5)

# Create your views here.
def index( request ):
    if "tareas" not in request.session:
        request.session["tareas"] = []

    return render(request, "tareas/index.html", {
        "tareas": request.session["tareas"]
    })

def add( request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            tarea = form.cleaned_data["tarea"]
            request.session["tareas"] += [tarea]
            return HttpResponseRedirect(reverse("tareas:index"))
        else:
            return render(request, "tareas/add.html",{
                "form": form
            })

    return render( request, "tareas/add.html", {
        "form": NewTaskForm()
    })
