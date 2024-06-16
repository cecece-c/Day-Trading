# Import 'os', 'sys' and 'time' libraries
import os, sys, time


# Get current working directory of script and store value in 'current_working_directory' (String)
current_working_directory = os.path.dirname(sys.argv[0])
current_working_directory = current_working_directory.replace("c:", "") + "/"


# Store value of trade number count in 'trade_number' (Integer)
trade_number = 1


while True:
    # Get action and store value in 'action' (String)
    while True:
        try:
            print("\nEnter '0' to exit program.")
            action = input("\nBuy / Sell: ")
            if action == "0":
                print("\nProgram exiting...")
                for delay in range(5):
                    time.sleep(1)
                sys.exit()
            elif action == "Buy" or action == "Sell":
                break
            else:
                print("\nInvalid input. Only the listed options are accepted.")
        except ValueError:
            print("\nInvalid input. Only integers are accepted.")


    # Get symbol name of share purchased or sold, average fill price of share(s) purchased or sold, quantity of shares purchased or sold, and transaction fee of trade, and store values in 'symbol_name' (String), 'average_fill_price' (Float), 'quantity_of_shares' (Float) and 'transaction_fee' (Float) respectively
    while True:
        try:
            if action == "Buy":
                symbol_name = input("\nEnter symbol name: ").upper()
                average_fill_price = float(input("\nEnter average fill price of share(s) purchased: $"))
                if average_fill_price > 0:
                    quantity_of_shares = float(input("\nEnter quantity of share(s) purchased: "))
                    if quantity_of_shares > 0:
                        transaction_fee = float(input("\nEnter transaction fee of trade: $"))
                        if transaction_fee >= 0:
                            break
                        else:
                            print("\nInvalid input. Only numbers above or equal to 0 are accepted.")
                    else:
                        print("\nInvalid input. Only numbers above 0 are accepted.")
                else:
                    print("\nInvalid input. Only numbers above 0 are accepted.")
            elif action == "Sell":
                print("\nEnter '0' to exit program.")
                symbol_name = input("\nEnter symbol name: ").upper()
                if symbol_name == "0":
                    print("\nProgram exiting...")
                    for delay in range(5):
                        time.sleep(1)
                    sys.exit()
                average_fill_price = float(input("\nEnter average fill price of share(s) sold: $"))
                if average_fill_price > 0:
                    quantity_of_shares = float(input("\nEnter quantity of share(s) sold: "))
                    if quantity_of_shares > 0:
                        transaction_fee = float(input("\nEnter transaction fee of trade: $"))
                        if transaction_fee >= 0:
                            break
                        else:
                            print("\nInvalid input. Only numbers above or equal to 0 are accepted.")
                    else:
                        print("\nInvalid input. Only numbers above 0 are accepted.")
                else:
                    print("\nInvalid input. Only numbers above 0 are accepted.")
        except ValueError:
            print("\nInvalid input. Only numbers are accepted.")


    # Calculate total price of share(s) purchased or sold, and store value in 'total_price' (Float)
    if action == "Buy":
        total_price = average_fill_price * quantity_of_shares + transaction_fee
    elif action == "Sell":
        total_price = average_fill_price * quantity_of_shares - transaction_fee


    # Write trade record to file 'Trade Record - {} - {}.txt'
    with open(f"{current_working_directory}Trade Record - {action} - {trade_number}.txt", "w") as filekey:
        filekey.write(f"Symbol name: {symbol_name}\nAverage fill price: ${round(average_fill_price, 2):.2f}\nQuantity of shares: {round(quantity_of_shares, 2):.2f}\nTransaction fee: ${round(transaction_fee, 2):.2f}\nTotal price of shares: ${round(total_price, 2):.2f}")
        print(f"\nTrade record has been generated and written to {current_working_directory}Trade Record - {action} - {trade_number}.txt.")
        trade_number += 1
