from django.shortcuts import render
from .models import Panel
from .models import ImportData
from .models import UploadData
from .forms import ImportDataForm
from .forms import UploadDataForm

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def panel_list(request):
    panels = Panel.objects.all()
    return render(request, 'archive/panel_list.html', {'panels' : panels})

def uploaddata(request):
    # Handle file upload
    if request.method == 'POST':
        form = UploadDataForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = UploadData(datafile = request.FILES['datafile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('archive.views.uploaddata'))
    else:
        form = UploadDataForm() # A empty, unbound form

    # Load documents for the list page
    documents = UploadData.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'archive/uploaddata.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def importdata(request):
    # Handle file upload
    if request.method == 'POST':
        form = ImportDataForm(request.POST, request.FILES)
        if form.is_valid():
            # call code to open document and create panel data
            documents = UploadData.objects.all()
            
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('archive.views.importdata'))
    else:
        form = ImportDataForm() # A empty, unbound form

    # Load documents for the list page
    documents = UploadData.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'archive/importdata.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )