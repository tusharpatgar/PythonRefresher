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

# #default arguments
# def string_adder(x="",y=""):
#     print(x+y)

# string_adder("Hello","World")
# string_adder("Emilio","estevez")
# string_adder()
# string_adder("tiger")

# def mul(x=1,y=1,z=1):
#     print(x*y*z)

# mul(2,2,2)
# mul()
# mul(3)
# mul(2,5)



# """String Methods"""

# def long_word(text: str) -> bool:
#     if len(text)<7:
#         print(False)
#     else:
#         print(True)
#         #return len(text)>7

# long_word("Python")
# long_word("magnificient")

# def first_longer_than_second(a: str,b: str) -> bool:
#     print("True" if len(a)>len(b) else "False")
#     #return len(a)>len(b)

# first_longer_than_second("Python","Ruby")
# first_longer_than_second("cat","mouse")
# first_longer_than_second("steven","seagal")



# def same_fisrt_same_last_letter(text: str):
#     return text[0]==text[-1]

# print(same_fisrt_same_last_letter("runner"))
# print(same_fisrt_same_last_letter("Runner"))     
# print(same_fisrt_same_last_letter("clock"))     
# print(same_fisrt_same_last_letter("q"))

# def three_number_sum(x: str)->str:
#     #total=0
#     return int(x[0]) + int(x[1]) + int(x[2])
#     """
#     for i in range(len(x)):
#         total = total + int(x[i])

#     for digit in x:
#         total += int(digit)
#     """

# print(three_number_sum("123"))
# print(three_number_sum("567"))
# print(three_number_sum("444"))
# print(three_number_sum("000"))


# s="make"
# print(s[0:5:2])


# def first_three_characters(text: str):
#     return text[:3]

# print(first_three_characters("dyn"))
# print(first_three_characters("emp"))


# def last_five_charcaters(text: str):
#     return text[::-2]


# print(last_five_charcaters("dynasty"))
# print(last_five_charcaters("empire"))


# # def is_palindrome(text: str):
# #     return text[:]==text[::-1]

# # print(is_palindrome("racecar"))
# print(is_palindrome("yummy"))


# s="commando"
# print("and" in s)

# 0

# mand

# ville

# dest

# \n -end line 
# \t - Tab

# len

# concatenate

# e

print("misfortune"[10])