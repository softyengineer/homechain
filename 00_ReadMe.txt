






# https://github.com/modmypi/Rotary-Encoder/

https://bitbucket.org/laurent_meyer/my-pi-projects/src/330002d43e84728d4b83e30f0cee4fd7945c33d3/Intelligent_Switcher/roue_codeuse.py?at=master&fileviewer=file-view-default




Import data here, making classes for each component

D:\Mega\MEGAsync\13 Northampton\90 St James Park Road\home automation\homeChain\rotary_encoder_example.py

cd /bin
python rotaryencodersmall.py



Files located in:
bin/
	readencoder.py
	RotaryEnc.py
	
	
Enter Python:
python

import RotaryEnc:
	from RotaryEnc import RotaryEnc
	
Set up pins using Pin A, Pin B, ReMin, ReMax:
	Position = 1
	RE1 = RotaryEnc(17,18,Position,0,10,1) 
	
	
	
	
	
	
	CLK - GPIO17 (pin11)
DT - GPIO18 (pin12)
+ - 3v3 (pin1)
GND - GND (pin6)