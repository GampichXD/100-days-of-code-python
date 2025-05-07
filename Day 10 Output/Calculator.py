# Calculator
from art import logo
import random
logos = random.choice(logo)
print(logos)
print("Selamat Datang di Program Kalkulator Sederhana!")

# TODO: Write out the 4 functions - add, subtract, multiply, and divide

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

def modulo(n1, n2):
    return n1 % n2

def floor_division(n1, n2):
    return n1 // n2

# TODO: Add these 4 functions to a dictionary as the value, Key is the operation symbol
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    '%': modulo,
    '//': floor_division
}

# TODO: Use the dictionary to perform the calculation. Multiply 4 by 8 using the dictionary.
# result = operations['*'](4, 8)
# print(result)

def calculator(nm1, nm2, op):
    calculation_function = operations[op]
    result = calculation_function(nm1, nm2)
    print(f"{nm1} {op} {nm2} = {result}")
    next_calculation = input("Ketik 'y' untuk melanjutkan menghitung dengan hasil sebelumnya dan tekan 'n' untuk menghitung dengan angka baru : ")
    if next_calculation == "y":
        input_calculator(result, nm2, op)
    else:
        new_calculation = input("Apakah ingin melanjutkan program kalkulator? (y/n) : ")
        if new_calculation == "y":
            input_calculator(None, None, None)
            print("\n" * 20)
        else:
            print("Hasil Perhitungan Terakhir kamu: ", result)
            print("Terima Kasih telah menggunakan program kalkulator sederhana ini!")
            return result


def input_calculator(nm1=None, nm2=None, op=None):
    if nm1 == None:
        nm1 = float(input("Masukkan angka pertama: "))
    op = input("Masukkan operator \n+ untuk penjumlahan \n- untuk pengurangan \n* untuk perkalian \n/ untuk pembagian \n** untuk perpangkatan \n% 'untuk modulo \n// untuk pembagian bulat \n= ")
    nm2 = float(input("Masukkan angka kedua: "))
    return calculator(nm1, nm2, op)

perhitungan = input_calculator()


