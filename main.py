import re
import cv2
import easyocr
reader = easyocr.Reader(['en'])

def get_depth_value(input_string):
  count = input_string.count('x')
  if count >= 1:
    match = re.search(r'x\s*([\d.]+)', input_string)
    result = match.group(1)
    return result
  match = re.search(r'[\d.]+', input_string)
  result = match.group(0)
  return result

def get_height_value(input_string):
  count = input_string.count('x')
  if count >= 2:
    match = re.search(r'x\s*([\d.]+)(?!.*x)', input_string)
    result = match.group(1)
    return result
  elif count == 1:
    match = re.search(r'x\s*([\d.]+)', input_string)
    result = match.group(1)
    return result
  match = re.search(r'[\d.]+', input_string)
  result = match.group(0)
  return result

def get_value(input_string):
  match = re.search(r'[\d.]+', input_string)
  result = match.group(0)
  return result

def get_wattage(string_list):
    # Define the mapping of alternative units to standard units
    unit_conversion = {
        "kilowatt": "kilowatt",  
        "kw": "kilowatt",         
        "watt": "watt",     
        "w": "watt",
        "watts":"watt",
        "kilowatts":"kilowatt"
    }

    # Define the regex to match dimensions with the alternative units
    units = "|".join(unit_conversion.keys())
    pattern = re.compile(r'(\d+\.?\d*)\s*(' + units + r')\b', re.IGNORECASE)
    
    # Traverse the list of strings in reverse order
    for text in reversed(string_list):
        # Find all matches in the string
        matches = list(pattern.finditer(text))
        
        # If we found matches, return the last match from this string
        if matches:
            last_match = matches[-1]
            dimension = last_match.group(0)  # The full dimension (e.g., "3 metres")
            unit = last_match.group(2).lower()  # Extract and standardize the unit
            
            # Convert the unit if it is in the mapping
            standardized_unit = unit_conversion.get(unit, unit)
            
            # Replace the unit in the dimension with the standardized unit
            standardized_dimension = last_match.group(1) + " " + standardized_unit
            
            return standardized_dimension
    
    return " "

def get_voltage(string_list):
    # Define the mapping of alternative units to standard units
    unit_conversion = {
        "millivolt": "millivolt",   
        "mv": "millivolt",            
        "kilovolt": "kilovolt",       
        "kv": "kilovolt",              
        "volt": "volt",     
        "v": "volt",
        "volts":"volt",
        "kilovolts":"kilovolt",
        "millivolts":"millivolt"
    }

    # Define the regex to match dimensions with the alternative units
    units = "|".join(unit_conversion.keys())
    pattern = re.compile(r'(\d+\.?\d*)\s*(' + units + r')\b', re.IGNORECASE)
    
    # Traverse the list of strings in reverse order
    for text in reversed(string_list):
        # Find all matches in the string
        matches = list(pattern.finditer(text))
        
        # If we found matches, return the last match from this string
        if matches:
            last_match = matches[-1]
            dimension = last_match.group(0)  # The full dimension (e.g., "3 metres")
            unit = last_match.group(2).lower()  # Extract and standardize the unit
            
            # Convert the unit if it is in the mapping
            standardized_unit = unit_conversion.get(unit, unit)
            
            # Replace the unit in the dimension with the standardized unit
            standardized_dimension = last_match.group(1) + " " + standardized_unit
            
            return standardized_dimension
    
    return " "

def get_weight(string_list, item_val):
    # Define the mapping of alternative units to standard units
    unit_conversion = {
        "mg":"milligram",
        "milligrams":"milligram",
        "milligram":"milligram",
        "kg":"kilogram",
        "kilogram":"kilogram",
        "Kg":"kilogram",
        "kilograms":"kilogram",
        "mcg":"microgram",
        "microgram":"microgram",
        "micrograms":"microgram",
        "gm":"gram",
        "grams":"gram",
        "g":"gram",
        "ounce":"ounce",
        "ounces":"ounce",
        "ton":"ton",
        "tons":"ton",
        "pound":"pound",
        "pounds":"pound",
        "lb":"pound",
        "tonne": "ton", 
        "t": "ton",
        "oz":"ounce"
    }

    # Define the regex to match dimensions with the alternative units
    units = "|".join(unit_conversion.keys())
    pattern = re.compile(r'(\d+\.?\d*)\s*(' + units + r')\b', re.IGNORECASE)
    
    # Traverse the list of strings in reverse order
    for text in reversed(string_list):
        # Find all matches in the string
        matches = list(pattern.finditer(text))
        
        # If we found matches, return the last match from this string
        if matches:
            last_match = matches[-1]
            input_string = text
            if item_val == 'width':
                value = get_value(input_string)
            elif item_val == 'depth':
                value = get_depth_value(input_string)
            else:
                value = get_height_value(input_string)
            
            unit = last_match.group(2).lower()  # Extract and standardize the unit
            
            # Convert the unit if it is in the mapping
            standardized_unit = unit_conversion.get(unit, unit)
            
            # Replace the unit in the dimension with the standardized unit
            standardized_dimension = value + " " + standardized_unit
            
            return standardized_dimension
    
    return " "

def get_dimension(string_list):
    # Define the mapping of alternative units to standard units
    unit_conversion = {
        "cm": "centimetre",
        "centimetre": "centimetre",
        "foot": "foot",
        "feet": "foot",
        "millimetre": "millimetre",
        "mm": "millimetre",
        "metre": "metre",
        "meter": "metre",
        "m": "metre",
        "inch": "inch",
        "inches": "inch",
        "in": "inch",
        "yard": "yard",
        "yards": "yard"
    }

    # Define the regex to match dimensions with the alternative units
    units = "|".join(unit_conversion.keys())
    pattern = re.compile(r'(\d+\.?\d*)\s*(' + units + r')\b', re.IGNORECASE)
    
    # Traverse the list of strings in reverse order
    for text in reversed(string_list):
        # Find all matches in the string
        matches = list(pattern.finditer(text))
        
        # If we found matches, return the last match from this string
        if matches:
            last_match = matches[-1]
            dimension = last_match.group(0)  # The full dimension (e.g., "3 metres")
            unit = last_match.group(2).lower()  # Extract and standardize the unit
            
            # Convert the unit if it is in the mapping
            standardized_unit = unit_conversion.get(unit, unit)
            
            # Replace the unit in the dimension with the standardized unit
            standardized_dimension = last_match.group(1) + " " + standardized_unit
            
            return standardized_dimension
    
    return " "

import re

def get_volume(string_list):
    # Define the mapping of alternative units to standard units
    unit_conversion = {
        "cubic foot": "cubic foot",
        "cubic feet": "cubic foot",    # Plural form
        "cu ft": "cubic foot",         # Abbreviation
        "cu feet": "cubic foot",       # Abbreviation with plural
        "microlitre": "microlitre",
        "microlitres": "microlitre",   # Plural form
        "µl": "microlitre",            # Abbreviation
        "microliters": "microlitre",   # US spelling plural
        "cup": "cup",
        "cups": "cup",                 # Plural form
        "fluid ounce": "fluid ounce",
        "fluid ounces": "fluid ounce", # Plural form
        "fl oz": "fluid ounce",        # Abbreviation
        "fl ounces": "fluid ounce",    # Abbreviation with plural
        "centilitre": "centilitre",
        "centilitres": "centilitre",   # Plural form
        "cl": "centilitre",            # Abbreviation
        "centiliters": "centilitre",   # US spelling plural
        "imperial gallon": "imperial gallon",
        "imperial gallons": "imperial gallon", # Plural form
        "pint": "pint",
        "pints": "pint",               # Plural form
        "decilitre": "decilitre",
        "decilitres": "decilitre",     # Plural form
        "dl": "decilitre",             # Abbreviation
        "deciliters": "decilitre",     # US spelling plural
        "litre": "litre",
        "litres": "litre",             # Plural form
        "liter": "litre",              # US spelling
        "liters": "litre",             # US spelling plural
        "l": "litre",                  # Abbreviation
        "millilitre": "millilitre",
        "millilitres": "millilitre",   # Plural form
        "ml": "millilitre",            # Abbreviation
        "milliliters": "millilitre",   # US spelling plural
        "quart": "quart",
        "quarts": "quart",             # Plural form
        "cubic inch": "cubic inch",
        "cubic inches": "cubic inch",  # Plural form
        "cu in": "cubic inch",         # Abbreviation
        "cu inches": "cubic inch",     # Abbreviation with plural
        "gallon": "gallon",            # US gallon
        "gallons": "gallon",           # Plural form
        "gal": "gallon"                # Abbreviation
    }


    # Define the regex to match dimensions with the alternative units
    units = "|".join(unit_conversion.keys())
    pattern = re.compile(r'(\d+\.?\d*)\s*(' + units + r')\b', re.IGNORECASE)
    
    # Traverse the list of strings in reverse order
    for text in reversed(string_list):
        # Find all matches in the string
        matches = list(pattern.finditer(text))
        
        # If we found matches, return the last match from this string
        if matches:
            last_match = matches[-1]
            dimension = last_match.group(0)# The full dimension (e.g., "3 metres")
            unit = last_match.group(2).lower()  # Extract and standardize the unit
            
            # Convert the unit if it is in the mapping
            standardized_unit = unit_conversion.get(unit, unit)
            
            # Replace the unit in the dimension with the standardized unit
            standardized_dimension = last_match.group(1) + " " + standardized_unit
            
            return standardized_dimension
    
    return " "

def preprocess_and_convert_image(image_path):
    img = cv2.imread(image_path)
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    results = reader.readtext(grayscale_img)
    input_text = []
    for result in results:
        input_text.append(result[1])
    return input_text