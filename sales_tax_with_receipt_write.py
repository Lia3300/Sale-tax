
import os

def clear():
      os.system("clear")

def get_state():
      print("Enter the two-letter abbreviation of the state where you are making the purchase:")
      state = input().upper()
      return state

def set_tax_rate(state):
      tax_rates = {
          "AL": 0.04,
          "AK": 0.00,
          "AZ": 0.056,
          "AR": 0.065,
          "CA": 0.0725,
          "CO": 0.029,
          "CT": 0.0635,
          "DE": 0.00,
          "FL": 0.06,
          "GA": 0.04,
          "HI": 0.04,
          "ID": 0.06,
          "IL": 0.0625,
          "IN": 0.07,
          "IA": 0.06,
          "KS": 0.065,
          "KY": 0.06,
          "LA": 0.04,
          "ME": 0.055,
          "MD": 0.06,
          "MA": 0.0625,
          "MI": 0.06,
          "MN": 0.06875,
          "MS": 0.07,
          "MO": 0.04225,
          "MT": 0.00,
          "NE": 0.055,
          "NV": 0.0685,
          "NH": 0.00,
          "NJ": 0.06625,
          "NM": 0.05125,
          "NY": 0.04,
          "NC": 0.0475,
          "ND": 0.05,
          "OH": 0.0575,
          "OK": 0.045,
          "OR": 0.00,
          "PA": 0.06,
          "RI": 0.07,
          "SC": 0.06,
          "SD": 0.04,
          "TN": 0.07,
          "TX": 0.0625,
          "UT": 0.0485,
          "VT": 0.06,
          "VA": 0.053,
          "WA": 0.065,
          "WV": 0.06,
          "WI": 0.05,
          "WY": 0.04,
      }
      return tax_rates.get(state, None)  

def get_num_items():
      while True:
          try:
              num_items = int(input("Enter the number of items you wish to purchase: "))
              if num_items <= 0:
                  raise ValueError("Number of items must be greater than 0.")
              return num_items
          except ValueError as e:
              print(f"Invalid input: {e}. Please enter a valid number.")

def get_item_cost():
      while True:
          try:
              cost = float(input("Enter the cost of the item: "))
              if cost < 0:
                  raise ValueError("Cost cannot be negative.")
              return cost
          except ValueError as e:
              print(f"Invalid input: {e}. Please enter a valid cost.")

def calculate_sales_tax(tax_rate, cost):
      sales_tax = cost * tax_rate
      return sales_tax

def calculate_total_cost(cost, sales_tax):
      total_cost = cost + sales_tax
      return total_cost

def get_items(tax_rate):
      item_prices = []
      item_tax_amounts = []
      item_totals = []

      num_items = get_num_items()

      for _ in range(num_items):
          cost = get_item_cost()
          item_prices.append(cost)

          tax = calculate_sales_tax(tax_rate, cost)
          item_tax_amounts.append(tax)

          total = calculate_total_cost(cost, tax)
          item_totals.append(total)

      return num_items, item_prices, item_tax_amounts, item_totals

def print_receipt(num_items, item_prices, item_tax_amounts, item_totals):
      print("\nReceipt:")
      for i in range(num_items):
          print(f"Price: ${item_prices[i]:.2f}")
          print(f"Tax: ${item_tax_amounts[i]:.2f}")
          print(f"Total: ${item_totals[i]:.2f}")
          print("-" * 20)

def run():
      clear()  
      state = get_state() 
      tax_rate = set_tax_rate(state)  

      if tax_rate is None:
          print("Invalid state abbreviation entered. Please try again.")
          return

      num_items, item_prices, item_tax_amounts, item_totals = get_items(tax_rate)  
      print_receipt(num_items, item_prices, item_tax_amounts, item_totals) 

if __name__ == "__main__":
      run()

 
