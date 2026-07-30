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

## Development and Integration

## Testing and Debugging

## Evaluation
