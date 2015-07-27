from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Record
from .forms import RecordForm

# Create your views here.

def record_table(request):
    records = Record.objects.order_by('medic_name')
    return render(request, 'regist/record_table.html', {'records': records})

def record_form(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.created_date = timezone.now()
            record.save()
    else:
        form = RecordForm()
    return render(request, 'regist/record_form.html', {'form': form})

def record_edit(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "POST":
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():

                record = form.save(commit=False)
                record.created_date = timezone.now()
                record.save()
    else:
        form = RecordForm(instance=record)
    return render(request, 'regist/record_form.html', {'form': form})