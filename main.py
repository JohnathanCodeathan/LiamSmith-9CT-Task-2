#Imports:
from machine import Pin, ADC
import math
import time
import threading 
import LilBirdy
from LilBirdy import Neopixel
import BiggestBird #Lil birdy, neopixel and biggest bird are functions for lorikeet, and the functions are located inside of the pico itself. I learnt how to operate this from 
import sys #Mainly for stopping everything if the program doesnt want to coorperate respectfully
'''Threading: Useful for running multiple functions SIMULTANEOUSLY
Used to run button, sensor, lights, and buzzer functions at the same time.
Source of Idea: Inbound Shovel (youtuber who is making a game on godot): https://youtu.be/44hfu7ELgVc?si=elyH6TVTryo967hW
Implementation: Python Docs: https://docs.python.org/3/library/threading.html'''

#Variables/prerequisites
JohnButton = Pin(16, Pin.IN, Pin.PULL_DOWN)# Left Button
JaneButton = Pin(17, Pin.IN, Pin.PULL_DOWN) # Right Button
PotentialMan = ADC(Pin(22)) #Potentiometer
manypickles = 5
pickles = Neopixel(manypickles, 0, 28, "GRB") #Set up for lorikeet
MAHORAGA = 1.0 #Analog value of potentiometer
Fin = False #If Level is finished
score = 0
rebt = (254, 0, 2)
mellow = (255, 239, 1)
suspicoussalmon = (252, 137, 119)
geen = (155, 253, 113)
ourple = (139, 18, 105)
MaxScore = 100
Songid = 5 
'''Song Levels:
- 0 = Raise up your bat by Toby Fox (Deltarune)
- 1 = Don't by Locus Juice, Azumi Takahashi and Atlus Sound Team (Persona 3 Reload)
- 2 = Flower Man by Toby Fox and Cammelia (Deltarune)
- 3 = Specialist by Atlus Sound Team (Persona 4)
- 4 = Tian Tian by Mili (Limbus Company)'''
Conv = 182.05 #Converts analog to angle, good for potentiometer


#Functions:

def Menu():
    pickles.brightness(0)
    while JohnButton.value() == 0 and JaneButton.value() == 0:
        MAHORAGA = PotentialMan.read_u16() #Checks potentiometer until button is not pressed
        SongId = math.floor((MAHORAGA/Conv)/72) #SongId is set to rounded down version of Mahoraga if it was in angular degrees
        if SongId == 0: #If you look at the markdown, the songid isn't in the while statement and the if statement is non-existent,  but this is because I would like the lights on the controller to light up as you move the potentiometer
            pass
            #Lorikeet shenanigans i will be doing today
'''How Menu works: 
Repeated until any button is pressed:
- Sets variable called mahoraga to get the analog input of the potentiometer
- Sets a variable called SongId to Mahoraga, converted to angular degrees, divided by 5, rounded down
- Lights up a different coloured light on the lorikeet for UX'''

def Song():
    global Fin
    Fin = False
    #Setting Up Threads
    InsulatedClothing = threading.Thread(target= Sound, args=Songid)
    HeadLamp = threading.Thread(target=LIGHTS)
    CameraCover = threading.Thread(target=CAMERA)
    SewingMachine = threading.Thread(target=ACTION)
    #Starting Threads
    InsulatedClothing.start()
    HeadLamp.start()
    CameraCover.start()
    SewingMachine.start()
    #Waiting for threads
    InsulatedClothing.join()
    HeadLamp.join()
    Fin = True
    print(f"Your score is {score}/{MaxScore}!")
    while True:
        if JohnButton.value() == 1 or JaneButton.value() ==1:
            break
'''How Song Works:
-Sets Fin to False and Global because it is important to reset it and let song change Fin
-Sets up all the threads and starts them
-Waits for light and buzzer threads to finish
-Sets Fin to true, letting sensor and button know to stop sensing
-Displays score, not necessary but I thought it would be cool
-Waits for button input before sending user back to menu'''

def Sound():
    pass

def LIGHTS():
    pass

def CAMERA(): #Sensor
    pass

def ACTION(): #Button
    pass

def WORSELIGHTS(): #Corner Lights
    pass




#Main Stuff:
while True:
    Menu()
    Song()
''' How this works:
Just a while loop that runs the menu and then the song. Not much else'''