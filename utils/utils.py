from utils.constants import *

def thousands(n):
    thousand, remainder = divmod(n, 1000)
    if remainder == 0:
        if thousand == 1:
            return "mille"
        else:
            return UNITS[thousand] + "-milles" #rule for plurals
    else:
        if thousand == 1:
            return "mille-" + number_to_french(remainder)
        else:
            return UNITS[thousand] + "-mille-" + number_to_french(remainder)

def hundreds(n):
    hundred, remainder = divmod(n, 100)
    if remainder == 0:
        if hundred == 1:
            return "cent"
        else:
            return UNITS[hundred] + "-cents" #rule for plurals
    else:
        if hundred == 1:
            return "cent-" + number_to_french(remainder)
        else:
            return UNITS[hundred] + "-cent-" + number_to_french(remainder)

def from_70_to_99(n):
    if n < 80: # rule for 60 and 80. e.g 60 + 12
        return "soixante-" + number_to_french(n - 60)
    else:
        return "quatre-vingt-" + number_to_french(n - 80)

def below_70(n):
    ten, unit = divmod(n, 10) # divmod makes give me the result of the floor division and the reminder
    if unit == 1:
        return TENS[ten] + "-et-un" # rule for tens finishing with 1
    elif unit > 0:
        return TENS[ten] + "-" + number_to_french(unit)
        
    else:
        return TENS[ten] # uses the tens list to get the number

def number_to_french(n):
    if n < 17:
        return UNITS[n] # these are the units without any rule
    elif n < 20:
        return "dix-" + UNITS[n - 10] # this is the rule for 17,18,19 (e.g. 10+7)
    elif n < 70:
        below_70(n)
    elif n < 100:
        from_70_to_99(n)
    elif n < 1000:
        hundreds(n)
    else:
        thousands(n)