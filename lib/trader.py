from random import randint

def generate_price_list(size, min_price, max_price):
    """Generate a list of random prices."""
    return [randint(min_price, max_price) for _ in range(size)]

def calculate_highest_benefit(prices):
    """Calculate the highest benefit from buying and selling on different days."""
    highest_benefit = 0
    buy_day = -1
    sell_day = -1
    
    #Setting the deficit for each day i, day 0 = first element of the list being substracted to the benefits
    for i in range(len(prices)):
        deficit = prices[i]

    #Then j is the day we sell, we will add the value associated to the index j to the deficit defined just above via buy_price
        for j in range(i + 1, len(prices)):
            profit = prices[j]
            benefit = profit - deficit
    #Still in the same loop, we will set the highest_benefit value if the actual benefit is higher than the actual highest benefit and we store the days
            if benefit > highest_benefit:
                highest_benefit = benefit
                buy_day = i
                sell_day = j

    return highest_benefit, buy_day, sell_day

def print_results(prices, highest_benefit, buy_day, sell_day):
    """Print the results in a formatted manner."""
    print(f"Given the list: {prices}")
    print("The highest benefit is:", highest_benefit, "euros")
    print(f"Buy on day {buy_day} for {prices[buy_day]}")
    print(f"Sell on day {sell_day} for {prices[sell_day]}")

def main():
    size = 10
    min_price = 0
    max_price = 150
    price_list = generate_price_list(size, min_price, max_price)
    highest_benefit, buy_day, sell_day = calculate_highest_benefit(price_list)
    print_results(price_list, highest_benefit, buy_day, sell_day)

if __name__ == "__main__":
    main()
