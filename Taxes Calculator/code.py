'''
$0
$9,700
10% of the amount over $0
$9,700
$39,475
$970 plus 12% of the amount over $9,700
$39,475
$84,200
$4,543 plus 22% of the amount over $39,475
$84,200
$160,725
$14,382 plus 24% of the amount over $84,200
$160,725
$204,100
$32,748 plus 32% of the amount over $160,725
$204,100
$510,300
$46,628 plus 35% of the amount over $204,100
$510,300
no limit
$153,798 plus 37% of the amount over $510,300
'''
import math
x = float(input("What is your 2019 taxable income?"))
x1 = ((x * 0.1) * 100)/x
x2 = ((970 + ((x - 9700) * 0.12)) * 100)/x
x3 = ((4543 + ((x - 39475) * 0.22)) * 100)/x
x4 = ((14382 + ((x - 84200) * 0.24)) * 100)/x
x5 = ((32748 + ((x - 160725) * 0.32)) * 100)/x
x6 = ((46628 + ((x - 204100) * 0.35)) * 100)/x
x7 = ((153798 + ((x- 510300) * 0.37)) * 100)/x
if x <= 9700:
    print("Your tax liability is",'${:,.2f}'.format(x * 0.1))
    print("Your effective tax rate is",str(float('{:.1f}'.format(x1)))+'%')
elif x <= 39475:
    print ("Your tax liability is",'${:,.2f}'.format(970 + ((x - 9700) * 0.12)))
    print("Your effective tax rate is",str(float('{:.1f}'.format(x2)))+'%')
elif x <= 84200:
    print ("Your tax liability is",'${:,.2f}'.format(4543 + ((x - 39475) * 0.22)))
    print("Your effective tax rate is",str(float('{:.1f}'.format(x3)))+'%')
elif x <= 160725:
    print("Your tax liability is",'${:,.2f}'.format(14382 + ((x - 84200) * 0.24)))
    print("Your effective tax rate is",str(float('{:.1f}'.format(x4)))+'%')
elif x <= 204100:
    print("Your tax liability is",'${:,.2f}'.format(32748 + ((x - 160725) * 0.32)))
    print("Your effective tax rate is",str(float('{:.1f}'.format(x5)))+'%')
elif x <= 510300:
    print("Your tax liability is",'${:,.2f}'.format(46628 + ((x - 204100) * 0.35)))
    print("Your effective tax rate is",str(float('{:.1f}'.format(x6)))+'%')
elif x > 510300:
    print("Your tax liability is",'${:,.2f}'.format(153798 + ((x- 510300) * 0.37)))
    print("Your effective tax rate is",str(float('{:.1f}'.format(x7)))+'%')
