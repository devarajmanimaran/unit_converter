from django.shortcuts import render

def fluids_converter(request):
    context = {
        'conversion_type': 'flow',  # Default to Length
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
                "flow": {
                    "cubic meter per second": 1,
                    "liter per second": 0.001,
                    "gallon per minute": 0.00006309
                },
                "flow_mass": {
                    "kilogram per second": 1,
                    "gram per second": 0.001,
                    "pound per second": 0.453592
                },
                "flow_molar": {
                    "mole per second": 1,
                    "kilomole per hour": 0.000277778
                },
                "mass_flux_density": {
                    "kilogram per square meter second": 1,
                    "gram per square meter second": 0.001
                },
                "concentration_molar": {
                    "mole per cubic meter": 1,
                    "mole per liter": 1000
                },
                "concentration_solution": {
                    "gram per liter": 1,
                    "milligram per liter": 0.001
                },
                "viscosity_dynamic": {
                    "pascal second": 1,
                    "poise": 0.1
                },
                "viscosity_kinematic": {
                    "square meter per second": 1,
                    "stokes": 0.0001
                },
                "surface_tension": {
                    "newton per meter": 1,
                    "dyne per centimeter": 0.001
                },
                "permeability": {
                    "darcy": 1,
                    "square meter": 9.869233e-13
                }
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

    return render(request, "fluids/fluids_converter.html", context)