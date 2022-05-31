# RasaChatbot project

## Guide

!! Make sure you install Microsoft C++ Build Tools (Just click "next" for all steps)
https://visualstudio.microsoft.com/visual-cpp-build-tools/


Try and see the installation videos on YT made by Rasa 

## To get started with this project.


### Step 1 - Clone this repo inside a folder of your choosing on your machine.
  
  
### Step 2 - Creating a virtual enviroment & installing dependencies.


  Download & install Miniconda : https://docs.conda.io/en/latest/miniconda.html
  
  Open Powershell which is the most "user-friendly" in my opinion terminal for windows users.
  **Just search in the search bar for "Powershell"


  Inside Powershell type the following comands:


  ### Create the virtual enviroment:
  
    conda init  - should change the begining of the prompt line with (base)
    
    conda create -n rasa30 python==3.8  - creates the env with python 3.8 , the rasa30 is the name of the new vienv
    
    conda activate rasa30  - activates the new enviroment


  ### Installing packages:
    
    conda install ujson
    
    conda install tensorflow
    
    pip install rasa==3.1.0  - after installing check if rasa is 3.0.8 with the command "rasa --version"


  ### Installing packages for Selenium webscrapping (Not enabled anymore as the timetable is empty)
    
    pip install selenium
    
    - download chromedriver from here:
    https://chromedriver.chromium.org/downloads
    *Match the chromedriver with your Google Chrome version
    
    - add the chromedriver in C: (maybe inside a folder) , after that replace the 
    path in actions.py at line 31, with your path to the chromedriver.
    
        
## Step 3 - Running the project in the terminal.
  
  Open 2 powershell teminals inside the folder containing this project
  Type the folling two commands:
  
    rasa run actions  - will run the actions server on one terminal
    
    rasa shell  - you will interact with the bot in the other terminal
