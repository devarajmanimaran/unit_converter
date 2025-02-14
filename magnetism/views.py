from django.shortcuts import render

def magnetism_converter(request):
    context = {
        'conversion_type': 'magnetomotive_force',  # Default to Length
        'value': '',
        'from_unit': '',
        'to_unit': '',
        'result': None
    }

    if request.method == "POST":
        context['value'] = request.POST.get("value", '')
        context['from_unit'] = request.POST.get("from_unit", '')
        context['to_unit'] = request.POST.get("to_unit", '')
        context['converter_type'] = request.POST.get("converter_type", 'magnetomotive_force')

        try:
            value = float(context['value'])
            converter_type = context['converter_type']
            from_unit = context['from_unit']
            to_unit = context['to_unit']

            # All conversion factors and formulas
            conversions = {
                    "magnetomotive_force": {
                        "ampere turn": 1,
                        "gilbert": 0.795773
                    },
                    "magnetic_field_strength": {
                        "ampere per meter": 1,
                        "oersted": 79.5774715
                    },
                    "magnetic_flux": {
                        "weber": 1,
                        "maxwell": 1e-8
                    },
                    "magnetic_flux_density": {
                        "tesla": 1,
                        "gauss": 1e-4
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

    return render(request, "magnetism/magnetism_converter.html", context)