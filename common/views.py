from django.shortcuts import render

def common_converter(request):
    context = {
        'conversion_type': 'length',  # Default to Length
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
                "length": {
                    "meter": 1,
                    "kilometer": 1000,
                    "centimeter": 0.01,
                    "millimeter": 0.001,
                    "mile": 1609.34,
                    "inch": 0.0254,
                    "foot": 0.3048,
                    "yard": 0.9144,
                    "nautical mile": 1852
                },
                "weight": {
                    "kilogram": 1,
                    "gram": 0.001,
                    "milligram": 0.000001,
                    "pound": 0.453592,
                    "ounce": 0.0283495,
                    "ton (metric)": 1000,
                    "ton (imperial)": 1016.05
                },
                "volume": {
                    "liter": 1,
                    "milliliter": 0.001,
                    "cubic meter": 1000,
                    "gallon": 3.78541,
                    "pint": 0.473176,
                    "quart": 0.946353,
                    "cubic centimeter": 0.001,
                    "cubic inch": 0.0163871
                },
                "temperature": lambda v, f, t: {
                    ("celsius", "fahrenheit"): v * 9/5 + 32,
                    ("fahrenheit", "celsius"): (v - 32) * 5/9,
                    ("celsius", "kelvin"): v + 273.15,
                    ("kelvin", "celsius"): v - 273.15,
                    ("fahrenheit", "kelvin"): (v - 32) * 5/9 + 273.15,
                    ("kelvin", "fahrenheit"): (v - 273.15) * 9/5 + 32,
                    ("celsius", "rankine"): (v + 273.15) * 9/5,
                    ("rankine", "celsius"): (v - 491.67) * 5/9
                }.get((f, t), v),
                "area": {
                    "square meter": 1,
                    "square kilometer": 1000000,
                    "acre": 4046.86,
                    "square foot": 0.092903,
                    "square inch": 0.00064516,
                    "hectare": 10000,
                    "square mile": 2589988.11
                },
                "pressure": {
                    "pascal": 1,
                    "bar": 100000,
                    "psi": 6894.76,
                    "torr": 133.322,
                    "atmosphere": 101325
                },
                "energy": {
                    "joule": 1,
                    "calorie": 4.184,
                    "kilowatt-hour": 3600000,
                    "electronvolt": 1.60218e-19,
                    "BTU": 1055.06
                },
                "power": {
                    "watt": 1,
                    "kilowatt": 1000,
                    "horsepower": 745.7,
                    "megawatt": 1000000,
                    "gigawatt": 1e9
                },
                "force": {
                    "newton": 1,
                    "dyne": 0.00001,
                    "pound-force": 4.44822,
                    "kilonewton": 1000
                },
                "time": {
                    "second": 1,
                    "minute": 60,
                    "hour": 3600,
                    "day": 86400,
                    "week": 604800,
                    "month": 2.628e6,
                    "year": 3.154e7,
                    "millisecond": 0.001,
                    "microsecond": 1e-6
                },
                "speed": {
                    "meter per second": 1,
                    "kilometer per hour": 0.277778,
                    "miles per hour": 0.44704,
                    "knot": 0.514444,
                    "feet per second": 0.3048
                },
                "angle": {
                    "degree": 1,
                    "radian": 57.2958,
                    "gradian": 0.9,
                    "minute of arc": 1/60,
                    "second of arc": 1/3600
                },
                "fuel": {
                    "kilometers per liter": 1,
                    "miles per gallon": 0.425144,
                    "liters per 100 kilometers": 100
                },
                "data": {
                    "bit": 1,
                    "byte": 8,
                    "kilobyte": 8192,
                    "megabyte": 8388608,
                    "gigabyte": 8.59e9,
                    "terabyte": 8.8e12,
                    "petabyte": 9.007e15
                },
                "volume_dry": {
                    "bushel": 35.2391,
                    "cubic foot": 28.3168,
                    "cubic yard": 764.555,
                    "peck": 8.80977,
                    "dry gallon": 4.40488
                },
                "numbers": lambda v, f, t: {
                    ("decimal", "binary"): bin(int(v))[2:],
                    ("decimal", "hexadecimal"): hex(int(v))[2:].upper(),
                    ("decimal", "octal"): oct(int(v))[2:],
                    ("binary", "decimal"): str(int(str(int(v)), 2)),
                    ("binary", "hexadecimal"): hex(int(str(int(v)), 2))[2:].upper(),
                    ("binary", "octal"): oct(int(str(int(v)), 2))[2:],
                    ("hexadecimal", "decimal"): str(int(str(v), 16)),
                    ("hexadecimal", "binary"): bin(int(str(v), 16))[2:],
                    ("hexadecimal", "octal"): oct(int(str(v), 16))[2:],
                    ("octal", "decimal"): str(int(str(v), 8)),
                    ("octal", "binary"): bin(int(str(v), 8))[2:],
                    ("octal", "hexadecimal"): hex(int(str(v), 8))[2:].upper()
                }.get((f, t), v)
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

    return render(request, "common/common_converter.html", context)