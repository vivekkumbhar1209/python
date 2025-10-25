# Write a python program using function to convert Celsius to Fahrenheit.

'''
If temperature = 0°C 
Formula 
F=(°C × 5 / 9)+32

'''

def celsius_to_Fahrenheit(celsius):
    fahrenheit = (celsius * 5/9) +32
    return fahrenheit

a = float(input("Enter a tempratue in celsius :"))
f = celsius_to_Fahrenheit(a)
print(f"temprature in fahrenheit :" ,f)