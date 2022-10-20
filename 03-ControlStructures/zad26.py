pin_code = "0805"
att = ""
count = 0

for i in range(3):
    att = input("Enter the PIN code: ")
    if att == pin_code:
        print("Accepted")
        break
    else:
        print("Incorrect...") 
        count += 1   
if(count == 3):
    print("Sorry, your payment card has been blocked.")