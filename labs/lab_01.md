## Lab 1: 
 
##### Naming conventions 

Put all of your homework files together into one folder, zip it and email it to your lab assistant with your name_the week.zip 

**for example:** 
phoenixperry_01.zip


##### Due Date 

Turn each lab no later than 24 hours after the lab session. 

##### Grading Matrix 

Trait | Very Good | Good | Acceptable | Unsatisfactory	
--- |--- | --- | --- | --- |
| *Specifications* | The program produces correct results and meets all specifications. | The program works and produces the correct results and displays them correctly. It also meets most of the other specifications. | The program produces correct results but does not display them correctly. | The program is producing incorrect results.
*Readability* | The code is exceptionally well organized and very easy to follow. | The code is fairly easy to read. | The code is readable only by someone who knows what it is supposed to be doing.| The code is poorly organized and very difficult to read.|
*Delivery* | The program was delivered on time. | The program was delivered within a week of the due date. | The code was within 2 weeks of the due date. | The code was more than 2 weeks overdue but no later than 3 weeks overdue. 

**After 3 weeks, you immediately get a fail for this lab. 


##Exercise 1_0 
1. Install Python version 2.7.10 
https://www.python.org 

2. Get java 

	* If you are on a mac, you'll need to install java. 
You can get apple's java here
https://support.apple.com/kb/DL1572?locale=en_US 

	
	* If you are on windows you might also need to do this step. Download java SE for runtime 
http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html 


3.Install Pycharm's Community Edition: 
https://www.jetbrains.com/pycharm/download/ 

4.Open up pycharm and create a new project from the menu choose:
	File > New Project 	
	It will open this pop up. 	
![](https://github.com/phoenixperry/hku_python/blob/master/images/newProject.png)  
	
Make sure you select the version of python that's 2.7 that's in the Library folder if you're on a mac. On windows this will not be a problem. You'll just see it listed here. 


5. A few things about Pycharm that are clever 
* To run your code, from the menu choose: 
Run > Run 

* To see the output console, from the menu choose: 
View > Tool Windows > Python Console


---
##Exercise 1_1 

Create a program that prints out a tic tac toe board when it runs in the console 

Sample output: 
``` 
|O|X|O|
|O|X|O|
|X|O|X|
```

##Exercise 1_2  
Create a simple program that asks the user a series of questions and saves the answers about an imaginary character, Ursula.  
 
1. What is your character's favorite color?  

2. What is your character's favorite food?  

3. Where does your character's live?  

Then print out all of these answers in the following format:  

Ursula's favorite colors is [USER COLOR HERE] and her favorite foods is [USER FOOD HERE]. She lives in [USER LOCATION HERE]. 

Example output: 
Ursula's favorite colors is grey and her favorite foods is cake. She lives in The Alps. 

This exercise uses string variables and the raw_input("Some message to the user") function. 

The raw_input function just reads whatever the user types and assigns it to the variable on the left of it 

for example: 

` userInput = raw_input("What's in quotes is printed in the console for the user as a prompt")`

Remember variable names can be anything. We make them up! userInput in this case could be potato and do exactly the same thing. 

` potato = raw_input("What's in quotes is printed in the console for the user as a prompt")`

Remember that raw_input("some prompt") is a function. A function is like a verb in a sentence. It does a thing. In this case it saves what the user types in the variable names potato. 

We will go into that in lots of detail in the coming weeks! No fear! This is a simple cheat I'm doing to get you making *something* and typing code. Have no fear if you only understand this a bit. That's all I have explained it thus far!  


Hint:
Check out the class code from the first week here -> https://github.com/phoenixperry/hku_python/blob/master/class_code/week01/week01.py  

####Are you lost? 
SPEAK UP! We will help you I promise. Don't let this drag on and you are not alone! :) 
Programming is crazy hard the first time you learn about it.
 
Why not give this site a try. It's super awesome and very clear.http://www.learnpython.org 


####Are you bored? 
Are you horridly bored? Why not check out getting python running on a raspberry pi! 

You could buy a simple pi here:
https://www.raspberrypi.org/products/raspberry-pi-2-model-b/

Now spend the first few weeks building the first project out of the book, Raspberry Pi Projects.   

https://www.raspberrypi.org/blog/raspberry-pi-projects-a-big-book-by-andrew-robinson-and-mike-cook/
