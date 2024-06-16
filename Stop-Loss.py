# Import 'sys' and 'time' libraries
import sys, time


while True:
    # Get average fill price of share(s) purchased, quantity of shares purchased and transaction fee of trade, and store values in 'average_fill_price' (Float), 'quantity_of_shares' (Float) and 'transaction_fee' (Float) respectively
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


    # Get maximum acceptable loss and store value in 'maximum_acceptable_loss' (Float)
    while True:
        try:
            maximum_acceptable_loss = float(input("\nEnter maximum acceptable loss: $"))
            if maximum_acceptable_loss >= 0:
                break
            else:
                print("\nInvalid input. Only numbers above or equal to 0 are accepted.")
        except ValueError:
            print("\nInvalid input. Only numbers are accepted.")


    # Calculate stop-loss price to sell each share at and store value in 'stop_loss_price' (Float)
    stop_loss_price = (total_price - maximum_acceptable_loss) / quantity_of_shares


    # Display stop-loss price to sell each share at in 2dp
    print(f"\nStop-loss price to sell each share at: ${round(stop_loss_price, 2):.2f}")


    # Calculate stop-loss percentage and store value in 'stop_loss_percentage' (Float)
    stop_loss_percentage = 100 - (stop_loss_price / (total_price / quantity_of_shares) * 100)


    # Display stop-loss percentage in 2dp
    print(f"\nStop-loss percentage: {round(stop_loss_percentage, 2):.2f}%")
