from django.shortcuts import render
from  .models import Record;
from .forms import RecordForm
from .function import *
from django.shortcuts import redirect

def add_new_text(request) :
    form = RecordForm()
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid() :
            form.save()
        if 'save_show' in request.POST :
            return redirect('list_of_notes')
    return render(request, '../templates/add_new_text.html', {'form': form})

def list_of_notes(request):
    records = Record.objects.all();
    sorted_results = sorted(records, key= lambda t: t._get_unique_elements(), reverse=True)
    return render(request, '../templates/list_of_notes.html', {
    'records': sorted_results
    })