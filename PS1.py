## PS1a: Months to save for a down payment
#  annual_salary = input("What is your annual salary? ")
# portion_saved = input("What is the portion of your salary to be saved? ")
# total_cost = input("What is the cost of your dream home? ")
#
# portion_down_payment = float(0.25)
# current_savings = float(0)
# r = float(0.04)
# mon = 0
#
# print current_savings
#
# print total_cost*portion_down_payment
# print current_savings
# while current_savings<total_cost*portion_down_payment:
#     return_invest = float(current_savings*r/12)
#     current_savings += float(portion_saved*annual_salary/12+return_invest)
#     mon += 1
# print "Number of months: ", mon


## PS1b: Salary increase
# annual_salary = input("What is your annual salary? ")
# portion_saved = input("What is the portion of your salary to be saved? ")
# total_cost = input("What is the cost of your dream home? ")
# semi_annual_raise = input("What is your semi-annual raise? ")
#
# portion_down_payment = float(0.25)
# current_savings = float(0)
# r = float(0.04)
# mon = 0
#
# print current_savings
#
# print total_cost*portion_down_payment
# print current_savings
# while current_savings<total_cost*portion_down_payment:
#     return_invest = float(current_savings*r/12)
#     current_savings += float(portion_saved*annual_salary/12+return_invest)
#     mon += 1
#     if mon%6 == 0:
#         annual_salary *= (1+semi_annual_raise)
# print "Number of months: ", mon

## PS1c
def months_to_save(annual_salary, portion_saved):
    current_savings = 0
    semi_annual_raise = 0.07
    r = 0.04
    portion_down_payment = 0.25
    total_cost = 1000000
    mon = 0
    while current_savings<total_cost*portion_down_payment:
        return_invest = float(current_savings*r/12)
        current_savings += float(portion_saved*annual_salary/12+return_invest)
        mon += 1
        if mon%6 == 0:
            annual_salary *= (1+semi_annual_raise)
    return mon

diff = 100
annual_sal = 150000
save_percent = 5000
bi_step = save_percent
ct = 0
months = months_to_save(annual_sal,float(save_percent)/10000)

while months != 36:
    ct += 1
    bi_step /= 2
    print bi_step
    months = months_to_save(annual_sal,float(save_percent)/10000)
    if months > 36:
        save_percent = save_percent+bi_step
    if months < 36:
        save_percent = save_percent-bi_step
    if ct == 1000:
        print "Not possible to save that much on your salary"
        break
print float(save_percent)/10000
print ct


