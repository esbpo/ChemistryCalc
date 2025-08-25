import funcLib as f
import inspect, re

to_m = {
    # Other SI variants
    'fm': 1e-15, # femtometer
    'pm': 1e-12, # picometer
    'nm': 1e-9, # nanometer
    'um': 1e-6, # micrometer
    'mm': 1e-3, # millimeter
    'cm': 1e-2, # centimeter
    'dm': 1e-1, # decimeter
    'm': 1, # meter
    'km': 1e3, # kilometer

    # Imperial units
    'in': 0.0254, # inch
    'ft': 0.3048, # foot
    'yd': 0.9144, # yard
    'mi': 1609.344, # mile
    'nmi': 1852, # nautical mile

    # Other units
    'pc': 3.085677581491367e16,  # parsec
    'ly': 9.4607e15,  # light-year
    'au': 149597870700,  # astronomical unit
}

to_g = {
    # Other SI variants
    'mg': 1e-3, # milligram
    'g': 1, # gram
    'kg': 1e3, # kilogram
    't': 1e6,  # tonne

    # Imperial units
    'oz': 28.34952, # ounce
    'lbs': 453.59237, # pound
    'st': 6350.29318,  # stone
    'ts': 907184.74,  # US short ton
    'tl': 1016046.91,  # UK long ton

    # Other units
    'grain': 0.06479891,  # grain
}

to_l = {
    # Other SI variants
    'ul': 1e-6, # microliter
    'ml': 1e-3, # milliliter
    'cl': 1e-2, # centiliter
    'dl': 1e-1, # deciliter
    'l': 1, # liter
    'hl': 1e2, # hectoliter
    'kl': 1e3, # kiloliter

    # Imperial units
    'fl_oz': 0.02957353, # fluid ounce
    'pt': 0.4731765, # US pint
    'qt': 946.353, # quart
    'gal': 3.78541, # US gallon

    # Other units
    'm3': 1e3,  # cubic meter
    'm^3': 1e3,  # cubic meter (alternative notation)
    'ft3': 28.316846592,  # cubic foot
    'ft^3': 28.316846592,  # cubic foot (alternative notation)
    'in3': 0.016387064,  # cubic inch
    'in^3': 0.016387064,  # cubic inch (alternative notation)
}

to_s = {
    'ps': 1e-12, # picosecond
    'ns': 1e-9, # nanosecond
    'us': 1e-6, # microsecond
    'ms': 1e-3, # milisecond
    's': 1, # second
    'min': 60, # minute
    'h': 3600, # hour
    'd': 86400, # day
}

si_units = {
    'm': to_m, # meters
    'g': to_g, # grams
    'l': to_l, # liters
    's': to_s, # seconds
}

desc_m = {
    'fm': "femtometer",
    'pm': "picometer",
    'nm': "nanometer",
    'um': "micrometer",
    'mm': "millimeter",
    'cm': "centimeter",
    'dm': "decimeter",
    'm': "meter",
    'km': "kilometer",
    'in': "inch",
    'ft': "foot",
    'yd': "yard",
    'mi': "mile",
    'nmi': "nautical mile",
    'pc': "parsec",
    'ly': "light-year",
    'au': "astronomical unit",
}

desc_g = {
    'mg': "milligram",
    'g': "gram",
    'kg': "kilogram",
    't': "tonne",
    'oz': "ounce",
    'lbs': "pound",
    'st': "stone",
    'ts': "US short ton",
    'tl': "UK long ton",
    'grain': "grain",
}

desc_l = {
    'ul': "microliter",
    'ml': "milliliter",
    'cl': "centiliter",
    'dl': "deciliter",
    'l': "liter",
    'hl': "hectoliter",
    'kl': "kiloliter",
    'fl_oz': "fluid ounce",
    'pt': "US pint",
    'qt': "quart",
    'gal': "US gallon",
    'm3': "cubic meter",
    'm^3': "cubic meter (alternative notation)",
    'ft3': "cubic foot",
    'ft^3': "cubic foot (alternative notation)",
    'in3': "cubic inch",
    'in^3': "cubic inch (alternative notation)",
}

desc_s = {
    'ps': "picosecond",
    'ns': "nanosecond",
    'us': "microsecond",
    'ms': "millisecond",
    's': "second",
    'min': "minute",
    'h': "hour",
    'd': "day",
}

categories = {
    "Length": desc_m,
    "Mass": desc_g,
    "Volume": desc_l,
    "Time": desc_s,
}

def printUnits():
    output = ["Available units for the convert command:"]
    for category, units in categories.items():
        output.append(f"\n-- {category} --")
        for k, v in units.items():
            output.append(f"'{k}': {v}")

    print("\n".join(output))

def convert_to_si(value, unit):
    if unit in si_units['g']:
        return (value * si_units['g'][unit], 'g')
    elif unit in si_units['m']:
        return (value * si_units['m'][unit], 'm')
    elif unit in si_units['l']:
        return (value * si_units['l'][unit], 'l')
    elif unit in si_units['s']:
        return (value * si_units['s'][unit], 's')
    else:
        return False