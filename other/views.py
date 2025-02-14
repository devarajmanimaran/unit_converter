from django.shortcuts import render

def other_converter(request):
    context = {
        'conversion_type': 'prefixes',  # Default to Length
        'value': '',
        'from_unit': '',
        'to_unit': '',
        'result': None
    }

    if request.method == "POST":
        context['value'] = request.POST.get("value", '')
        context['from_unit'] = request.POST.get("from_unit", '')
        context['to_unit'] = request.POST.get("to_unit", '')
        context['converter_type'] = request.POST.get("converter_type", 'prefixes')

        try:
            value = float(context['value'])
            converter_type = context['converter_type']
            from_unit = context['from_unit']
            to_unit = context['to_unit']

            # All conversion factors and formulas
            conversions = {
                "prefixes": {
                    "kilo": 1000,
                    "mega": 1e6,
                    "giga": 1e9
                },
                "data_transfer": {
                    "bit per second": 1,
                    "kilobit per second": 1000,
                    "megabit per second": 1e6
                },
                "sound": {
                    "decibel": 1,
                    "neper": 8.68589
                },
                "typography": {
                    "point": 1,
                    "pica": 12
                },
                "volume_lumber": {
                    "cubic meter": 1,
                    "board foot": 0.00235974
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

    return render(request, "other/other_converter.html", context)