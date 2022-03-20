weeklyorbi = int(input("Do you get paid weekly or biweekly? (1 for weekly, 2 for bi) "))

wage = float(input("Enter Hourly Wage: "))

def weekly():
    sunday = int(input("Enter Hours Worked for Sunday: "))
    monday = int(input("Enter Hours Worked for Monday: "))
    tuesday = int(input("Enter Hours Worked for Tuesday: "))
    wednesday = int(input("Enter Hours Worked for Wednesday: "))
    thursday = int(input("Enter Hours Worked for Thursday: "))
    friday = int(input("Enter Hours Worked for Friday: "))
    saturday = int(input("Enter Hours Worked for Saturday: "))
    
    hours = sunday + monday + tuesday + wednesday + thursday + friday + saturday 

    flat_tax = 0.323

    weekly_paycheck = hours * wage
    paycheck_aftertax = weekly_paycheck * flat_tax

    print("This Pay Period, you worked a total of ", hours, " hours. Before Tax, you should have made about $",weekly_paycheck, ". After tax, you should have made about $", paycheck_aftertax)

def biweekly():
  sunday1 = int(input("Enter Hours Worked for the first Sunday of this pay period: "))
  monday1 = int(input("Enter Hours Worked for the first Monday of this pay period: "))
  tuesday1 = int(input("Enter Hours Worked for the first Tuesday of this pay period: "))
  wednesday1 = int(input("Enter Hours Worked for the first Wednesday of this pay period: "))
  thursday1 = int(input("Enter Hours Worked for the first Thursday of this pay period: "))
  friday1 = int(input("Enter Hours Worked for the first Friday of this pay period: "))
  saturday1 = int(input("Enter Hours Worked for the first Saturday of this pay period: "))
  sunday2 = int(input("Enter Hours Worked for the second Sunday of this pay period: "))
  monday2 = int(input("Enter Hours Worked for the second Monday of this pay period: "))
  tuesday2 = int(input("Enter Hours Worked for the second Tuesday of this pay period: "))
  wednesday2 = int(input("Enter Hours Worked for the second Wednesday of this pay period: "))
  thursday2 = int(input("Enter Hours Worked for the second Thursday of this pay period: "))
  friday2 = int(input("Enter Hours Worked for the second Friday of this pay period: "))
  saturday2 = int(input("Enter Hours Worked for the second Saturday of this pay period: "))
  hours = sunday1 + monday1 + tuesday1 + wednesday1 + thursday1 + friday1 + saturday1 + sunday2 + monday2 + tuesday2 + wednesday2 + thursday2 + friday2 + saturday2

  flat_tax = 0.323

  biweekly_paycheck = hours * wage
  paycheck_aftertax = biweekly_paycheck * flat_tax

  print("This Pay Period, you worked a total of ", hours, " hours. Before Tax, you should have made about $",biweekly_paycheck, ". After tax, you should have made about $", paycheck_aftertax)

if weeklyorbi == 1:
    weekly()
elif weeklyorbi == 2:
    biweekly()
else:
    print("Sup Buddy.")
