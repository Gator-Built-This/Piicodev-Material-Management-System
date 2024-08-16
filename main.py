# Read from two RFID modules independently
from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms

#Intitalise the readers
readerA = PiicoDev_RFID(asw=[0,0])     # Initialise the first RFID module with both address switches OFF
readerB = PiicoDev_RFID(asw=[0,1])     # Initialise the second RFID module with the second address switch ON
readerC = PiicoDev_RFID(asw=[1,0])     # Initialise the third RFID module with the first address switch ON
readerD = PiicoDev_RFID(asw=[1,1])     # Initialise the fourth RFID module with both address switches ON

#intialising the basic RFID module function for read
rfid = PiicoDev_RFID()

#Start of code
print('Checking Slots')
print('')

while True: 
    if readerA.tagPresent():              # if an RFID tag is present on reader A
        A = readerA.readText()             # get the id
        a = A.split()
        brandA = a.pop(0)
        colourA = a.pop(0)
        materialA = a.pop(0)
        weightA = a.pop(0)
        print(0*" " + 'Brand: ' + brandA)            # print the Brand
        print(0*" " + 'Colour: ' + colourA)			# print the colour
        print(0*" " + 'Material: ' + materialA)		# print the material
        print(0*" " + 'Weight: ' + weightA)			# print the weight (In future this will be a bit of math to take the current weight of the roll - (starting weight of the roll - 1000g)      
   
    if readerB.tagPresent():              # if an RFID tag is present on reader B
        B = readerB.readText()             # get the id
        b = B.split()
        brandB = b.pop(0)
        colourB = b.pop(0)
        materialB = b.pop(0)
        weightB = b.pop(0)
        print(10*" " + 'Brand: ' + brandB)            # print the Brand
        print(10*" " + 'Colour: ' + colourB)			# print the colour
        print(10*" " + 'Material: ' + materialB)		# print the material
        print(10*" " + 'Weight: ' + weightB)			# print the weight (In future this will be a bit of math to take the current weight of the roll - (starting weight of the roll - 1000g) 
    
    if readerC.tagPresent():              # if an RFID tag is present on reader C
        C = readerC.readText()             # get the id
        c = C.split()
        brandC = c.pop(0)
        colourC = c.pop(0)
        materialC = c.pop(0)
        weightC = c.pop(0)
        print(20*" " + 'Brand: ' + brandC)            # print the Brand
        print(20*" " + 'Colour: ' + colourC)			# print the colour
        print(20*" " + 'Material: ' + materialC)		# print the material
        print(20*" " + 'Weight: ' + weightC)			# print the weight (In future this will be a bit of math to take the current weight of the roll - (starting weight of the roll - 1000g)

    if readerD.tagPresent():              # if an RFID tag is present on reader D
        D = readerD.readText()             # get the id
        d = D.split()
        brandD = d.pop(0)
        colourD = d.pop(0)
        materialD = d.pop(0)
        weightD = d.pop(0)
        print(30*" " + 'Brand: ' + brandD)            # print the Brand
        print(30*" " + 'Colour: ' + colourD)			# print the colour
        print(30*" " + 'Material: ' + materialD)		# print the material
        print(30*" " + 'Weight: ' + weightD)			# print the weight (In future this will be a bit of math to take the current weight of the roll - (starting weight of the roll - 1000g)
    
    sleep_ms(500)
