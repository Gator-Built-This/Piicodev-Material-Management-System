# Read from two RFID modules independently
from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms
import time
import math
import machine

#Intitalise the readers
readerA = PiicoDev_RFID(asw=[0,0])     # Initialise the first RFID module with both address switches OFF
readerB = PiicoDev_RFID(asw=[0,1])     # Initialise the second RFID module with the second address switch ON
readerC = PiicoDev_RFID(asw=[1,0])     # Initialise the third RFID module with the first address switch ON
readerD = PiicoDev_RFID(asw=[1,1])     # Initialise the fourth RFID module with both address switches ON

#intialising the basic RFID module function for read
rfid = PiicoDev_RFID()

def printTagDetails(brand, colour, material, weight):
    print(0*" " + 'Brand: ' + brand)            # print the Brand
    print(0*" " + 'Colour: ' + colour)# print the colour
    print(0*" " + 'Material: ' + material)# print the material
    print(0*" " + 'Weight: ' + weight)# print the weight (In future this will be a bit of math to take the current weight of the roll - (starting weight of the roll - 1000g)


#Start of code
print('Checking Slots\n')

#def slot1_callback(timer):  #Slot 1

while True:
    if readerA.tagPresent():              # if an RFID tag is present on reader A
        rawData = readerA.readText().split()             # get the id
        brand, colour, material, weight = rawData[:4]     # assign the elements in rawData into individual variables
        printTagDetails(brand, colour, material, weight)   # Call function to output tag details

    if readerB.tagPresent():              # if an RFID tag is present on reader B
        rawData = readerB.readText().split()             # get the id
        brand, colour, material, weight = rawData[:4]     # assign the elements in rawData into individual variables
        printTagDetails(brand, colour, material, weight)   # Call function to output tag details

    if readerC.tagPresent():              # if an RFID tag is present on reader C
        rawData = readerC.readText().split()             # get the id
        brand, colour, material, weight = rawData[:4]     # assign the elements in rawData into individual variables
        printTagDetails(brand, colour, material, weight)   # Call function to output tag details

    if readerD.tagPresent():              # if an RFID tag is present on reader D
        rawData = readerD.readText().split()             # get the id and split into a list
        brand, colour, material, weight = rawData[:4]     # assign the elements in rawData into individual variables
        printTagDetails(brand, colour, material, weight)   # Call function to output tag details

    sleep_ms(500)
