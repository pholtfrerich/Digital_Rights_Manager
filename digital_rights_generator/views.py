from django.shortcuts import render
from .forms import DigitalRightsGeneratorForm
from .models import generate_pdf


def digital_rights_generator(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DigitalRightsGeneratorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return generate_pdf(form.cleaned_data)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DigitalRightsGeneratorForm()

    return render(request, 'index.html', {'form': form})

    render(request, 'contract.html')