#Imports:
from machine import Pin, ADC, PWM
import math
import uasyncio as uas
'''So I realised threading doesn't work, with the help of google gemini.
Then I did some more research and found uasyncio for micropython, which does the same thing, but instead of using multiple threads, which the pico doesn't have, all the background processes share one.
Source: https://docs.micropython.org/en/v1.14/library/uasyncio.html'''
import threading 
import time
import LilBirdy
from LilBirdy import Neopixel#Lil birdy, neopixel and biggest bird are functions for lorikeet, and the functions are located inside of the pico itself. I learnt how to operate this from 
import sys #Mainly for stopping everything if the program doesnt want to coorperate respectfully

#Variables/prerequisites
JohnButton = Pin(16, Pin.IN, Pin.PULL_UP)# Left Button
JaneButton = Pin(17, Pin.IN, Pin.PULL_UP) # Right Button
PotentialMan = ADC(Pin(26)) #Potentiometer
HATE = PWM(Pin(18)) #Buzzer
    #Lights
JohnMellow = Pin(10, Pin.OUT)
JohnRebt = Pin(11, Pin.OUT)
JohnGeen = Pin(9, Pin.OUT)
JaneMellow = Pin(13, Pin.OUT)
JaneRebt = Pin(14, Pin.OUT)
JaneGeen = Pin(12, Pin.OUT)
mod = 0.0
manypickles = 5#Also setup for lorikeet
pickles = Neopixel(manypickles, 0, 28, "GRB") #Set up for lorikeet
Fin = False #If Level is finished
Johntiming = [] #Refers to the eligibility in scoring for the lights on John Buttons side
Janetiming = [] #Refers to the eligibility in scoring for the lights on Jane Buttons side
#John and Jane timing are now lists because in the current order of the Lights function, it would set the timing variables to that of a red light. But if we append it all to a list, and select the biggest one. (Order is non-negotiable, refer to comment in lights function)
corner = 0 #Tells corner lights what value to be 
Johnreleased = False #Checks if the left button is released
Janereleased = False#Checks if right button is released
JohnKneaded = False #Is a note in the left side needed
JaneKneaded = False #Is a note in the right side needed
    #RGB codes for colours
rebt = (254, 0, 2) #Red
mellow = (255, 239, 1) #Yellow
suspicoussalmon = (252, 137, 119) #Salmon
geen = (155, 253, 113) #Green
ourple = (139, 18, 105) #Purple
score = 0
MaxScore = 100
SongId = 5 
'''Song Levels:
- 0 = Raise up your bat by Toby Fox (Deltarune)
- 1 = Don't by Locus Juice, Azumi Takahashi and Atlus Sound Team (Persona 3 Reload)
- 2 = Flower Man by Toby Fox and Cammelia (Deltarune)
- 3 = Specialist by Atlus Sound Team (Persona 4)
- 4 = Tian Tian by Mili (Limbus Company)'''
Conv = 182.05 #Converts analog to angle, good for potentiometer
 #Notes:
A2 = 110
B2 =123
b5 = 988
g5 = 784
e6 = 1318
c6 = 1047
d3 = 147
f6 = 1397
b4 = 494
a3 = 220
B1 = 62
e5 = 659
c4 = 262
C3 = 131
f5 = 698
a4 = 440
d6 = 1175
d5 = 587
a5 = 880
e3 = 165
d2 = 73

#Functions:

def Menu():
    global SongId
    pickles.brightness(0)
    print("Menu is being ran")
    while True:
        MAHORAGA = PotentialMan.read_u16() #Checks potentiometer until button is not pressed
        SongId = math.floor((MAHORAGA/Conv)/72) #SongId is set to rounded down version of Mahoraga if it was in angular degrees
        pickles.brightness(50)
        if SongId == 0: #If you look at the markdown, the songid isn't in the while statement and the if statement is non-existent,  but this is because I would like the lights on the controller to light up as you move the potentiometer
            pickles.fill(ourple)
        elif SongId == 1:
            pickles.fill(rebt)
        elif SongId == 2:
            pickles.fill(geen)
        elif SongId == 3:
            pickles.fill(mellow)
        elif SongId == 4 or SongId == 5:
            pickles.fill(suspicoussalmon) #Lorikeet shenanigans i have completed today
        else:
            sys.exit("The dev did some math wrong this isn't supposed to happen")
        if JohnButton.value() == 0 or JaneButton.value() == 0:
            break
        pickles.show()
        time.sleep(0.1)
'''How Menu works: 
Repeated until any button is pressed:
- Sets variable called mahoraga to get the analog input of the potentiometer
- Sets a variable called SongId to Mahoraga, converted to angular degrees, divided by 5, rounded down
- Lights up a different coloured light on the lorikeet for UX'''

def Song():
    global Fin
    global MaxScore
    print("Song is being ran")
    Fin = False
    pickles.brightness(0)
    uas.run(main())
    uas.wait_for(Sound, 120)
    Fin = True
    print(f"Your score is {score}/{MaxScore}!")
    while True:
        if JohnButton.value() == 1 or JaneButton.value() == 1:
            break
'''How Song Works:
-Sets Fin to False and Global because it is important to reset it and let song change Fin
-Sets up all the threads and starts them
-Waits for light and buzzer threads to finish
-Sets Fin to true, letting sensor and button know to stop sensing
-Displays score, not necessary but I thought it would be cool
-Waits for button input before sending user back to menu'''

async def LIGHTS():
    global JaneKneaded
    global JohnKneaded
    global Johntiming
    global Janetiming
    print("LIGHTS")
    while Fin == False:
        Johntiming = [0]
        Janetiming = [0]
        if JohnGeen.value() == 1: #Order of the if statements in this line and below is non-negotiable because if we arrange it any other way, when say a yellow light is checked and the note goes to green, if we then check green, the previous note from the yellow will interfere with the check.
            Johntiming.append(0)
            JohnGeen.value(0)
        if JohnMellow.value() == 1:
            Johntiming.append(2)
            JohnMellow.value(0)
            JohnGeen.value(1)
        if JohnRebt.value() == 1:
            Johntiming.append(1)
            JohnMellow.value(1)
            JohnRebt.value(0)
        if JohnKneaded == True:
            JohnRebt.value(1)
            JohnKneaded = False           
        await uas.sleep(0.25+mod)  
        if JaneGeen.value() == 1:
            Janetiming.append(0)
            JaneGeen.value(0)
        if JaneMellow.value() == 1:
            Janetiming.append(2)
            JaneGeen.value(1)
            JaneMellow.value(0)
        if JaneRebt.value() == 1:
            Janetiming.append(1)
            JaneRebt.value(0)
            JaneMellow.value(1)
        if JaneKneaded == True:
            JaneRebt.value(1)
            JaneKneaded = False
        await uas.sleep(0.25+mod)                     
'''How LIGHTS works: 
- Declares JohnKneaded, JaneKneaded (The variables that track whether a note is needed for the red lights in the two columns), Johntiming and Janetiming (The lists that track the scoring eligibility) to global
Repeated until the level is finished:
- Clear the John and Jane Timing lists
- If the left green light is on, add 0 to the list of timing values of the left side and turn off the left green light
- Repeat for the right green light.
- If the left yellow light is on, add 2 to the list of timing values of the left side, turn off the left yellow light and turn on the right green light
- Repeat for the right yellow light
- If the left red light is on, add 1 to the list of timing values of the left side, turn off the left red light and turn on the right yellow light
- Repeat for the right red light'''
async def CAMERA(): #Sensor
    pass

async def ACTION(): #Button
    global corner
    print("ACTION!")
    while Fin == False:
        if JohnButton.value() == 0:
            if max(Johntiming) == 0: #max returns the highest value from a list
                corner = 0
            elif max(Johntiming) == 1:
                corner = 1
                score += 1
                JohnMellow.value(0)
            elif max(Johntiming) == 2:
                corner = 2
                score += 2
                JohnGeen.value(0)
            else:
                print("The developer is a numpty this isnt supposed to happen, John Button is the issue")
                sys.exit()
        if JaneButton.value() == 0:
            if max(Janetiming) == 0:
                corner = 0
            elif max(Janetiming) == 1:
                corner = 1
                score += 1
                JaneMellow.value(0)
            elif max(Janetiming) == 2:
                corner = 2
                score += 2
                JaneGeen.value(0)
            else:
                print("The developer is a numpty this isnt supposed to happen, Janebutton is the issue")
                sys.exit()        
        await WORSELIGHTS()
        await uas.sleep(0.1)
'''How ACTION works:
-sets corner, the variable that tracks what state the corner lights should be, to global
then, while fin, the variable that tracks whether the song is finished or not, is false:
-if the left button is released, set corner to it's timing value, add that to score, and turn off the corresponding light in the level (unless its red). If timing isn't 0, 1, or 2, shut down the program
-repeat for right button
-Run the Worselights function'''

async def Sound(RingNursefatherOutis, buzzer, MODS):
  global JohnKneaded
  global MaxScore
  global JaneKneaded
  if RingNursefatherOutis == 0:
        buzzer.duty_u16(1000)
        buzzer.freq(B2) #Bar 1
        await uas.sleep(0.26 + MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(A2)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(B2)
        await uas.sleep(0.26+ MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(A2)
        await uas.sleep(0.13+ MODS) #Bar 2
        buzzer.freq(B2)
        await uas.sleep(0.26+ MODS)
        buzzer.freq(B1)
        await uas.sleep(0.26+ MODS)
        buzzer.freq(B2)
        await uas.sleep(0.26+ MODS)
        buzzer.freq(C3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(d3)
        await uas.sleep(0.39+ MODS) #Bar 3
        buzzer.freq(d2)
        await uas.sleep(0.26+ MODS)
        buzzer.freq(d3)
        await uas.sleep(0.26+ MODS)
        buzzer.freq(d2)
        await uas.sleep(0.26+ MODS) #Bar 4
        buzzer.freq(d3)
        await uas.sleep(0.26+ MODS)
        buzzer.freq(d2)
        await uas.sleep(0.26+ MODS)  
        buzzer.freq(d3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(e3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(d3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(C3)
        await uas.sleep(0.39+ MODS) #Bar 5
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.26+ MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(c4)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(C3)
        await uas.sleep(0.26+ MODS) #Bar 6
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.26+ MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(c4)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(C3)
        await uas.sleep(0.26+ MODS) #Bar 7
        buzzer.freq(B2)
        await uas.sleep(0.26+ MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(A2)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(B2)
        await uas.sleep(0.26+ MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(A2)
        await uas.sleep(0.13+ MODS) #Bar 8
        buzzer.freq(B2)
        await uas.sleep(0.26+ MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(A2)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(B2)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(e3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(d3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(B2)
        await uas.sleep(0.39+ MODS) #Bar 9
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(A2)
        await uas.sleep(0.13+ MODS)  
        buzzer.freq(B2)
        await uas.sleep(0.26+ MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(A2)
        await uas.sleep(0.13+ MODS) #Bar 10
        buzzer.freq(B2)
        await uas.sleep(0.26+ MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(A2)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(e3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(d3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(A2)
        await uas.sleep(0.26+ MODS) #Bar 11
        buzzer.freq(d3)
        await uas.sleep(0.26+ MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(B2)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(d3)
        await uas.sleep(0.26+ MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(B2)
        await uas.sleep(0.13+ MODS) #Bar 12
        buzzer.freq(d3)
        await uas.sleep(0.26+ MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(B2)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(d3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(a3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(d3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(C3)
        await uas.sleep(0.39+ MODS) #Bar 13
        buzzer.duty_u16(0)
        await uas.sleep(0.05+ MODS)
        buzzer.duty_u16(1000)
        await uas.sleep(0.26+ MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(C3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(a3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(C3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(C3)
        await uas.sleep(0.39+ MODS) #Bar 14
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.26+ MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(C3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(a3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(C3)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(B2)
        JohnKneaded = True
        await uas.sleep(0.39+ MODS) #Bar 15
        JaneKneaded = True
        JohnKneaded = True
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(A2)
        await uas.sleep(0.13+ MODS)
        JaneKneaded = True
        buzzer.freq(B2)
        await uas.sleep(0.26+ MODS)
        JohnKneaded = True
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        await uas.sleep(0.13+ MODS)
        buzzer.freq(A2)
        await uas.sleep(0.13+ MODS) #Bar 16
        JaneKneaded = True
        buzzer.freq(B2)
        await uas.sleep(0.26+ MODS)
        JohnKneaded = True
        buzzer.duty_u16(0)  
        await uas.sleep(0.26+ MODS)
        JaneKneaded = True
        buzzer.duty_u16(1000)
        buzzer.freq(f5)
        MaxScore += 2
        await uas.sleep(0.13 +MODS)
        buzzer.freq(a5)
        MaxScore += 2
        await uas.sleep(0.13+MODS)
        JohnKneaded = True
        buzzer.duty_u16(0)
        await uas.sleep(0.13 +MODS)
        JaneKneaded = True
        buzzer.duty_u16(1000)
        buzzer.freq(b5)
        MaxScore += 2
        await uas.sleep(0.39+ MODS) #Bar 17
        JohnKneaded = True #11
        buzzer.freq(f5)
        MaxScore += 2
        await uas.sleep(0.26+MODS)
        JaneKneaded = True
        buzzer.freq(e5)
        MaxScore+= 2
        await uas.sleep(0.26 + MODS)
        JohnKneaded = True
        buzzer.freq(d5)
        MaxScore += 2
        await uas.sleep(0.13 +MODS) #Bar 18
        JaneKneaded = True
        await uas.sleep(0.13 +MODS)
        MaxScore += 2
        JohnKneaded = True #15
        buzzer.freq(e5)
        await uas.sleep(0.26 + MODS)
        MaxScore += 2
        buzzer.freq(d5)
        await uas.sleep(0.26 +MODS)
        MaxScore += 2
        buzzer.freq(d6)
        await uas.sleep(0.13 + MODS)
        MaxScore += 2
        buzzer.freq(a5)
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(1000)
        buzzer.freq(b5) #11
        MaxScore += 2
        await uas.sleep(0.39 + MODS) #Bar 19
        JaneKneaded = True
        buzzer.freq(f5)
        MaxScore += 2
        await uas.sleep(0.13 + MODS)
        JohnKneaded = True
        await uas.sleep(0.13 + MODS)
        JaneKneaded = True
        buzzer.freq(e5)
        MaxScore += 2
        await uas.sleep(0.13 + MODS)
        JohnKneaded = True
        await uas.sleep(0.13 + MODS)
        buzzer.freq(d5)
        MaxScore += 2
        await uas.sleep(0.13 + MODS)
        buzzer.freq(f5) #15
        MaxScore += 2
        await uas.sleep(0.26 + MODS) #Bar 20
        JaneKneaded = True #20
        await uas.sleep(0.13 + MODS)
        JohnKneaded = True
        await uas.sleep(0.26 + MODS)
        JaneKneaded = True
        buzzer.duty_u16(0)#Bar 21
        await uas.sleep(0.39 + MODS)
        JohnKneaded = True
        await uas.sleep(0.13 + MODS)
        await uas.sleep(0.13+ MODS)
        JaneKneaded = True
        buzzer.duty_u16(1000)
        buzzer.freq(f5)
        MaxScore += 2
        await uas.sleep(0.26 + MODS)
        buzzer.freq(e5)
        MaxScore +=2
        await uas.sleep(0.13 + MODS)
        buzzer.freq(d5)
        MaxScore += 2
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(1000)
        MaxScore += 2
        buzzer.freq(e5)
        await uas.sleep(0.13 + MODS) #Bar 22
        buzzer.duty_u16(0)
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(1000)
        buzzer.freq(a4) #20
        MaxScore += 2
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        MaxScore +=2
        await uas.sleep(0.13 + MODS)
        buzzer.freq(a5)
        MaxScore += 2
        await uas.sleep(0.39 + MODS)
        JohnKneaded = True #25
        buzzer.freq(g5)
        MaxScore +=2
        await uas.sleep(0.13 + MODS) #Bar 23
        JaneKneaded = True
        await uas.sleep(0.13 + MODS)
        buzzer.freq(f5)
        MaxScore += 2
        await uas.sleep(0.13 + MODS) #Bar 24
        JohnKneaded = True
        await uas.sleep(0.39 + MODS)
        JaneKneaded = True
        await uas.sleep(0.26)
        JohnKneaded = True
        await uas.sleep(0.26)
        JaneKneaded = True #30
        buzzer.duty_u16(0)
        await uas.sleep(0.26 + MODS)
        JohnKneaded = True
        await uas.sleep(0.26 + MODS)
        JaneKneaded = True
        buzzer.duty_u16(1000) # 25
        MaxScore += 2
        await uas.sleep(0.13 +MODS)
        buzzer.freq(a5)
        MaxScore += 2
        await uas.sleep(0.13+MODS)
        JohnKneaded = True
        buzzer.duty_u16(0)
        await uas.sleep(0.13 +MODS)
        JaneKneaded = True
        buzzer.duty_u16(1000)
        buzzer.freq(b5)
        MaxScore += 2
        await uas.sleep(0.26+ MODS)
        JohnKneaded = True # 35
        await uas.sleep(0.13 + MODS)#Bar 25
        buzzer.freq(f5)
        MaxScore += 2
        await uas.sleep(0.26+MODS)
        JaneKneaded = True
        buzzer.freq(e5)
        MaxScore+= 2
        await uas.sleep(0.26 + MODS)
        JohnKneaded = True
        buzzer.freq(d5) #30
        MaxScore += 2
        await uas.sleep(0.13 +MODS) #Bar 26
        await uas.sleep(0.13 +MODS)
        JaneKneaded = True
        MaxScore += 2
        buzzer.freq(e5)
        await uas.sleep(0.13 + MODS)
        JohnKneaded = True
        await uas.sleep(0.13 + MODS)
        MaxScore += 2
        buzzer.freq(d5)
        await uas.sleep(0.26 +MODS)
        MaxScore += 2
        buzzer.freq(d6)
        await uas.sleep(0.13 + MODS)
        MaxScore += 2
        buzzer.freq(a5)
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(1000)
        buzzer.freq(b5) #35
        MaxScore += 2
        await uas.sleep(0.39 + MODS) #Bar 27
        buzzer.freq(f5)
        MaxScore += 2
        await uas.sleep(0.13 + MODS)
        JaneKneaded = True #40
        await uas.sleep(0.13 + MODS)
        buzzer.freq(e5)
        MaxScore += 2
        await uas.sleep(0.13 + MODS)
        JohnKneaded = True
        await uas.sleep(0.13 + MODS)
        JaneKneaded = True
        buzzer.freq(d5)
        MaxScore += 2
        await uas.sleep(0.13 + MODS)
        JohnKneaded = True
        buzzer.freq(f5)
        MaxScore += 2
        await uas.sleep(0.13) #Bar 28
        await uas.sleep(0.26) #Bar 29
        JaneKneaded = True
        await uas.sleep(0.26)
        JohnKneaded = True #45
        await uas.sleep(0.13 + MODS)
        JaneKneaded = True
        await uas.sleep(0.26)
        JohnKneaded = True
        await uas.sleep(0.13)
        buzzer.duty_u16(0)
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(1000)
        buzzer.freq(f5) #40
        MaxScore += 2
        await uas.sleep(0.26 + MODS)
        buzzer.freq(e5)
        MaxScore +=2
        await uas.sleep(0.13 + MODS)
        buzzer.freq(d5)
        MaxScore += 2
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(1000)
        buzzer.freq(e5)
        MaxScore += 2
        await uas.sleep(0.39 + MODS) #Bar 30
        MaxScore += 2
        buzzer.freq(d5)
        await uas.sleep(0.26 + MODS)
        buzzer.freq(a4) #45
        MaxScore += 2
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        MaxScore += 2
        await uas.sleep(0.26 + MODS)
        buzzer.freq(b4)
        MaxScore +=2
        await uas.sleep(0.26 + MODS) #Bar 31
        JaneKneaded = True
        await uas.sleep(0.26)
        JohnKneaded = True
        await uas.sleep(0.13)
        JaneKneaded = True #50
        buzzer.duty_u16(0)
        await uas.sleep(0.26 + MODS) #Bar 32
        JohnKneaded = True
        await uas.sleep(0.26)
        await uas.sleep(0.13)#Bar 33
        JaneKneaded = True
        await uas.sleep(0.26 + MODS)
        JohnKneaded = True
        await uas.sleep(0.13)
        JaneKneaded = True
        await uas.sleep(0.26)
        JohnKneaded = True
        await uas.sleep(0.26)
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(1000)
        buzzer.freq(f6)
        MaxScore += 2
        await uas.sleep(0.26 + MODS)
        buzzer.freq(e6)
        MaxScore += 2
        await uas.sleep(0.13 + MODS)
        buzzer.freq(d5) #50
        MaxScore += 2
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(1000)
        buzzer.freq(e6)
        MaxScore += 2
        await uas.sleep(0.39 + MODS) #Bar 34
        buzzer.freq(d6)
        MaxScore += 2
        await uas.sleep(0.26 + MODS)
        buzzer.freq(a5)
        MaxScore += 2
        await uas.sleep(0.13 + MODS)
        buzzer.duty_u16(0)
        await uas.sleep(0.05)
        buzzer.duty_u16(1000)
        MaxScore += 2
        await uas.sleep(0.26 + MODS)
        buzzer.freq(b5)
        MaxScore += 2
        await uas.sleep(0.65 + MODS) #Bar 35
        buzzer.duty_u16(0)
        await uas.sleep(0.52 + MODS) #Bar 36
        await uas.sleep(1.04 + MODS)
  else:
        print("The devs haven't made a song for that yet!")
        sys.exit()      
'''How Sound() works:
-Okay so you're thinking Liam and Oliver why is there so much code and why is it all yellow?
- So this manages the buzzer section of the song, and is in a seperate file because I don't like my code being dragged down by this disgrace.
- It might look scary but it's mostly just repeating things.
- Firstly, the Middle Nursefather Outis is just a placeholder for song id because it's in a seperate file, and is used in the if statement to change the song based on the id
- If the song is the first song, it will play raise up your bat, which is the main crime in this here court.
- The buzzer.freq plays the note in the bracket
- uas.sleep() just tells it to stop by a set value (0.26 seconds for crochets, 0.13 for semiquavers, 0.05 to get a distinction between notes of the same pitch), added to the value influenced by the temperature called "MODS".
- buzzer.duty_u16 sets the volume of the buzzer, either 1000 for normal or 0 for off
- MaxScore is just increasing the maximum score possible'''


async def WORSELIGHTS(): #Corner Lights
    global corner
    pickles.brightness(50)
    if corner == 0:
        pickles.fill(rebt)
    elif corner == 1:
        pickles.fill(mellow)
    elif corner == 2:
        pickles.fill(geen)
    else:
        print("The developer is a numpty this isnt supposed to happen, Worselights is the issue")
        sys.exit()
    pickles.show()
    corner = 3 #3= placeholder value
    await uas.sleep(1)
    pickles.brightness(0)
'''How WORSELIGHTS works:
-sets the brightness of the lorikeet to 50%
-if corner = 0, turn the lorikeet leds red. If corner = 1, turn the lorikeet leds yellow. If corner =2, turn the lorikeet leds green. If corner = anything else, turn off program
-Set corner to 3, the placeholder value
-Wait 1 second
-Set the lorikeets brightness to 0'''
async def main():
    uas.create_task(LIGHTS())
    uas.create_task(CAMERA())
    uas.create_task(ACTION())
    uas.create_task(Sound(SongId, HATE, mod))
    await uas.sleep(10)

#Main Stuff:

while True:
    Menu()
    Song()
''' How this works:
Just a while loop that runs the menu and then the song. Not much else'''



