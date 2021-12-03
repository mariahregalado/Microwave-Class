#Mariah Regalado
#Assignment 10.1
#This is a simple microwave function that has four preset functions and two presets that can be inputted
#by the user
#Sebastian Reyes helped me, and this website taught me 
#about the time module https://www.programiz.com/python-programming/time
#I imported time and intitialized my class
import time
class Microwave:
    #I made 4 dictionaries for presets and 2 empty ones for user input
    preset1={"popcorn":105}
    preset2={"defrost":180}
    preset3={"potato":360}
    preset4={"drink":70}
    userpreset={}
    userpreset2={}
    #definied __init__
    def __init__(self):
        self.__preset1=Microwave.preset1
        self.__preset2=Microwave.preset2
        self.__preset3=Microwave.preset3
        self.__preset4=Microwave.preset4
        self.__userpreset=Microwave.userpreset
        self.__userpreset2=Microwave.userpreset2
    #Defined my first get function to get all the presets
    def get_presets(self):
        #Made them into strings
        __a=''.join(Microwave.preset1.keys())
        __b=''.join(Microwave.preset2.keys())
        __c=''.join(Microwave.preset3.keys())
        __d=''.join(Microwave.preset4.keys())
        #returned the list
        return print(f"This microwave comes with the following presets:{__a}, {__b}, {__c}, {__d}")
    # defined get preset time function to take in a key as an argument
    def get_preset_time(self,key):
        #initialized variables
        self.__key=key
        self.__key.lower()
        #used if statements to check the inputted argument against the dict key
        if self.__key=="popcorn":
            #used .get to get the value and printed it 
            __x=Microwave.preset1.get("Popcorn")
            print(f"Preset Popcorn:{__x} Seconds")
        #used an else statment to pass if the key isn't equal
        else:
            pass
        #used if statements to check the inputted argument against the dict key
        if self.__key=="defrost":
            #used .get to get the value and printed it 
            __z=Microwave.preset2.get("Defrost")
            print(f"Preset Defrost:{__z} Seconds")
        else:
            pass
        #used if statements to check the inputted argument against the dict key
        if self.__key=="potato":
            #used .get to get the value and printed it 
            __y=Microwave.preset3.get("Potato")
            print(f"Preset Potato: {__y} Seconds")
        else:
            pass
        #used if statements to check the inputted argument against the dict key
        if self.__key=="drink":
            #used .get to get the value and printed it 
            self.__v=Microwave.preset4.get("Drink")
            return print(f"Preset Drink: {self.__v} Seconds")
        else:
            pass
    #defined my two add preset functions to accept the name of the preset and 
    #the time (int)
    def add_preset(self,name,time):
        #initialized variables
        self.__name=name
        self.__time=time
        #set the name as a key and the time as a value and returned the dict
        Microwave.userpreset[self.__name.lower()]=self.__time
        return print(f"{Microwave.userpreset}")
    def add_preset2(self,name,time):
        #initialized variables
        self.__name=name
        self.__time=time
        #set the name as a key and the time as a value and returned the dict
        Microwave.userpreset2[self.__name.lower()]=self.__time
        return print(f"{Microwave.userpreset2}")
    #initialized my use_preset video to accept one argument
    def use_preset(self,k):
        #initialized variable
        self.__k=k
        #used if statements to check if the argument matched a preset
        if self.__k.lower()=="popcorn":
            #I made a variable for the value
            __t=Microwave.preset1["popcorn"]
            #I used a for loop to create a timer from 1 to the value, 
            #subtracting one each time. I used sleep to make it wait 1
            #second before the next iteration
            for num in range(1,__t):
                __t=__t-1
                print(f"{__t} seconds remaining...")
                time.sleep(1)
            return print(f"Your popcorn is done!")
        #used if statements to check if the argument matched a preset
        if self.__k.lower()=="defrost":
            #I made a variable for the value
            __r=Microwave.preset2["defrost"]
              #I used a for loop to create a timer from 1 to the value, 
            #subtracting one each time. I used sleep to make it wait 1
            #second before the next iteration
            for num in range(1,__r):
                __r=__r-1
                print(f"{__r} seconds remaining...")
                time.sleep(1)
            return print(f"Done Defrosting!")
        #used if statements to check if the argument matched a preset
        if self.__k.lower()=="potato":
            #I made a variable for the value
            __e=Microwave.preset3["potato"]
              #I used a for loop to create a timer from 1 to the value, 
            #subtracting one each time. I used sleep to make it wait 1
            #second before the next iteration
            for num in range (1,__e):
                __e=__e-1
                print (f"{__e} seconds remaining...")
                time.sleep(1)
            return print(f"Your potato is done!")
        #used if statements to check if the argument matched a preset
        if self.__k.lower()=="drink":
            #I made a variable for the value
            __w=Microwave.preset4["drink"]
              #I used a for loop to create a timer from 1 to the value, 
            #subtracting one each time. I used sleep to make it wait 1
            #second before the next iteration
            for num in range(1,__w):
               __w=__w-1
               print(f"{__w} seconds remaining...")
               time.sleep(1)
            return print(f"Your drink is done!")
        #used if statements to check if the argument matched a user preset
        if self.__k.lower() in Microwave.userpreset.keys():
            #Initialized variables
            __q=Microwave.userpreset[k.lower()]
            __s = Microwave.userpreset.keys()
              #I used a for loop to create a timer from 1 to the value, 
            #subtracting one each time. I used sleep to make it wait 1
            #second before the next iteration
            for num in range(1,__q):
                __q=__q-1
                print (f"{__q} seconds remaining...")
                time.sleep(1)
            return print(f"Your {''.join(__s)} is done!")
        #used if statements to check if the argument matched a user preset
        if self.__k.lower() in Microwave.userpreset2.keys():
            #I made a variable for the value
              #I used a for loop to create a timer from 1 to the value, 
            #subtracting one each time. I used sleep to make it wait 1
            #second before the next iteration
            __p=Microwave.userpreset2[k.lower()]
            for num in range(1,__p):
                __p=__p-1
                print(f"{__p} seconds remaining...")
                time.sleep(1)
            print(f"Your {''.join(Microwave.userpreset2.keys())} is done!")
            
#Defined my main function and used my methods
def main():
    z=Microwave()
    z.get_presets()
    z.get_preset_time("drink")
    #input the new user presets as arguments and return them 
    z.add_preset("Vegetable",180)
    z.add_preset2("Rice",80)
    #argument is the thing you want to cook 
    z.use_preset("RiCe")
#called my main function
if __name__=="__main__":
    main()
        
    