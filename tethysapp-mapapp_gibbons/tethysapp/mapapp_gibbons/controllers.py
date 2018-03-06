from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button, RangeSlider, TextInput, DatePicker

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
    time_slider = RangeSlider(display_text='Time of Day',
                          name='time_slider',
                          min=0,
                          max=24,
                          initial=12,
                          step=1
    )

    adjust_slider = RangeSlider(display_text='Air Quality Adjustment',
                          name='slider2',
                          min=-5,
                          max=5,
                          initial=0,
                          step=0.5,
    )

    search_input = TextInput(display_text='Location Search',
                            name = 'search_input',
                            icon_append = 'glyphicon glyphicon-search',
    )

    date_picker = DatePicker(name='date_picker',
                             display_text='Date',
                             autoclose=True,
                             format='MM d, yyyy',
                             start_date='03/05/18',
                             start_view='decade',
                             today_button=True,
                             initial='March 5, 2018'
    )

    context = {
        'time_slider': time_slider,
        'adjust_slider': adjust_slider,
        'search_input': search_input,
        'date_picker': date_picker,
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