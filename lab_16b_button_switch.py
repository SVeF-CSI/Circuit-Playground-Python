from adafruit_circuitplayground import cp

while True:
    if cp.button_a:    #pressed
	    #loop until cp.button changes to False - released)
        while (cp.button_a):  
		    pass
        print("You clicked the button a") #register a click
    if cp.button_b:    #pressed
	    #loop until cp.button changes to False - released)
        while (cp.button_b):  
		    pass
        print("You clicked the button b") #register a click

