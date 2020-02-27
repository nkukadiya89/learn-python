#Logical operators
# AND
# OR
# NOT

high_income = True
good_credit = False
student = False

if (high_income or good_credit) and not student:
    print("Approved")
else:
    print("Rejected")   


#Short-circuit Evaluation - When first codition return false then no other codition checked and gives Rejected  as a output
#
# if high_income and good_credit and not student:
#    print("Approved")
# else:
#    print("Rejected")   
       