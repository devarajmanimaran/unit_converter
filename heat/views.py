from django.shortcuts import render

def heat_converter(request):
    context = {
        'conversion_type': 'fuel_efficiency_mass',  # Default to Length
        'value': '',
        'from_unit': '',
        'to_unit': '',
        'result': None
    }

    if request.method == "POST":
        context['value'] = request.POST.get("value", '')
        context['from_unit'] = request.POST.get("from_unit", '')
        context['to_unit'] = request.POST.get("to_unit", '')
        context['converter_type'] = request.POST.get("converter_type", 'length')

        try:
            value = float(context['value'])
            converter_type = context['converter_type']
            from_unit = context['from_unit']
            to_unit = context['to_unit']

            # All conversion factors and formulas
            conversions = {
                    "fuel_efficiency_mass": {
                    "kilometer per kilogram": 1,
                    "mile per pound": 0.425144,
                    "meter per gram": 0.001
                    },
                    "fuel_efficiency_volume": {
                        "kilometer per liter": 1,
                        "mile per gallon": 0.425144,
                        "meter per milliliter": 0.001
                    },
                    "temperature_interval": {
                        "celsius": 1,
                        "kelvin": 1,
                        "fahrenheit": 1.8
                    },
                    "thermal_expansion": {
                        "per kelvin": 1,
                        "per celsius": 1
                    },
                    "thermal_resistance": {
                        "kelvin per watt": 1,
                        "celsius per watt": 1
                    },
                    "thermal_conductivity": {
                        "watt per meter kelvin": 1,
                        "calorie per second centimeter celsius": 0.2388459
                    },
                    "specific_heat_capacity": {
                        "joule per kilogram kelvin": 1,
                        "calorie per gram celsius": 4.184
                    },
                    "heat_density": {
                        "joule per cubic meter": 1,
                        "calorie per cubic centimeter": 4184
                    },
                    "heat_flux_density": {
                        "watt per square meter": 1,
                        "calorie per second square centimeter": 0.0002388459
                    },
                    "heat_transfer_coefficient": {
                        "watt per square meter kelvin": 1,
                        "calorie per second square meter celsius": 0.2388459
                    },
            }

            # Handle the conversion
            if converter_type in conversions:
                if converter_type in ['temperature', 'numbers']:
                    # Special handling for temperature and number systems
                    result = conversions[converter_type](value, from_unit, to_unit)
                    if converter_type == 'numbers':
                        context['result'] = result  # Don't round number conversions
                    else:
                        context['result'] = round(float(result), 6)
                else:
                    # Standard conversion for other types
                    result = (value * conversions[converter_type][from_unit]) / conversions[converter_type][to_unit]
                    context['result'] = round(result, 6)  # Round to 6 decimal places

        except (ValueError, KeyError, TypeError) as e:
            context['error'] = "Invalid conversion parameters"

    return render(request, "heat/heat_converter.html", context)