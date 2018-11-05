import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
 
class RotaryEnc:
    
    def __init__(self,PinA,PinB,Position,REmin,REmax,inc):
        
        self.PinA = PinA                                        # GPIO Pin for encoder PinA
        self.PinB = PinB                                        # GPIO Pin for encoder PinB
        self.Position = Position                                # encoder 'position'
        self.min = REmin                                        # Max value
        self.max = REmax                                        # Min value
        self.inc = inc                                          # increment  
        self.oldPinA = 1 
        GPIO.setup(self.PinA, GPIO.IN)                          # setup IO bits...
        GPIO.setup(self.PinB, GPIO.IN)                          #
                                                                #
    def read(self):                                             # Function to Read encoder...
        encoderPinA=GPIO.input(self.PinA)                       # get inputs...
        encoderPinB=GPIO.input(self.PinB)                       #
        if encoderPinA and not self.oldPinA:                    # Transition on PinA?
                if not encoderPinB:                             #    Yes: is PinB High?
                        self.Position=self.Position+self.inc    #        No - so we're going clockwise
                        if self.Position > self.max:            #        limit maximum value
                                self.Position = self.max        #
                                                                #
                else:                                           #
                                                                #           
                        self.Position=self.Position-self.inc    #        Yes - so we're going anti-clockwise
                        if self.Position < self.min:            #        limit minimum value
                                self.Position = self.min        #     
        self.oldPinA=encoderPinA                                #    No: just save current PinA state for next time        
                                                                #
 
# -------------------------------------------------------------------------------------------------------------------
# Here's a simple example of how to use the RotaryEnc Class ...
#
# Set up Rotary Encoder...
#  format is : RotaryEnc(PinA,PinB,button,Position,REmin,REmax,inc):
Position = 1                                                    # Position is also used as a variable
RE1 = RotaryEnc(12,16,Position,0,10,1)                          # Instatiate the encoder                         
 
 
# Main Operating Loop...
while True:
    try:
        RE1.read()                                                  # Read the encoder    
        if Position <> RE1.Position:                                # has the position changed?
            print RE1.Position                                      # Yes: so print new value
            Position = RE1.Position                                 #      and update it
    except KeyboardInterrupt:
        break