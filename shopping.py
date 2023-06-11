def shopping(services):
    print("Hello and welcome to the Zero Shopping Abyss!")
    print("We are providing the following services. Feel free to purchase anything as prices are flexible.")
    
    bill = 0
    purchased_items = {}
    
    print("Available items and their prices:")
    for item, price in services.items():
        print(f"{item}: {price} rupees")
    
    while True:
        choice = input("Enter the number corresponding to the item you want to purchase (or 'x' to exit): ")
        
        if choice.isdigit():
            choice = int(choice)
            if choice < 0 or choice >= len(services):
                print("Invalid choice. Please select a valid item.")
                continue
            
            item = list(services.keys())[choice]
            price = list(services.values())[choice]
            bill += price
            print(f"{item} added to your cart for {price} rupees.")
            purchased_items[item] = price
        
        elif choice.lower() == "x":
            while True:
                final_choice = input("Are you sure you want to exit? (Y/N): ")
                if final_choice.lower() == "y":
                    print(f"Here's the list of items you've purchased and your total bill is {bill}:")
                    for item, price in purchased_items.items():
                        print(f"{item}: {price} rupees")
                    try:
                        enter_bill = int(input("Enter the bill amount: "))
                        while enter_bill != bill:
                            if enter_bill == bill:
                                print("Thanks for shopping! Come again soon!")
                                return
                            elif enter_bill > bill:
                                print(f"Please receive your change of {enter_bill - bill} rupees.")
                                return
                            elif enter_bill < bill:
                                pending = bill - enter_bill
                                enter_remaining = int(input(f"{pending} rupees is still pending. Please enter the remaining amount: "))
                                enter_bill += enter_remaining
                                print(f"You have paid {enter_bill} rupees.")
                    except ValueError:
                        print("Enter a valid numeric value for the bill.")
                        return
                else:
                    print("Enter a valid choice.")
                if final_choice.lower() == "y":
                    print("Thanks for shopping")
                    quit()

services = {
        "Soap": 50,
        "Milk": 100,
        "Butter": 120,
        "Cream": 200,
        "Ice-cream": 250,
        "Nutella": 500,
        "T-shirts": 700,
        "P-caps": 450,
        "Watch": 400,
        "Glasses": 600,
        "Books": 550,
        "Hoodies": 800,
        "Stationary_kit": 1200,
        "Sweet_box": 2000
    }
shopping(services)
