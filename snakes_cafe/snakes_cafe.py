import textwrap


#### Function to display menu ####
def display_menu():

  print (textwrap.dedent( '''**************************************
  **    Welcome to the Snakes Cafe!   **
  **    Please see our menu below.    **
  **
  ** To quit at any time, type "quit" **
  **************************************

  Appetizers
  ----------
  Wings
  Cookies
  Spring Rolls

  Entrees
  -------
  Salmon
  Steak
  Meat Tornado
  A Literal Garden

  Desserts
  --------
  Ice Cream
  Cake
  Pie

  Drinks
  ------
  Coffee
  Tea
  Unicorn Tears

  ***********************************
  ** What would you like to order? **
  ***********************************
  '''))
  
 
    #### Add items ####

def add_item(new_item, dict):

  multiple = ""

  if new_item in dict:
    dict[new_item] = dict[new_item] + 1

    if new_item[-1].lower() != 's':
      multiple= "s"

  else:
    dict[new_item] = 1

  print (f'\n** {dict[new_item]} order of {new_item}{multiple} have been added. **\n')

    

if __name__ == "__main__":
      
  display_menu()

  resume = True
  dict = {}

  while(resume):
      order = input("> ")
      if order.lower().strip() != 'quit':
          add_item(order, dict)
      else: 
            break

