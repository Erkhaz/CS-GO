from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

teams = {
    "Navi": "Navi is csgo team",
    "G2": "G2 is csgo team",
    "Gambit": "Gambit is csgo team"
}


# Create your views here.
def getTeamname(request, name):
    if teams.get(name):
        data = {
            'name': name,
            'description': teams[name]
        }
        return render(request, "csgoteamname/csgotteams.html", context=data)
    else:
        return HttpResponseRedirect('404')


def getSport(request):
    data = {
        'teams': teams.keys()
    }
    return render(request, "csgoteamname/cs_team.html", context=data)


def getNotFound(request):
    return render(request, 'csgoteamname/404.html')


from django.shortcuts import render, redirect

from .forms import AddTeamForm, AddcyberSportTypeForm,AddplayerForm
from .models import csgoplayer,csgo,csgoteam


def addpage(request):
    if request.method == 'POST':
        form = AddcyberSportTypeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                print('something went wrong')
    else:
        form = AddcyberSportTypeForm()
    return render(request, 'sporttype/sporttype.html', {'form': form})


def add_team(request):
    if request.method == 'POST':
        form = AddTeamForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                print('something went wrong')
    else:
        form = AddTeamForm()
    return render(request, 'csgoteamnane/add_team.html', {"form": form})



