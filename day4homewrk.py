class items():
    def __init__(self, store, items, country='United States'):
        self.store = store
        self.item = items
        self.country = country
        self.depth_chart = {}
        self.number_of_items = 0
    
    def additems(self):
        cart = input('What would you like to add to your cart? ')
        price = int(input(f'What will the price be {cart} ? '))
        self.depth_chart[cart] = price
        self.number_of_items += 1 
        print(f'{cart} has been added to the store!')
        print(f'Your current items is {self.depth_chart}')
    
    def deleteitems(self):
        deleteitem = input('What item would you like to delete? ')
        print(f'{self.depth_chart[deleteitem]} has been removed from the roster!')
        del self.depth_chart[deleteitem]
    
    def showlist(self):
        print(f'You currently have {self.number_of_items} in your shopping cart! ')
        print(f'---------- Current items for the {self.store} {self.item}! -----------------')
        for key,value in self.depth_chart.items():
            print(key,value)
        


shoppinglist1 = items('products', 'price')

def shopper():
    while True:
        user_choice = input('What would you like to do with your shopping cart? (add,delete,show, or quit)? ')
        if user_choice == 'quit':
            shoppinglist1.showlist()
            print('Enjoy your items come back soon!')
            break  
        elif user_choice == 'add more items':
            shoppinglist1.additems()
        elif user_choice == 'delete':
            shoppinglist1.deleteitems()
        elif user_choice == 'show':
            shoppinglist1.showlist()
        else:
            print('Not a valid option, please try again')

shopper()

shoppinglist1.store = 'Harris'
