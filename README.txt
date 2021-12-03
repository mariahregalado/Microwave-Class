Class Description: 
The class I made is a microwave. It comes with four presets in
the form of dictionaries with the keys being the names of the food the microwave is 
heating and the values being the times in seconds. The keys are strings and the values
are integers. There are also two empty dictionaries that allow the user to input their
own presets to use the microwave. I also implemented the time module to make my timer, 
though only the .sleep function is used. 
Variable Description:
preset1: A dictionary containing the key 'popcorn' and value 105. When plugged into the 
use_preset, it starts a timer for 105 seconds.
preset2:A dictionary containing the key 'defrost' and value 180. When plugged into the 
use_preset, it starts a timer for 180 seconds.
preset3:A dictionary containing the key 'potato' and value 360. When plugged into the 
use_preset, it starts a timer for 360 seconds.
preset4:A dictionary containing the key 'drink' and value 70. When plugged into the 
use_preset, it starts a timer for 70 seconds.
userpreset: An empty dictionary for the user to add to using the add_preset method.
userpreset2:A second empty dictionary for the user to add to.
a:The string version of the key in preset1 (popcorn).
b: The string version of the key in preset2(defrost).
c:The string version of the key in preset3(potato).
d:The string version of the key in preset4(drink).
key: Inputted argument by the user, used to get values.
x:The value corresponding to key 'popcorn'(105).
z:The value corresponding to key 'defrost'(180).
y:The value corresponding to key 'potato' (360).
name: The key of the user created dictionary.
time: The value of the user created dictionary.
k: User inputted argument used in for loops to start timers, should be a a preset key.
t:The value corresponding to key 'popcorn'(105).
r:The value corresponding to key 'defrost'(180).
e:The value corresponding to key 'potato'(360).
w:The value corresponding to key 'drink' (70).
q:The value in the user created dictionary.
s:The key in the user created dictionary.
p:The value in the second user created dictionary.
Method Descriptions:
__init__: Doesn't accept any arguments and returns nothing. It sets up variables.
get_presets: Doesn't accept any arguments, but returns a string containing the
keys of the available presets. It also doesn't accept any inputs.
get_preset_times: It accepts a key from a preset dictionary as an argument. It
returns the corresponding value for the inputted key. Only viable on the presets, not
userpresets.
add_preset: It accepts two arguments, a string to be used as a key in the first user 
preset dictionary. The second argument is an integer to be used as a value in the
dictionary. It returns the dictionary with the arguments implemented.
add_preset2:Accepts the same two arguments as the first one, but adds them to the 
second empty userpreset dictionary. It also returns the dictionary with the newly
implemented data.
use_preset: This accepts one argument, which should be a string of a key to a dictionary.
It should be the name of the food desired to cook. It returns a timer, which counts down
the value of the dictionary until the food is ready, then a completed message will print.
Demo Program Description: 
My demo program gets all of the available presets first. Then it gets the preset time
for 'Drink', which is 70 seconds. Then, after inputting my arguments into the add methods,
it returns the two new user inputted dictionaries. This is mostly for confirmation that
the arguments were added. Then I would input the item I wanted to cook in the microwave
into the use_preset method, and the timer would start when the program ran. Once the timer 
is done, the completed message will print. 
Demo Program Instructions:
You just need to input the required arguments and run it in your terminal. 