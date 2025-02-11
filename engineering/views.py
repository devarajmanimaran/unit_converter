# engineering/views.py
from django.shortcuts import render

def torque_converter(request):
    result = None
    if request.method == 'POST':
        newton_meters = float(request.POST.get('newton_meters', 0))
        pound_feet = newton_meters * 0.737562
        result = f"{newton_meters} N·m = {pound_feet:.2f} lb·ft"
    return render(request, 'engineering/torque_converter.html', {'result': result})