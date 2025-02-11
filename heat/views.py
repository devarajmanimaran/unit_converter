# heat/views.py
from django.shortcuts import render

def thermal_conductivity_converter(request):
    result = None
    if request.method == 'POST':
        watts_per_meter_kelvin = float(request.POST.get('watts_per_meter_kelvin', 0))
        btu_per_hour_foot_fahrenheit = watts_per_meter_kelvin * 0.577789
        result = f"{watts_per_meter_kelvin} W/(m·K) = {btu_per_hour_foot_fahrenheit:.2f} BTU/(hr·ft·°F)"
    return render(request, 'heat/thermal_conductivity_converter.html', {'result': result})