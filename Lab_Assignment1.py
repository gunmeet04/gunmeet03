#Project1

print("solving Q1", '\n')
inpnum1 = int(input("Enter first no."))
inpnum2 = int(input("Enter second no."))
inpnum3 = int(input("Enter third no."))
avg = (int(inpnum1) + int(inpnum2) + int(inpnum3)) / 3
print("The average of three numbers are:",(avg), '\n')


#Project2
print("solving Q2", '\n')
print('''Please adhere to the following instructions for calculating the Income Tax:
      • All taxpayers are charged a flat tax rate of 20%.
      • All taxpayers are allowed a $10,000 standard deduction.
      • For each dependent, a taxpayer is allowed an additional $3,000 deduction.
      • Gross income must be entered to the nearest penny.''')

tax_rate = 0.2
standarad_deduction = 10000
more_deduction = 3000
gross = int(input("Please enter your Gross Income:"))
dependents = int(input("Please enter no. of dependents:"))
taxable_Income = (int(gross) - int(standarad_deduction) - (int(more_deduction) * int(dependents)))
tax = (int(taxable_Income)*float(tax_rate))
print("Your Income Tax value is:", (tax), "$",'\n')


#Project3
print("solving Q3", '\n')
print("This is your final list of semester 1 result."
      "So please enter all the particulars sincerely")

Sid = int(input(("Please Enter Your SID:")))
name = input("Please Enter Your Name:")
gender = input("Please Enter Your Gender:")
course_name = input("Please Enter Your Course Name:")
cgpa = float(input("Please Enter Your CGPA:"))

students_list = [Sid, name, gender, course_name, cgpa]
print("Student" + str(students_list), '\n')

#Project4
print("solving Q4", '\n')
m1 = int(input("Enter your marks student 1:"))
m2 = int(input("Enter your marks student 2:"))
m3 = int(input("Enter your marks student 3:"))
m4 = int(input("Enter your marks student 4:"))
m5 = int(input("Enter your marks student 5:"))

marksList = [m1, m2, m3, m4, m5]
marksList.sort()
print(marksList,'\n')


#Project5
# removing the elements of a given list.
print("solving Q5", '\n')
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("The provided list is ", color, '\n')

# removing the 4th term and returning modified list
color.pop(3)
print(" The modified list  is color 1 =", color)

# replacing 'Black' and 'Pink' with 'Purple'
color2 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color2[3:5] = ['Purple']
print("The modified list is color 2 =", color2)
