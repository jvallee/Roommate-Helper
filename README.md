CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Recommended modules
 * Installation
 * Application Architecture 
 * Testing
 * Bonus Content
 * FAQ
 * Maintainers
 
 
 INTRODUCTION
------------

This application's goal is to help people manage the chores and tasks of an apartment. It is a terminal application that connects to a mongodb database.



 * This application was developed in PyCharm, recommended that be used to debug but not by any means required
   
   
REQUIREMENTS
------------

This application requires the following modules:

 * pymongo
 * mongoengine
 * tqdm
 * colorama
 * python-dateutil
 * switch
 * certifi
 * chardet
 * urllib3
 * six
 * setuptools 
 
 For this application to work it also requires that mongodb be installed and running, and that python3 be installed.
 For info on installing python look [here](https://realpython.com/installing-python/) and for info on mongodb look here
 [here](https://docs.mongodb.com/manual/administration/install-community/) 
 
 
 INSTALLATION
------------
 
Note: these setup instruction are mac specific, but can be applied to windows with little to no changes.
1. make sure you have python installed on you're machine (can check by going to the terminal and typing in python --version or python3 --version) if not installed, install 

2. next make sure you have pip installed (pip for python3 can check by running pip --version or pip3 --version)

3. then navigate to the folder "jason_tandem_challenge" in your terminal

4. Now if you want to set up a virtual environment 
in your terminal type in "python3 -m venv .env --copies" --copies only required on macOS, if you don't want to ignore 
this step (ignoring is not recommended) 

5. then type "pip3 install -r requirements.txt" and hit return

6. navigate in the Roommate_Helper/src (in the terminal this is done with "cd src")

7. then run the app with python3 program.py

To see the entire schedule for the sprint when prompted hit enter r in the terminal (for run application). Next, 
entire v in the terminal when prompted for View schedule. The user is all pairings for each sprint
or to view the pairings for a specific sprint. 

 
 
APPLICATION ARCHITECTURE/DESCRIPTION
------------
###  Apartment Management
The goal of this application is to add the user in managing one too many apartments. An apartment consists of occupants 
and tasks; it is important to note that the user does not need to be an occupant to manage the apartment. Tasks can be
recurring or one offs, decided by the user upon task creation. 



TESTING
------
After running the application enter "t" in the terminal to enter testing mode. 

FAQ
---

Q: Does this application work on windows? <br/>
A: Yes it does. However, for best UI experience we recommend that you use a mac due to added text coloring that is not 
guaranteed to function properly in windows.

Q: The test in the terminal is hard to see, is there any way to change that? <br/>
A: This might be due to the fact that your terminal background color is white. It is an aesthetically better 
experience if your terminal's background is not set to the default white but rather black. 

Q: Whe I first try to run this program I get this error in the terminal 'No connection could be made because the 
target machine actively refused it', how do i fix this? <br/>
A: This is probably because you do not have mongodb installed and if you do have it installed you do not have it 
running. Look at the link provided above for installing it and if you need help starting it look 
[here for windows](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/) and 
[here for mac](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)

MAINTAINERS
-----------

Current maintainers:
 * Jason Vallee - last updated November 2, 2020


 
 
 
 
