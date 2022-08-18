def taking_the_square_root(N) -> int:
    '''Return integer square_root N if there is a root else None'''
    try:
        my_square_root = N ** 0.5
        if type(my_square_root) == complex:
            return None
    #print(my_square_root)
        checking_for_an_integer = int(my_square_root)
        if checking_for_an_integer == my_square_root:
           return checking_for_an_integer
        else:
           return None
    except TypeError:
        print('pass a number')
   



if __name__ == '__main__':
    print(taking_the_square_root(25))
    print(taking_the_square_root(36))
    print(taking_the_square_root(121))
    print(taking_the_square_root(-121))
    print(taking_the_square_root(300))
    print(taking_the_square_root(24))
    print(taking_the_square_root(21))
    print(taking_the_square_root('asdqed'))
