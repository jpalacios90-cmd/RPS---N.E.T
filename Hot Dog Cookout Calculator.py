serving=10
calories=300
number_of_cookies=input("Enter the number of cookies:")
number_of_cookies=int(number_of_cookies)
serving_per_cookies= (number_of_cookies*serving)/40
calories_eaten= serving_per_cookies*calories
print("The calories count is",calories_eaten)
