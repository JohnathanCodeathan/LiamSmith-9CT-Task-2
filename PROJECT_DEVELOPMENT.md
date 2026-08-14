# Project Documentation
## Requirements Outline
### Defining My Purpose
The need:

Parents have significantly negatively impacted their childs attention span and cognitive development by shoving an iPad in their face when the parent is too busy at work and the child would otherwise disturb their work. I acknowledge the struggle that parents face in trying to earn income to buy products to support their child, while also trying to look after their child, but shoving an iPad in their face is lazy and negatively impacts their child.

The Solution:

With all that said,  instead  of turning to the iPad,  they can use our product, the Rhythminator5000, which not only keeps your child entertained and stimulated while you work, but also permanently increases their memory,  hand eye coordination, reaction speed, sense of rhythm and multitasking skills. Furthermore, this product can be used with people of all ages who want to test their hand eye coordination, reaction speed, or just want to have fun with this product. This toy will have various levels to choose from ranging in difficulty, and will have an added challenge of a motion sensor that will increase the speed of the notes if the users hands/fingers are moving fast, and decrease the speed of the notes if the users hands/fingers are moving slow, encouraging the user to think about their speed as well as the level, further boosting hand eye coordination and speed control.

### Key Actions
- Buzzer plays the song once song is selected
- Lights display the notes that are upcoming at an interval of 0.5 seconds
- If the button is pressed when a note has reached the bottom lights, increase score and a seperate green light illuminates itself.
- If button is pressed when there is no note at the bottom, a seperate red light illuminates itself 
- If the button is not pressed when the note passes the bottom lights, the seperate red light illuminates itself.

### Functional Requirements:
- Potentiometer input: Used to select from the song options able to be played.  By dividing the potentiometer into sections of (360/[amount of songs) degrees, the user can turn the potentiometer into those sections and a different coloured light bulb will light up.
- Light output in menu: Once the potentiometer has reached a specific section, the corresponding light bulb will light up. These bulbs will be located in the top corner of the breadboard.
- Menu button input: Once the user has decided on their song, they can press either of the two buttons on the bottom of the breadboard to start the level.
- Buzzer output: Once the level begins, the buzzer will play the selected song.
- Light output in level: There will be a 2 light wide column somewhere in the middle of the breadboard with two buttons below the bottom two bulbs. When a note is required,  one of the two lights at the top of the column will light up before player input is needed. Then that top light will turn off and the light below it will turn on, and this will be repeated at an interval of 0.5 seconds until this light reaches the bottom and the buzzer plays the corresponding note of the song. 
- Button input in level: The player will then be required to press the button below the section of the column that has the note lit up before it disappears. If they do so successfully, a value of 2 will be added to their score, and one of the green lights in the corner will light up for a short time for user experience. If the user presses the button slightly too early or late, a value of 1 will be added to their score, and one of the yellow lights in the corner will light up for a short time for user experience. However, if the user either doesn't press the button in time at all, or presses it way too early, no value will be added to the score, but a red light in the corner will light up for user experience.
- Speed sensor: Once the level begins, if the sensor detects the users hands moving fast enough, the interval of which notes move speeds up, along with the song. Conversely, if the users hands are moving slow enough, the speed of the notes and song will slow down.
- Digital Output (???): At the end of and throughout the level, the users score will be displayed on the computer as a fraction of score/maximum possible score.

### Test Cases:
| Test Case | Input | Expected Output |
| --------- | ----- | --------------- |
| User turns potentiometer | User rotates the potentiometer to the desired section | Corresponding coloured light bulb will light up |
| User presses button in menu phase | User presses button when they have chosen their song with the potentiometer in the menu phase | The corresponding song and level will play |
| User presses button perfectly on time | User presses the button while the light directly above it is lit up | Score will be increased by 2 and green light in the corner will light up for 1 second. |
| User presses button almost on time | User presses button while the note is in between 1 second too early and 1 second too late but not perfectly on time | Score will increase by 1 and yellow light in corner will light up for 1 second |
| User doesn't press button on time at all | User presses button while there is note within the pressable range of 1 second too early and 1 second too late, or the user doesn't press the button at all when the note passes by | Score will stay the same and the red light in the corner will light up for 1 second |
| User's hands are moving fast | The users hands are moving at a rather quick speed | Song and time between notes moving down increases in speed |
| User's hands are moving slow | The users hands are moving at a rather sluggish speed | Song and time between notes moving down decreases in speed. |
### Non-functional Requirements:
- Button response time: The button inputs in both the menu and song phases should react instantaneously, or within 0.1 seconds or less.
- Potentiometer response time: The potentiometer in the menu phase should react to input as fast as possible, or within 0.1 seconds or less.
- Sensor response time: The sensor should react to an update in the users hand speed within 1 second or less.
- Light efficiency: In the song phase, the notes should move down a level every 0.5 seconds, and the lights in the corner should light up within 0.5 seconds of a user input.
## Design
### Flow Chart:

![Here is a comprehensive flow chart for the design of most of the program ](IMAGE_FRIEND/FlowChart.png)

### Psuedocode:
 START CornerLights()

    IF corner = 0
        RedCornerLight = ON
    ELSE IF corner = 1
        YellowCornerLight = ON
    ELSE IF corner = 2
        GeenCornerLight = ON
    ELSE
        Display "The developer is a numpty this isnt supposed to happen"
        END EVERYTHING    
    END IF
    Wait 1 Second
    All Corner Lights = OFF
    corner = 3
END CornerLights()

 START SENSOR()

    WHILE finished is false
        READ SENSOR
        IF fingerspeed > x+5
            modifier = modifier - 0.1
        ELSE IF fingerspeed < x-5
            modifer = modifier + 0.1
        END IF
        WAIT 1 second
    ENDWHILE
END SENSOR()

START LIGHT()

    WHILE finished is False
        IF leftnoteneeded = TRUE
            Top left light = ON
            leftnoteneeded = false
        ENDIF
        IF rightnoteneeded = TRUE
            Top Right light = ON
            rightnotneeded = false
        ENDIF
        IF lightsinbottom = ON
            Timing = 2
            lightsinbottom = OFF
        ENDIF
        FOR current row = bottom row +1 TO top row STEP 1
            IF lights in current row = ON
                lights in current row -1 = ON
                lights in current row = OFF
            END IF
            IF current row = Yellow
                timing = 1
            ELSE IF current row = Red
                timing = 0
            ELSE
                DISPLAY "The developer is a numpty this isnt supposed to happen"
                END EVERYTHING
            END IF
            WAIT 0.5 + modifier seconds
        END FOR
    ENDWHILE
    END LIGHT()

START Button()

    WHILE FINISHED IS FALSE
        Read Button
        IF Button is pressed
            IF timing = 0
                corner = 0
            ELSE IF timing = 1
                corner = 1
                closest yellow light = OFF
                score = score + 1
            ELSE IF timing = 2
                corner = 2
                score = score + 2
            ELSE:
                Display "The developer is a numpty this isnt supposed to happen"
                END EVERYTHING
            ENDIF
        ENDIF
            CornerLight()
    ENDWHILE
END Button()

START Buzzer()

    if SongID = 0
        play Raiseupyourbat
    elif SongID = 1
        play Don't
    elif SongID = 2
        play FlowerMan
    elif SongID = 3
        play specialist
    elif SongId = 4
        play TianTian
    else:
        display "The developer is a numpty this isnt supposed to happen"
END Buzzer()

START Song()

    START Buzzer() THREAD
    START Lights() THREAD
    START Sensor() THREAD
    START Button() THREAD
    WAIT FOR Buzzer() THREAD
    WAIT FOR Lights() THREAD
    finished? = True
    Display score
    WHILE Button is not pressed
         READ Button
    END WHILE
END Song()

START Menu()

    WHILE Button is not pressed
        READ potentiometer
        READ Button
    END WHILE
    SongID = potentiometer angle / 72
END Menu()

START
   
    WHILE TRUE
        MENU()
        SONG()
    ENDWHILE
END

## Development and Integration
### Initial Prototype:
```Python
#Imports:
from machine import Pin, ADC, PWM
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
HATE = PWM(Pin(26))
PotentialMan = ADC(Pin(22)) #Potentiometer
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
MAHORAGA = 1.0 #Analog value of potentiometer
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
    while Johnreleased == False and Janereleased == False:
        MAHORAGA = PotentialMan.read_u16() #Checks potentiometer until button is not pressed
        SongId = math.floor((MAHORAGA/Conv)/72) #SongId is set to rounded down version of Mahoraga if it was in angular degrees
        pickles.brightness(50)
        if SongId == 0: #If you look at the markdown, the songid isn't in the while statement and the if statement is non-existent,  but this is because I would like the lights on the controller to light up as you move the potentiometer
            pickles.fill(ourple)
        elif Songid == 1:
            pickles.fill(rebt)
        elif Songid == 2:
            pickles.fill(geen)
        elif Songid == 3:
            pickles.fill(mellow)
        elif Songid == 4:
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

def LIGHTS():
    global JaneKneaded
    global JohnKneaded
    global Johntiming
    global Janetiming
    while Fin == False:
        Johntiming = []
        Janetiming = []
        if JohnGeen.value() ==1: #Order of the if statements in this line and below is non-negotiable because if we arrange it any other way, when say a yellow light is checked and the note goes to green, if we then check green, the previous note from the yellow will interfere with the check.
            Johntiming.append(0)
            JohnGeen.value() = 0
        if JaneGeen.value() ==1:
            Janetiming.append(0)
            JaneGeen.value() = 0
        if JohnMellow.value() ==1:
            Johntiming.append(2)
            JohnMellow.value() = 0
            JohnGeen.value() = 1
        if JaneMellow.value() ==1:
            Janetiming.append(2)
            JaneGeen.value() = 1
            JaneMellow.value() = 0
        if JohnRebt.value() ==1:
            Johntiming.append(1)
            JohnMellow.value() = 1
            JohnRebt.value() = 0
        if JaneRebt.value() ==1:
            Janetiming.append(1)
            JaneRebt.value() = 0
            JaneMellow.value() = 1
        if JohnKneaded == True:
            JohnRebt.value() = 1
            JohnKneaded = False
        if JaneKneaded == True:
            JaneRebt.value() = 1
            JaneKneaded = False            
        time.sleep(0.5+mod)           
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
def CAMERA(): #Sensor
    pass

def ACTION(): #Button
    global corner
    while Fin == False:
        if Johnreleased == True:
            if max(Johntiming) == 0: #max returns the highest value from a list
                corner = 0
            elif max(Johntiming) == 1:
                corner = 1
                score += 1
                JohnMellow.value() = 0
            elif max(Johntiming) == 2:
                corner = 2
                score += 2
                JohnGeen.value() = 0
            else:
                print("The developer is a numpty this isnt supposed to happen")
                sys.exit()
        if Janereleased == True:
            if max(Janetiming) == 0:
                corner = 0
            elif max(Janetiming) == 1:
                corner = 1
                score += 1
                JaneMellow.value() = 0
            elif max(Janetiming) == 2:
                corner = 2
                score += 2
                JaneGeen.value() = 0
            else:
                print("The developer is a numpty this isnt supposed to happen")
                sys.exit()        
        WORSELIGHTS()
'''How ACTION works:
-sets corner, the variable that tracks what state the corner lights should be, to global
then, while fin, the variable that tracks whether the song is finished or not, is false:
-if the left button is released, set corner to it's timing value, add that to score, and turn off the corresponding light in the level (unless its red). If timing isn't 0, 1, or 2, shut down the program
-repeat for right button
-Run the Worselights function'''

def WORSELIGHTS(): #Corner Lights
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
    time.sleep(1)
    pickles.brightness(0)
'''How WORSELIGHTS works:
-sets the brightness of the lorikeet to 50%
-if corner = 0, turn the lorikeet leds red. If corner = 1, turn the lorikeet leds yellow. If corner =2, turn the lorikeet leds green. If corner = anything else, turn off program
-Set corner to 3, the placeholder value
-Wait 1 second
-Set the lorikeets brightness to 0'''


def RELEASETHECHECKER(): #Checks whether button was released to prevent inputs getting registered every frame the button is held down
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
'''How RELEASETHECHECKER works:
-Set Johnreleased and Janereleased(The variables that tell whether the button was released, rather than being held down or not being pressed at all) to global
-forever, if the left button is pressed, while Johnpress is false, John press is now true and Johnreleased is false.
  if the left button isn't pressed while Johnpress is true, Johnreleased is true and Johnpress is false
  if any other combination of those two conditions is happening, Johnpress and John released are both false
  and do the same for the right button, but with Janes instead of Johns'''

#Main Stuff:
collar = threading.Thread(target=RELEASETHECHECKER) #Thread for the improved button fix
collar.start()
while True:
    Menu()
    Song()
''' How this works:
setting a thread for the function that checks whether the button was released or not and then
Just a while loop that runs the menu and then the song. Not much else'''
```
- Notes: We got a few errors with this prototype, namely one just telling us to soft reboot and the other one telling us to reset our microbit and that something went wrong in Thonny's back end, I'll check on that when I can.
## Testing and Debugging

## Evaluation
