# Step-by-step guide to convert a Python script(.py) to an executable(.exe):
# For this:

# First we need to install a package named 'pyinstaller'
# ->pip install pyinstaller
# run this command in the Command prompt and install the package
# Then we are ready to go...

#Then, run your program that you want to convert (from '.py' to '.exe') in your Code Editor's terminal, 
#in that terminal, type...
#       pyinstaller -F .\worksetup_auto.p
#       instead of worksetup_auto.p , youll have to put the name of your Python file, that you want to convert
#       The '-F' flag creates a single, standalone executable file.
# Then successfully the exe file is installed into the directory where our .py file exists
# if we double click on this .exe file, then it'll  start to run the program
#The program should be running without needing Python installed on the machine.
