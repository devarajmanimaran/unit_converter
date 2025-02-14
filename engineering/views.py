from django.shortcuts import render

def engineering_converter(request):
    context = {
        'conversion_type': 'velocity_angular',  # Default to Length
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
                "velocity_angular": {
                    "radian per second": 1,
                    "degree per second": 0.0174533,
                    "revolution per minute": 0.10472,
                    "hertz": 6.28319,
                    "revolution per second": 1,
                    "gradian per second": 0.0157079
                },
                "acceleration": {
                    "meter per second squared": 1,
                    "foot per second squared": 0.3048,
                    "gal": 0.01,
                    "standard gravity": 9.80665,
                    "inch per second squared": 0.0254,
                    "mile per hour squared": 0.000124178
                },
                "acceleration_angular": {
                    "radian per second squared": 1,
                    "degree per second squared": 0.0174533,
                    "revolution per minute squared": 0.00174533,
                    "gradian per second squared": 0.0157079
                },
                "density": {
                    "kilogram per cubic meter": 1,
                    "gram per cubic centimeter": 1000,
                    "pound per cubic foot": 16.0185,
                    "pound per cubic inch": 27679.9,
                    "ounce per cubic inch": 1729.99,
                    "gram per liter": 1,
                    "kilogram per liter": 1000
                },
                "specific_volume": {
                    "cubic meter per kilogram": 1,
                    "liter per kilogram": 0.001,
                    "cubic foot per pound": 0.062428,
                    "cubic inch per pound": 0.0005787,
                    "gallon per pound": 0.119826,
                    "milliliter per gram": 1
                },
                "moment_of_inertia": {
                    "kilogram square meter": 1,
                    "gram square centimeter": 1e-6,
                    "pound square foot": 0.04214,
                    "pound square inch": 0.00029264,
                    "ounce square inch": 0.00001829,
                    "slug square foot": 1.35582
                },
                "moment_of_force": {
                    "newton meter": 1,
                    "kilogram-force meter": 9.80665,
                    "pound-force foot": 1.35582,
                    "pound-force inch": 0.113,
                    "dyne centimeter": 0.0000001,
                    "ounce-force foot": 0.084738
                },
                "torque": {
                    "newton meter": 1,
                    "dyne centimeter": 0.0000001,
                    "kilogram-force meter": 9.80665,
                    "pound-force foot": 1.35582,
                    "ounce-force inch": 0.00706155,
                    "kilopond meter": 9.80665,
                    "gram-force centimeter": 0.00009807
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

    return render(request, "engineering/engineering_converter.html", context)