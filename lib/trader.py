#Pour chaque élément de la liste, soustraire élément à variable(bénéfice) puis ajouter les autres éléments à bénéfice.
#Retourner la meilleure paire.
price_list = [17, 3, 6, 9, 15, 8, 6, 1, 10]

def day_trader(prices):
  benefits = 0
  for price in prices:
    price_index = prices.index(price)
    benefits -= price

    print(f"Actualized list : {prices}")
  
day_trader(price_list)

