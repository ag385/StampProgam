"""
Program: Determine the proper number of stamps for a letter

Start
Obtain the number of Sheets (Sheets)                                ----  input
Set the number of stamps to Sheets /5                               ----  process
Round the number of stamps up to a whole number                     ----  process
Display the number of stamps                                        ----  output

End
"""
#Test input number 16 should output 3.2 and round up to 4


import math
number_of_sheets = 16                                                                   #Step 1 
number_of_stamps = number_of_sheets/5                                                   #Step 2
round_stamps = math.ceil(number_of_stamps)                                              #Step 3
print("The sheets of paper is " + str(number_of_sheets) + ".")                          
print("The number of stamps needed is " + str(round_stamps) + ".")                      #Step 4



