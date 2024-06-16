# Import 'sys' and 'time' libraries
import sys, time


while True:
    # Get average fill price of share(s) purchased, quantity of shares purchased and transaction fee, and store values in 'average_fill_price' (Float), 'quantity_of_shares' (Float) and 'transaction_fee' (Float) respectively
    while True:
        try:
            print("\nEnter '0' to exit program.")
            average_fill_price = float(input("\nEnter average fill price of share(s) purchased: $"))
            if average_fill_price == 0:
                print("\nProgram exiting...")
                for delay in range(5):
                    time.sleep(1)
                sys.exit()
            elif average_fill_price > 0:
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
        except ValueError:
            print("\nInvalid input. Only numbers are accepted.")


    # Calculate total price of share(s) purchased and store value in 'total_price' (Float)
    total_price = average_fill_price * quantity_of_shares + transaction_fee


    # Get desired profit and store value in 'desired_profit' (Float)
    while True:
        try:
            desired_profit = float(input("\nEnter desired profit: $"))
            if desired_profit >= 0:
                break
            else:
                print("\nInvalid input. Only numbers above or equal to 0 are accepted.")
        except ValueError:
            print("\nInvalid input. Only numbers are accepted.")


    # Calculate take-profit price to sell each share at and store value in 'take_profit_price' (Float)
    take_profit_price = (total_price + desired_profit) / quantity_of_shares


    # Display take-profit price to sell each share at in 2dp
    print(f"\nTake-profit price to sell each share at: ${round(take_profit_price, 2):.2f}")


    # Calculate take-profit percentage and store value in 'take_profit_percentage' (Float)
    take_profit_percentage = (take_profit_price / (total_price / quantity_of_shares) * 100) - 100


    # Display take-profit percentage in 2dp
    print(f"\nTake-profit percentage: {round(take_profit_percentage, 2):.2f}%")
