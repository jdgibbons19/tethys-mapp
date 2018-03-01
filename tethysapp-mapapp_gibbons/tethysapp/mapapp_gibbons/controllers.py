from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """


    context = {

    }

    return render(request, 'mapapp_gibbons/home.html', context)

@login_required()
def mapview(request):
    """
    Controller for the app map page.
    """




    context = {

    }

    return render(request, 'mapapp_gibbons/mapview.html', context)

@login_required()
def data(request):
    """
    Controller for the app data page.
    """


    context = {

    }

    return render(request, 'mapapp_gibbons/data.html', context)

@login_required()
def about(request):
    """
    Controller for the app about page.
    """


    context = {

    }

    return render(request, 'mapapp_gibbons/about.html', context)

@login_required()
def proposal(request):
    """
    Controller for the app proposal page.
    """


    context = {

    }

    return render(request, 'mapapp_gibbons/proposal.html', context)

@login_required()
def mockups(request):
    """
    Controller for the app mockups page.
    """


    context = {

    }

    return render(request, 'mapapp_gibbons/mockups.html', context)