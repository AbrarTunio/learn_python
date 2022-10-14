def greet(name):
    print("Welcome", name)

# greet("Abrar")
# greet("Zamin")
# greet("Abdul")

def greet2(name):
    return "Welcome" + name

# greet2("Abrar")

#Apply Print function on greet 2
# print(  greet2("Abrar")  )
#Apply max function on greet 2
big_val =  max( greet2("Abrar")  ) 
# print(big_val) 
#Apply len function on greet 2
length =  len( greet2("Abrar")  ) 
# print(length) 



def myFunction( num ):
    print(num + num)
    print(num - num)
    print(num * num)


# myFunction(6)

def order (n):
    print("welcome" ,n ,"would you want to have tea" , n)

order("Abrar")
order("Suleman")


def ask(msg):
    print("Length of your message is: ", len(msg))

ask("In which class do you study")








