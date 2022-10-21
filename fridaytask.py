name = input("Please enter your name:")
print(f"Hello {name}, welcome to Cian's Restaurant Guide.")


control2 = 0

areacode = int(input("Please enter your areacode (e.g. Dublin 1, Dublin 3) Dublin: "))
if areacode % 2 == control2:
  print(f"Based on your area code being Dublin {areacode}, you will now be redirected to restaurants on the Southside. ")
else:
  print(f"Based on your area code being Dublin {areacode}, you will now be redirected to restaurants on the Northside. ")

# Area code given, now enter your cuisine preference  
print("You will now be given a choice of cuisine. Please choose from the following cuisines: ")
print("Italian, Mexican, Chinese")

preference = input("Please state your preferred cuisine:")
  
if preference == "Italian":
    print("You have chosen Italian as your cuisine of choice ")
    
    if preference == "Mexican":
        print("You have chosen Mexican as your cuisine of choice ")
    
    if preference == "Chinese":
        print("You have chosen Chinese as your cuisine of choice ")
        

# You have chosen your preferred cuisine, now for your budget
italbudget = int(input("Please state an estimate of your budget - what is the max price you are willing to pay for your meal? "))
if italbudget >= 25 and preference == "Italian":
        print("Based on your budget of 25 euros or more pp, we recommend Marco Biancos")
else:
        print("For a budget under 25 euros, we recommend either: Happy Italy or Vapianos")
    
mexbudget = int(input("Please state an estimate of your budget - what is the max price you are willing to pay for your meal? "))
if mexbudget > 25 and preference == "Mexican":
        print("Based on your budget of 25 euros or more pp, we recommend Tucos Tacqueria")
else:
        print("For a budget under 25 euros, we recommend either: Boojum or Tolteca")
        
chibudget = int(input("Please state an estimate of your budget - what is the max price you are willing to pay for your meal? "))
if chibudget > 25 and preference == "Italian":
        print("Based on your budget of 25 euros or more pp, we recommend Tattu")
else:
        print("For a budget under 25 euros, we recommend either: Golden Goose or Siver Duck")

# if preference == "Mexican" and budget > 50:
#     print("Based on your budget of 50 euros or more pp, we recommend Tucos Tacqueria")
# else:
#     print("For a budget under 25 euros, we recommend either: Boojum or Tolteca")

# mexbudget = int(input("Please state an estimate of your budget - what is the max price you are willing to pay for your meal? "))
# if mexbudget >= 100 and preference == "Mexican":
#   print("Based on your budget of 100 euros pp, we recommend Tucos Tacqueria")
# if mexbudget >= 50 and preference == "Mexican":
#   print("Based on your budget of 50 euros pp, we recommend Pablo Picante")
# if mexbudget >= 25 and preference == "Mexican":
#   print("Based on your budget of 25 euros pp, we recommend BurritoLand")
# else:
#   print("For a budget under 25 euros, we recommend either: Boojum or Tolteca")

# chibudget = int(input("Please state an estimate of your budget - what is the max price you are willing to pay for your meal? "))
# if chibudget >= 100 and preference == "Chinese":
#   print("Based on your budget of 100 euros pp, we recommend Tattu")
# if chibudget >= 50 and preference == "Chinese":
#   print("Based on your budget of 50 euros pp, we recommend Golden Dragon")
# if chibudget >= 25 and preference == "Chinese":
#   print("Based on your budget of 25 euros pp, we recommend Silver boat")
# else:
#   print("For a budget under 25 euros, we recommend either: Mama Goose or Happy Dumpling")
