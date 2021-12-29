#program for convert celcius to fahnrenheit, Reamur, Kelvin
#C = ((C*4/5)+5 R
#C = (C*9/5)+32 F
#C = ((C*5)/5)+237 K

C = float(input("Input Celcius : "))
hasilF = ((C*9)/5)+32
hasilR = ((C*4)/5)+0
hasilK = ((C*5)/5)+273

print(C,"derajat Celcius", '=', hasilF, "deraja Fahrenheit")
print(C,"derajat Celcius", '=', hasilR, "derajat Reamur ")
print(C,"derajat Celcius", '=', hasilK, "derajat Kelvin")
