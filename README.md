# Random number generator
# Brief Intro
A random number generation and visualization project.

'Script 1' generate 1000 random number valued between 1-100.

'Script 2' did a calculation based on the result of script 1 and get another 1000 number. 

'Script 3' visualizes the result using result from 1 as x-axis and result from 2 as y-axis.

'/Output' folder contains output result as Json files and one visualized image for script 3 as well.

'script.ipynb' contains visualizations, can be run by Jupyter notebook and Binder.

# Environment requirement
The file "requirements.txt" lists all packages needed to run those scripts. Compare to that list, we only need to do a "pip install Jupyter" and a "pip install matplotlib" by hand, others will be created when you build the enviroment.

The following steps lists all job to be done to create the environment.

1. create a virtual environment using virtualenv, name it as "dsci560H4", see this page:https://docs.python.org/3/library/venv.html 
2. move into the virtual environment folder and go to /scripts folder, run activate.bat to start the environment
![image](/image/4.png)
3. install needed package by hand using following commend while the virtual environment is running: 
![image](/image/9.png)
![image](/image/0.png)
4. excute python scripts, should see the following screen for successfully run script1. 
![image](/image/1.png)
5. before update the repo, add the environment folder to the .gitignore file to avoid uploading it.

# Binder badge to show the notebook
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/alvinzhou66/Random-Number-and-Virtual-Environment/main?filepath=%2Fscript.ipynb)
