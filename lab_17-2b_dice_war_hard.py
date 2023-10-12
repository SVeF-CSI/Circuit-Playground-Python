from adafruit_circuitplayground import cp
import random
import time

cp.pixels.brightness=0.1

scoreA = 0
scoreB = 0

while scoreA < 5 and scoreB < 5: 
    

    
    #Player A always goes first
    if cp.button_a==True:
        while(cp.button_a==True):
            pass
        # click detected
        rollA = random.randint(0,4)
        print("Player A:",rollA)
        
        #reset ? 
        for i in range(5):
            cp.pixels[i] =(0,0,0)
        
        #light up
        for i in range(rollA+1):
            cp.pixels[i] =(0,0,255)
            time.sleep(0.05)
    
    #Player B goes next
    #To keep the logic simple, assume player B always goes next and the winner is determined afterward
    if cp.button_b==True:
        while(cp.button_b==True):
            pass
        # click detected
        rollB = random.randint(0,4)
        print("Player B:",rollB)
        
        #reset ? 
        for i in range(5,10):
            cp.pixels[i] =(0,0,0)
        
        #light up
        for i in range(5,5+rollB+1):
            cp.pixels[i] =(255,0,0)
            time.sleep(0.05)
        
        #pause for a half sec
        time.sleep(.5)
        #clear
        cp.pixels.fill((0,0,0))
        
        #determine who won
        if rollA>rollB:
            print("Player A wins")
            scoreA+=1
            
            #blink A couple times
            for x in range(3):
                for i in range(rollA+1):
                    cp.pixels[i] =(0,0,255)
                time.sleep(.3)
                cp.pixels.fill((0,0,0))
                time.sleep(.1)
            
        elif rollA<rollB:
            print("Player B wins")
            scoreB+=1
            #blink B couple times
            for x in range(3):
                for i in range(5,5+rollB+1):
                    cp.pixels[i] =(255,0,0)
                time.sleep(.3)
                cp.pixels.fill((0,0,0))
                time.sleep(.1)
        else:
            print("It's a tie")
            
            #blink A & B 3 times
            for x in range(3):
                #on
                for i in range(rollA+1):
                    cp.pixels[i] =(0,0,255)
                for i in range(5,5+rollB+1):
                    cp.pixels[i] =(255,0,0)
                    
                time.sleep(.3)
                #off
                cp.pixels.fill((0,0,0))
                time.sleep(.1)
                
        time.sleep(.2)
        #show the score
        print("Score: Player A=",scoreA," Player B=",scoreB)
        
        #display A score
        for i in range(scoreA):
            cp.pixels[i] =(255,255,255)
        #display B score
        for i in range(5,5+scoreB):
            cp.pixels[i] =(255,255,255)
