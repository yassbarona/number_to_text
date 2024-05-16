from utils.constants import *

def thousands(n):
    thousand, remainder = divmod(n, 1000)
    if thousand == 1:
        thousand_text = "mille"
    else:
        thousand_text = number_to_french(thousand) + "-mille"
    
    if remainder == 0:
        return thousand_text
    else:
        return thousand_text + "-" + number_to_french(remainder)

def hundreds(n):
    hundred, remainder = divmod(n, 100)
    if hundred == 1:
        hundred_text = "cent"
    else:
        hundred_text = number_to_french(hundred) + "-cents" if remainder == 0 else number_to_french(hundred) + "-cent"
    
    if remainder == 0:
        return hundred_text
    else:
        return hundred_text + "-" + number_to_french(remainder)

def from_70_to_99(n):
    if n < 80:  # rule for 70 to 79 (60 + x)
        return "soixante-" + number_to_french(n - 60)
    else:  # rule for 80 to 99 (80 + x)
        return "quatre-vingt-" + number_to_french(n - 80)

def below_70(n):
    ten, unit = divmod(n, 10)  # divmod gives me the result of the floor division and the remainder
    if unit == 1:
        return TENS[ten] + "-et-un"  # rule for tens finishing with 1
    elif unit > 0:
        return TENS[ten] + "-" + number_to_french(unit)
    else:
        return TENS[ten]  # uses the tens list to get the number

def number_to_french(n):
    if n < 17:
        return UNITS[n]  # these are the units without any rule
    elif n < 20:
        return "dix-" + UNITS[n - 10]  # this is the rule for 17, 18, 19 (e.g. 10+7)
    elif n < 70:
        return below_70(n)
    elif n < 100:
        return from_70_to_99(n)
    elif n < 1000:
        return hundreds(n)
    else:
        return thousands(n)
