import csv
import random

def create_market_basket_csv(filename, item_names):
    num_transactions = 1000
    num_items = len(item_names)
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header row
        header_row = ['TransactionID'] + item_names
        writer.writerow(header_row)
        
        for transaction_id in range(num_transactions):
            # Generate a random transaction with sparse boolean values
            transaction = [transaction_id] + ['1' if random.random() < 0.1 else '0' for _ in range(num_items)]
            writer.writerow(transaction)

    print("CSV file '{}' created successfully.".format(filename))



item_names = ['Apple', 'Banana', 'Orange', 'Mango', 'Grapes', 'Eggs', 'Yogurt', 'Cheese' , 'salt', 'sugar']  # Replace with your own item names
create_market_basket_csv('market_basket.csv', item_names)

