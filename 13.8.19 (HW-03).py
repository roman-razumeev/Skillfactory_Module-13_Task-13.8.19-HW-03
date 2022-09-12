full_price = 1390   # От 25 лет — полная стоимость 1390 руб.
middle_price = 990  # От 18 до 25 лет — 990 руб.
total_sum = 0       # Переменная расчета общей стоимости
visitor_age = 0     # Переменная для хранения возраста посетителя

# Firstly, request the total amount of tickets:
total_tickets = int(input("\nPlease input the total amount of tickets which "
                          "you are wish to buy: "))
# Basic block - calculate a total sum:
for i in range(1, total_tickets+1):
    visitor_age = int(input(f"Please input the age of visior {i}: "))
    if visitor_age >= 26:  # verification > 25
        total_sum += full_price
    elif 18 <= visitor_age <= 25:  # # verification - from 18 to 25
        total_sum += middle_price

# Check the discount condition and display the payment:
if total_tickets >= 3:  # check the discount possibility
    print(f"Congratulation, "
          f"You are the not small company, therefore, got the discount 10 %!!!\n"
          f"The total payment is {int(total_sum * 0.9)} rub")
else:
    print (f"The total payment is {int(total_sum)} rub")









