from django.shortcuts import render

# Create your views here.
# common/views.py
from django.shortcuts import render

def length_converter(request):
    result = None
    if request.method == 'POST':
        meters = float(request.POST.get('meters', 0))
        feet = meters * 3.28084
        result = f"{meters} meters = {feet:.2f} feet"
    return render(request, 'common/length_converter.html', {'result': result})