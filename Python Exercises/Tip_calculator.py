total_bil = float(input("What was the total bill ? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people are splitting the bill ? "))

bill_to_pay = total_bil +  ((total_bil*tip)/100)

print(f"Each person should pay {round(bill_to_pay/people,2)}")