#add item to cart
#remove item of order
#detele order
#show order
#out cart

# Declare cart, type(cart)=list
cart = []

# def add item to cart
def def_AddIteam(item):
    cart.append(item)
    print(f'{item} has been added to your cart.')

def def_RemoveItem(item):
    try:
        cart.remove(item)
        print(f'{item} has been removed from the cart.')
    except:
        print('Sorry we couldn\'t remove that item.')

def def_DeteleOder():
    cart.clear()
    print('Your cart is empty')

def def_ShowCart():
    if cart:
        print('Here is your cart')
        ID = 1
        for i in cart:
            print(f'{ID}. {i}')
            ID +=1
    else:
        print('Your cart is empty')

def def_main():
    done = False
    while not done:
        ans =  input('add:1; remove:2; clear:3; quit:4\n').lower()
        if ans =='1':
            item = input('What would you like to add? ').title()
            def_AddIteam(item)
            print('-'*20)
            def_ShowCart()
        elif ans =='2':
            item = input('What would you like to remove? ').title()
            def_RemoveItem(item)
            print('-' * 20)
            def_ShowCart()
        elif ans == '3':
            def_DeteleOder()
            print('-' * 20)
        elif ans == '4':
            done=True

def_main()