from django.shortcuts import render

def radiology_converter(request):
    context = {
        'conversion_type': 'radiation',  # Default to Length
        'value': '',
        'from_unit': '',
        'to_unit': '',
        'result': None
    }

    if request.method == "POST":
        context['value'] = request.POST.get("value", '')
        context['from_unit'] = request.POST.get("from_unit", '')
        context['to_unit'] = request.POST.get("to_unit", '')
        context['converter_type'] = request.POST.get("converter_type", 'radiation')

        try:
            value = float(context['value'])
            converter_type = context['converter_type']
            from_unit = context['from_unit']
            to_unit = context['to_unit']

            # All conversion factors and formulas
            conversions = {
                "radiation": {
                    "gray": 1,
                    "rad": 0.01
                },
                "radiation_activity": {
                    "becquerel": 1,
                    "curie": 3.7e10
                },
                "radiation_exposure": {
                    "coulomb per kilogram": 1,
                    "roentgen": 0.000258
                },
                "radiation_absorbed_dose": {
                    "sievert": 1,
                    "rem": 0.01
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

    return render(request, "radiology/radiology_converter.html", context)