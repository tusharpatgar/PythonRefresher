# print("What's Peanut butter without",end=" ")
# print("jelly? Nothing!")


# Season= "Summer"

# lucky_number= 7

# hard_math= 3+4+5

# my_str= "3"

# my_num= int(my_str)

# # fancy_name="Tushar"

# # print(Season,lucky_number,hard_math,my_str,type(my_num))

# # print(fancy_name)

# a=int("xyz")

# print(a)


#functiions 
# def print_syntax():
#     pass

# def addition():
#     print(5+7)

# def substraction(x: int,y: int)->int:
#     z= x- y
#     print("Substraction of ",x," & ",y," is ",z)
# print_syntax()
# addition()
# substraction(10,5)


# def p(text):
#     print(text)

# a="Hello"
# p(str(a))


# def mul(x :int,y: int) ->int:
#     z=x*y
#     return z

# mul(10,2)
# print("Multiplication ",mul(10,3))

# #exercise
# def easy_money():
#     return 100

# def best_foof_ever():
#     return "sushi"

# def convert_to_currency(x: float):
#     return "$"+str(x)

# print(easy_money())
# print(best_foof_ever())
# print(convert_to_currency(15.0))

#default arguments
def string_adder(x="",y=""):
    print(x+y)

string_adder("Hello","World")
string_adder("Emilio","estevez")
string_adder()
string_adder("tiger")

def mul(x=1,y=1,z=1):
    print(x*y*z)

mul(2,2,2)
mul()
mul(3)
mul(2,5)