from django.shortcuts import render

def electricity_converter(request):
    context = {
        'conversion_type': 'charge',  # Default to Length
        'value': '',
        'from_unit': '',
        'to_unit': '',
        'result': None
    }

    if request.method == "POST":
        context['value'] = request.POST.get("value", '')
        context['from_unit'] = request.POST.get("from_unit", '')
        context['to_unit'] = request.POST.get("to_unit", '')
        context['converter_type'] = request.POST.get("converter_type", 'charge')

        try:
            value = float(context['value'])
            converter_type = context['converter_type']
            from_unit = context['from_unit']
            to_unit = context['to_unit']

            # All conversion factors and formulas
            conversions = {
                "charge": {
                        "coulomb": 1,
                        "ampere hour": 3600
                    },
                    "linear_charge_density": {
                        "coulomb per meter": 1,
                        "millicoulomb per meter": 0.001
                    },
                    "surface_charge_density": {
                        "coulomb per square meter": 1,
                        "millicoulomb per square meter": 0.001
                    },
                    "volume_charge_density": {
                        "coulomb per cubic meter": 1,
                        "millicoulomb per cubic meter": 0.001
                    },
                    "current": {
                        "ampere": 1,
                        "milliampere": 0.001
                    },
                    "linear_current_density": {
                        "ampere per meter": 1,
                        "milliampere per meter": 0.001
                    },
                    "surface_current_density": {
                        "ampere per square meter": 1,
                        "milliampere per square meter": 0.001
                    },
                    "electric_field_strength": {
                        "volt per meter": 1,
                        "kilovolt per meter": 1000
                    },
                    "electric_potential": {
                        "volt": 1,
                        "millivolt": 0.001
                    },
                    "electric_resistance": {
                        "ohm": 1,
                        "milli-ohm": 0.001
                    },
                    "electric_resistivity": {
                        "ohm meter": 1,
                        "milli-ohm meter": 0.001
                    },
                    "electric_conductance": {
                        "siemens": 1,
                        "milli-siemens": 0.001
                    },
                    "electric_conductivity": {
                        "siemens per meter": 1,
                        "milli-siemens per meter": 0.001
                    },
                    "electrostatic_capacitance": {
                        "farad": 1,
                        "microfarad": 1e-6
                    },
                    "inductance": {
                        "henry": 1,
                        "millihenry": 0.001
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

    return render(request, "electricity/electricity_converter.html", context)