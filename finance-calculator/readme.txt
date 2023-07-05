This is somple calculator program, that calculates Bond or Investment result.
Options:

Bond:
result = (i * P)/(1 - (1 + i)**(-n))
P’ is the present value of the house.
● ‘i’ is the monthly interest rate, calculated by dividing the annual
interest rate by 12. Remember to divide the interest entered by
the user by 100 e.g. (8 / 100) before dividing by 12.
● ‘n’ is the number of months over which the bond will be repaid.

Investment:
-simple_result = P*(1 + r*t)
-complex result = P(1 + r)^t ------- A = P * math.pow((1+r),t)
‘r’ is the interest entered above divided by 100, e.g. if 8% is entered,
then r is 0.08.
● ‘P’ is the amount that the user deposits.
● ‘t’ is the number of years that the money is being invested.
● ‘A’ is the total amount once the interest has been applied.
