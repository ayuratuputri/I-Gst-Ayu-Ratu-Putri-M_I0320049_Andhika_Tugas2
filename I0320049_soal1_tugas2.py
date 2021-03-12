import math

#menampilkan informasi program
print("Luas persegi panjang  luas lingkaran  luas kubus")

#input nilai sisi
p = float(input("Masukkan nilai panjang: "))
l = float(input("Masukkan nilai lebar: "))

#input nilai jari-jari
r = float(input("Masukkan nilai jari-jari: "))

#input nilai sisi
s = float(input("Masukkan nilai sisi: "))

#menghitung luas persegi panjang
luas_persegi_panjang = p * l

#menghitung luas lingkaran
luas_lingkaran = 3.14 * (r ** 2)

#menghitung luas kubus
luas_kubus = 6 * (s ** 2)

#menampilkan hasil perhitungan kelayar
print("luas persegi panjang: ", luas_persegi_panjang)
print("luas lingkaran: ", luas_lingkaran)
print("luas kubus: ", luas_kubus)

#menampilkan informasi program

print("Konersi suhu (Celcius ke Farenheit)")

#input suhu dalam celcius
C = float(input("Masukkan suhu(celcius): "))

#melakukan konversi suhu ke farenheit
F = (9/5 * C) + 32

#menampilakan hasil konversi kelayar
print("Celcius: ", C)
print("Farenheit: ", F)

#menampilakan informasi program

print("Konversi suhu (Reamur ke Kelvin)")

#input suhu dalam reamur
R = float(input("Masukkan suhu(reamur): "))

#melakukan konversi suhu ke kelvin
K = (5/4 * R) + 273

#menampilkan hasil konversi kelayar
print("Reamur: ", R)
print("Kelvin: ", K)
