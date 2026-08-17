#Imports:
from machine import Pin, ADC, PWM
import math
import uasyncio as uas
import threading 
import time
import LilBirdy
from LilBirdy import Neopixel
import BiggestBird #Lil birdy, neopixel and biggest bird are functions for lorikeet, and the functions are located inside of the pico itself. I learnt how to operate this from 
import sys #Mainly for stopping everything if the program doesnt want to coorperate respectfully

#Variables/prerequisites
JohnButton = Pin(16, Pin.IN, Pin.PULL_DOWN)# Left Button
JaneButton = Pin(17, Pin.IN, Pin.PULL_DOWN) # Right Button
PotentialMan = ADC(Pin(22)) #Potentiometer
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


#Functions:

def Menu():
    pickles.brightness(0)
    while Johnreleased == False and Janereleased == False:
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
'''How Menu works: 
Repeated until any button is pressed:
- Sets variable called mahoraga to get the analog input of the potentiometer
- Sets a variable called SongId to Mahoraga, converted to angular degrees, divided by 5, rounded down
- Lights up a different coloured light on the lorikeet for UX'''

def Song():
    global Fin
    Fin = False
    pickles.brightness(0)
    uas.run(main())
    Fin = True
    print(f"Your score is {score}/{MaxScore}!")
    while True:
        if Johnreleased == True or Janereleased == True:
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

async def LIGHTS():
    global JaneKneaded
    global JohnKneaded
    global Johntiming
    global Janetiming
    while Fin == False:
        Johntiming = []
        Janetiming = []
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
    while Fin == False:
        if Johnreleased == True:
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
                print("The developer is a numpty this isnt supposed to happen")
                sys.exit()
        if Janereleased == True:
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
                print("The developer is a numpty this isnt supposed to happen")
                sys.exit()        
        uas.run(WORSELIGHTS())
'''How ACTION works:
-sets corner, the variable that tracks what state the corner lights should be, to global
then, while fin, the variable that tracks whether the song is finished or not, is false:
-if the left button is released, set corner to it's timing value, add that to score, and turn off the corresponding light in the level (unless its red). If timing isn't 0, 1, or 2, shut down the program
-repeat for right button
-Run the Worselights function'''

async def WORSELIGHTS(): #Corner Lights
    pickles.brightness(50)
    if corner == 0:
        pickles.fill(rebt)
    elif corner == 1:
        pickles.fill(mellow)
    elif corner == 2:
        pickles.fill(geen)
    else:
        print("The developer is a numpty this isnt supposed to happen")
        sys.exit()
    corner = 3 #3= placeholder value
    await uas.sleep(1)
    pickles.brightness(0)
'''How WORSELIGHTS works:
-sets the brightness of the lorikeet to 50%
-if corner = 0, turn the lorikeet leds red. If corner = 1, turn the lorikeet leds yellow. If corner =2, turn the lorikeet leds green. If corner = anything else, turn off program
-Set corner to 3, the placeholder value
-Wait 1 second
-Set the lorikeets brightness to 0'''


async def RELEASETHECHECKER(): #Checks whether button was released to prevent inputs getting registered every frame the button is held down
    global Johnreleased
    global Janereleased
    while True:
        if JohnButton.value() == 1 and Johnpress == False: 
            Johnpress = True
            Johnreleased = False
        elif JohnButton.value() == 0 and Johnpress == True:
            Johnreleased = True
            Johnpress = False
        else:
            Johnpress = False
            Johnreleased = False
        if JaneButton.value() == 1 and Janepress == False:
            Janepress = True
            Janereleased = False
        elif JaneButton.value() == 0 and Janepress == True:
            Janereleased = True
            Janepress = False
        else:
            Janepress = False
            Janereleased = False
        await uas.sleep_ms(75)
'''How RELEASETHECHECKER works:
-Set Johnreleased and Janereleased(The variables that tell whether the button was released, rather than being held down or not being pressed at all) to global
-forever, if the left button is pressed, while Johnpress is false, John press is now true and Johnreleased is false.
  if the left button isn't pressed while Johnpress is true, Johnreleased is true and Johnpress is false
  if any other combination of those two conditions is happening, Johnpress and John released are both false
  and do the same for the right button, but with Janes instead of Johns'''
#Main Stuff:
async def main():
    uas.create_task(LIGHTS())
    uas.create_task(CAMERA())
    uas.create_task(ACTION())
uas.run(RELEASETHECHECKER())
while True:
    Menu()
    Song()
''' How this works:
setting a thread for the function that checks whether the button was released or not and then
Just a while loop that runs the menu and then the song. Not much else'''