import random
import time
from adafruit_circuitplayground import cp

# brightness between 0 and 1
cp.pixels.brightness=0.3 

# set tapped to true if tapped once
cp.detect_taps = 1

#answerbank
answerbank = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes – definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.' 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Dont count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']

while True:
    
    #wait for tap to trigger
    if cp.tapped:

        #thinking light show
        
        #do this 7 times
        # for i in range(7):
        #     #generate a random number
        #     rnd = random.randint(0,9) 
            
        #     #random RGB color
        #     red = random.randint(0,255)
        #     green = random.randint(0,255)
        #     blue = random.randint(0,255)
            
        #     #turn on the led at location rnd
        #     #using random RGB values
        #     cp.pixels[rnd] =(red,green,blue) 
        #     #cp.pixels[rnd] =(255,0,0) 
        #     time.sleep(0.1)
            
        #     #turn off
        #     cp.pixels[rnd] =(0,0,0)   #turn it off
        #     time.sleep(0.1)
        
        #alt: spinning circle 3 times
        for i in range(2):
            for i in range(10):
                cp.pixels[i] =(196,0,32)
                time.sleep(0.07)
            
            for i in range(10):
                cp.pixels[i] =(0,0,0)
                time.sleep(0.07)
                
        #print the randomly selected answer
        random_answer = random.choice(answerbank)
        print("=== Magic 8 Ball says ===")
        print(random_answer)
        
    time.sleep(0.05)
