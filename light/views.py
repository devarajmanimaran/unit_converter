from django.shortcuts import render

def light_converter(request):
    context = {
        'conversion_type': 'luminance',  # Default to Length
        'value': '',
        'from_unit': '',
        'to_unit': '',
        'result': None
    }

    if request.method == "POST":
        context['value'] = request.POST.get("value", '')
        context['from_unit'] = request.POST.get("from_unit", '')
        context['to_unit'] = request.POST.get("to_unit", '')
        context['converter_type'] = request.POST.get("converter_type", 'luminance')

        try:
            value = float(context['value'])
            converter_type = context['converter_type']
            from_unit = context['from_unit']
            to_unit = context['to_unit']

            # All conversion factors and formulas
            conversions = {
                    "luminance": {
                        "candela per square meter": 1,
                        "foot-lambert": 3.426259
                    },
                    "luminous_intensity": {
                        "candela": 1,
                        "lumen per steradian": 1
                    },
                    "illumination": {
                        "lux": 1,
                        "foot-candle": 10.76391
                    },
                    "digital_image_resolution": {
                        "dpi": 1,
                        "ppcm": 2.54
                    },
                    "frequency_wavelength": {
                        "hertz": 1,
                        "nanometer": 299792458
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
                    context['result'] = round(result, 16)  # Round to 6 decimal places

        except (ValueError, KeyError, TypeError) as e:
            context['error'] = "Invalid conversion parameters"

    return render(request, "light/light_converter.html", context)