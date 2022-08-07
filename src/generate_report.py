def output():
    return ''

def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank} l
    External tank: {external_tank} l
    Hydrogen tank: {hydrogen_tank} l"""


generate_report(80,70,75)    
print (generate_report)

