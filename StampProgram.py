"""
Program: Determine the proper number of stamps for a letter

Start
Obtain the number of Sheets (Sheets)                                ----  input
Set the number of stamps to Sheets /5                               ----  process
Round the number of stamps up to a whole number                     ----  process
Display the number of stamps                                        ----  output

End
"""




Number_Of_Sheets = eval(input("What is the number of sheets of paper? "))               #Step 1 

NUmber_Of_Stamps = Number_Of_Sheets/5                                                   #Step 2

print("The number of Stamps needed for " + str(Number_Of_Sheets) + " Sheets is " + str(NUmber_Of_Stamps) + " Stamps.")    #Step 4
