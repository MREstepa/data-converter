import xlrd
import math
import pandas as pd

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from shipping_rate import get_shipping_rate


def convert_name_phone(filename):
    "Convert Phone numbers and Lastnames"

    sheet_name = "raw_data"
    columns = ['phone_numbers','full_names']

    data = pd.read_excel (filename, sheet_name=sheet_name) 
    df = pd.DataFrame(data, columns=columns)

    phone_numbers = []
    last_names = []

    for rec in df.values:
        # for converting phone numbers
        num = '+63' + str(rec[0])
        if str(rec[0]).endswith('.0'): num = '+63' + str(rec[0])[:-2]
        phone_numbers.append(num)

        # for getting lastnames out of full names
        last_name = rec[1].split()[-1].capitalize()
        last_names.append(last_name)

    data = {
        'Phone Numbers': phone_numbers,
        'Last Names': last_names
    }
    output_file = "/converted-name_phone.xlsx"

    return data, output_file

def convert_cod(filename):
    "Calculate COD"

    sheet_name = "cod"
    columns = ['location','weight','parcel_value']

    data = pd.read_excel (filename, sheet_name=sheet_name) 
    df = pd.DataFrame(data, columns=columns)

    cods = []
    for rec in df.values:
        shipping_rate = 0
        location = str(rec[0])
        weight = float(rec[1])
        parcel_value = int(rec[2])

        shipping_rate = get_shipping_rate(location, weight)

        cod = math.ceil(( (shipping_rate * .027) + shipping_rate ) + ( (parcel_value / 500) * 5 ))
        cods.append(cod)

    data = {
        'COD': cods
    }
    output_file = "/converted-cod.xlsx"

    return data, output_file


if __name__ == '__main__':
    switch = int(input("(1) Phone Number & Lastname\n(2) COD\nSwitch >>> "))

    # get file name
    Tk().withdraw()
    filename = askopenfilename()

    # get destination (same folder location with the uploaded file)
    destination = ''.join(
        [str(elem) for elem in [ '/' + str(filename.split('/')[x])
        for x in range(len(filename.split('/'))-1)]]
    )[1:]

    if switch == 1: data, output_file = convert_name_phone(filename)
    if switch == 2: data, output_file = convert_cod(filename)

    converted = pd.DataFrame(data)

    converted.to_excel(destination + output_file)
    print("Converted Successfully!\nCreated file \"{}\"".format(output_file[1:]))
