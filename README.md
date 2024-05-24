# enviro-pro-ccontrol-code
this repository contains all the code for the control of the Enviro Pro robot it also contains the .step file for fabrication
SECTION 1 - OVERVIEW - WHAT IS THE PROJECT
This project is a combination of the design, fabrication and programming of a robot
From the ground up
All base files for code and the models are included
SECTION 2 - PREPARATION REQUIREMENTS
You will need:
a 3D printer
16 sg90 servo motors
A Raspberry Pi 5
A servo driver HAT
A few KGs of PLA filament
You must also install all the libraries required for the servo driver HAT if the Raspberry Pi says it can’t install a library because it’s externally managed copy the command in the code that says --break system packets it will install the library just fine
Also adafruit servokit is required for the manual code for control
SECTION 3 - HOW DO YOU BUILD IT
Building it consists of taking the brackets and screwing the motors in then connecting them to the other brackets the CAD file is pretty self-explanatory MAKE SURE TO MOUNT ALL THE MOTORS IN THE SAME ORIENTATION also MAKE SURE TO MOUNT THE MOTOR ARMS IN THE CORRECT ORIENTATION OR YOU ROBOOT WILL NOT WALK PROPERLY
SECTION 4 - HOW DO YOU OPERATE IT
The code that comes in the GitHub repository is manual control only. enter values between 0 and 180 press enter to leave the values the same feel free to write inverse kinematics code if you want
SECTION 5 - HOW DO YOU TEST OR CHECK IT
Check it by using the manual control code to set all the motors to 90 degrees
SECTION 6 - LINK TO REFERENCES
