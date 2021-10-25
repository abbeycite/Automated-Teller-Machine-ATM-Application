# Automated-Teller-Machine-ATM-Application and Banking Package.
# Intro...
This is an Automated Teller Machine(ATM) Application that enables customers to have access to their bank accounts for basic transactions such as checking balance, depositing, withdrawal, and logout functions. The banking application was implemented through the modular programming procedures(modules and packages) for simplicity reasons.
![atmUI](https://user-images.githubusercontent.com/48870117/138626586-35193e9e-aef1-4523-830d-b0ca10af114d.PNG)
# Modular Programming
Modular programming is used to explain the process of breaking a large, unwieldy programming task into separate, smaller, more manageable subtasks or modules. Individual modules can then be cobbled together like building blocks to create a larger application. Functions, modules and packages are all constructs in Python that promote code modularization.
A Python module is a single file, and a package(non-distribution packages) in this context is a folder with potentially multiple files. Having multiples files for project enables us to break our codes into modules that can be accessed through a specific module while using the "from *** import ***" code line at the top of the file. The package is also initializd with __--init__--.py (often pronounced "dunder init", short for "double underscore init double underscore").

![bankingpkg_modules](https://user-images.githubusercontent.com/48870117/138630351-4cd4d8c2-5807-43b5-82a5-1fbd011110b4.PNG)

# Objectives
Amongst others, the primary objective of this project is to enable finger-tips access to banking transactions like checking of account balance before or after a specific deposit/withdrawal transactions. make a deposit, make a withdrawal and perhaps log out of your App after use. Other objectives and processes we want to facilitate includes:

* Ensure the username and pin characters are not null values with caps of 10 and 4 characters respectively
* Validates the login credentials against the registered credentials before proceeding
* Verify that balance after a deposit transaction is correctly updated
* Verify that balance after a withdrawal transaction is also correctly updated.

# Implementation...
For simplicity and to facilitate quick understanding, I have decided to break the implementation processes into steps/tasks:
* Step1:
I started off with the VS code environment by creating two modules, the app.py and the account.py, the account.py is embedded in the banking_pkg(non-distribution package) and it contents are basically the functions that display or return value about balance, deposit, withraw, and logout to the app.py.

![bankingpkg_modules](https://user-images.githubusercontent.com/48870117/138630351-4cd4d8c2-5807-43b5-82a5-1fbd011110b4.PNG)
* Step2:
On the app.py module, I imported the account.py module from the banking_pkg, "from banking_pkg import account" to be able to call functions present in the account.py module into the app.py file. I used the python built-in function, print() to print the User Interface(UI) and familiarize oneself with the applications features and the associated keywords.

![UI_mainfeatures](https://user-images.githubusercontent.com/48870117/138638134-3ba13a5d-42a2-463b-a6d7-6e4d677d81f7.PNG)

* step3:
I used the input() function to prompt user for registeration name, used if-statement to check if name provided is >=1 and <10, if this is false then an error message is printed and the user is prompted to re-enter name that meets this character limit. If this condition is passed then user is prompted to provide a-4 digit PIN and also to check for validity of PIN. if this is also passed then a new message that shows successful regsiterion with the name, and the initialized balance of $0 is printed to the app UI. 

* step4:
Within a while loop, user is prompted to input() corresponding username and PIN that matches the credentials used to register. if this conditions are met, a success message is printed and we break out of the while loop. break, else, an error message is printed and application logs you out.

![step4](https://user-images.githubusercontent.com/48870117/138640772-a1e8ef58-e685-4f64-9c2a-a14e57f2193e.PNG)

* step5: 
While the last step above is validated, the next step, I printed the application features again and prompted the user to choose the number that corresponds to transaction they want to perform with the input() function.
If option "1" is selected, I call the deposit function from the account.py module which also prompt the user to enter an amount to deposit if any and assigned the variable "balance" to value returned from this function. The next line also calls the show_balance function from the account.py module and prints the balance to the screen.
If option "2" is selected, I call the show_balance function from the account.py module to print the previous balance, then call the deposit function to prompt user to enter an amount to deposit if any, this function also return the newly calculated value from adding amount deposited to the previous balance. I assigned the variable "balance" to value returned from this function. The next line also calls the show_balance function from the account.py module and prints the balance to the screen. 
If option "3" is selected, I call the withdraw function from the account.py module which also prompt the user to enter an amount to withdraw if any, this function also return the newly calculated value from subtracting the withdrawn amount from the previous balance. I assigned the variable "balance" to value returned from this function. The next line also calls the show_balance function from the account.py module and prints the balance to the screen after a withdrawal is made.
Finally, when the option "4" is selected, the program breaks out of the while loop statement and terminates to log out.

![step5](https://user-images.githubusercontent.com/48870117/138710093-237cad5a-c12d-4f9e-9ee0-39fae929aad1.PNG)

![step5print](https://user-images.githubusercontent.com/48870117/138710043-569257ef-71c0-4ed2-a4e1-fe0672281e0a.PNG)

# Conclusion: 
The application is still in the development process, and working on improving the features, and functionalities.

P.S: I will gladly welcome any contributions.

# THANK YOU FOR STOPPING BY!!!
# PLEASE SEE SOME OF MY OTHER PROJECTS.

## AUTHOR:
ABIODUN M. ABIDEMI
