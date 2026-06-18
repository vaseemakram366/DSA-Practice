# : Determine whether a year is a leap year.





# year = int(input("Enter a year: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")



def divisible_by_3_and_5(num):
    return num % 3 == 0 and num % 5 == 0

def atm_withdrawal(balance, amount):
    return amount <= balance

def admission_eligible(marks, sports_quota):
    return marks >= 70 or sports_quota

def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)