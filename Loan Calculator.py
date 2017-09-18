import math

def create_table(n,r,pv,P):
    print('%-12s%-12s%-14s%-13s%-12s' % ("Month","Payment","Principle","Interest","Balance"))
    for i in range(1,n+1):
        interest = r * pv
        if pv + interest < P:
            P = pv + interest
        principle = P - interest
        pv = pv - principle
        print('%-12i$%-12.2f$%-12.2f$%-12.2f$%-12.2f' % (i, P, principle, interest, pv))
        
def mode1(pay):
    number_of_months = n = int(input("Amount of months you want to pay this loan off in:"))
    interest_rate = r = float(input("Enter interest rate on this loan i.e. 4.3:"))/1200
    priciple_value = pv = float(input("Enter principle value of loan:"))
    P = (r * pv)/ (1 - (1+r)**-n)
    create_table(n,r,pv,P)
  
def mode2(pay):
    principle_value = pv = float(input("Enter principle value of this loan:"))
    interest_rate = r = float(input("Enter your interest rate on this loan f.e. 4.3:"))/1200
    desired_monthly_payment = P = float(input("Enter your desired monthly payment:"))
    n = math.ceil(math.log((P/(P-r*pv)),(1+r)))
    create_table(n,r,pv,P)   

def interest_calculator():
    print("Hello, welcome to Kevin's loan calculator.")
    print("")
    print("In mode 1 you will be asked to enter the required information to calculate the  approximate amount of money needed to pay off this loan")
    print("")
    print("In mode 2 you will be asked to enter the required information and the amount of time in months to pay off this loan will be calculated")
    print("")
    mode_number = input("Which mode would you like to use Mode 1 or 2?: ")
    if mode_number == "1":
        mode1("pay")
    elif mode_number == "2":
        mode2("pay")
    else:
        print("Please enter a 1 or 2")

interest_calculator()
