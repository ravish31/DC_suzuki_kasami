DEPENDENCY:
Python 3.x
* python 3.8.10 was used to test the app.

USAGE:
python3 DC_suzuki_kasami.py

The application depends on user input

On running the user will get a prompt to Request CS, Release CS & End execution.


======================================================================================================
7 sites in distributed system numbered 0...6

DISPLAYING STATE OF THE SYSTEM
------------------------
privileged_site : 0

TOKEN :
Token Queue : empty
Token LN Array: [0, 0, 0, 0, 0, 0, 0]
S0_RN Array :   [0, 0, 0, 0, 0, 0, 0]
S1_RN Array :   [0, 0, 0, 0, 0, 0, 0]
S2_RN Array :   [0, 0, 0, 0, 0, 0, 0]
S3_RN Array :   [0, 0, 0, 0, 0, 0, 0]
S4_RN Array :   [0, 0, 0, 0, 0, 0, 0]
S5_RN Array :   [0, 0, 0, 0, 0, 0, 0]
S6_RN Array :   [0, 0, 0, 0, 0, 0, 0]
---------------------------

Please enter the operation
1. Req for Requesting CS
2. Rel for releasing CS
3. End to terminate the program
=======================================================================================================

* if user inuputs Req, then site id will be asked in the following manner 

========================================================

Please enter the operation
1. Req for Requesting CS
2. Rel for releasing CS
3. End to terminate the program

Req
Enter Site id which is requesting CS

3(example)
========================================================



*For releasing the CS the user has to input Rel, then the site id will be asked in the following manner

========================================================
Please enter the operation
1. Req for Requesting CS
2. Rel for releasing CS
3. End to terminate the program

Rel
Enter Site id which needs to exit CS

3(example)
========================================================

Since there is no CS to execute the release command has to be provided by end user
-> The end user can provide Rel & Req command multiple times for different sites in any order to test.
-> At every step the state of system will be displayed in the following manner.
-> The state includes the site holding the token, Token queue, LN array and RN array for all sites. 

========================================================
DISPLAYING STATE OF THE SYSTEM
------------------------
privileged_site : 0

TOKEN :
Token Queue : empty
Token LN Array: [0, 0, 0, 0, 0, 0, 0]
S0_RN Array :   [0, 0, 0, 0, 0, 0, 0]
S1_RN Array :   [0, 0, 0, 0, 0, 0, 0]
S2_RN Array :   [0, 0, 0, 0, 0, 0, 0]
S3_RN Array :   [0, 0, 0, 0, 0, 0, 0]
S4_RN Array :   [0, 0, 0, 0, 0, 0, 0]
S5_RN Array :   [0, 0, 0, 0, 0, 0, 0]
S6_RN Array :   [0, 0, 0, 0, 0, 0, 0]
---------------------------
========================================================

To end the execution simply input End.