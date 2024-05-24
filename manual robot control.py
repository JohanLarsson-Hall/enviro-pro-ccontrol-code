import time
from adafruit_servokit import ServoKit

# Initialize the servo HAT
kit = ServoKit(channels=16)

# Set the minimum and maximum pulse lengths (in microseconds)
SERVO_MIN_PULSE = 150
SERVO_MAX_PULSE = 600

# Set the angle range of your servos
MIN_ANGLE = 0
MAX_ANGLE = 180

# Map servo range to pulse lengths
def map_servo(angle):
    return int((angle - MIN_ANGLE) / (MAX_ANGLE - MIN_ANGLE) * (SERVO_MAX_PULSE - SERVO_MIN_PULSE) + SERVO_MIN_PULSE)

# Function to get servo angle from user input
def get_servo_angle(servo_num, last_angle):
    while True:
        try:
            angle_input = input(f"Enter servo {servo_num} angle (0-180) [Last angle: {last_angle}]: ")
            if angle_input.strip() == "":
                return last_angle
            angle = int(angle_input)
            if angle < 0 or angle > 180:
                print("Angle must be between 0 and 180.")
            else:
                return angle
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main loop
last_angles = [90] * 16  # Default angle for all servos

while True:
    try:
        # Prompt the user to input the angle for each servo
        for servo_num in range(16):
            last_angle = last_angles[servo_num]
            angle = get_servo_angle(servo_num, last_angle)
            last_angles[servo_num] = angle
            
            # Map servo angle to pulse length
            pulse_length = map_servo(angle)
            
            # Set the servo position
            kit.servo[servo_num].angle = angle
            
            print(f"Servo {servo_num} Angle:", angle)
        
        time.sleep(0.1)  # Delay for smoother movement
        
    except KeyboardInterrupt:
        print("\nExiting program")
        break
