
#code to calculate gross pay and overtime pay

hrs = float(input("Enter Hours worked:"))
rate = float(input("enter rate per hour"))

if hrs <= 40:
    grossPay = hrs * rate
else:
    regular_pay = 40 * rate
    overtime_pay = (hrs - 40) * (rate * 1.5)
    total = regular_pay + overtime_pay
    print(total)
