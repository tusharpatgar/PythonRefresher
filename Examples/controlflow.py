# # def even_odd(a: int):
# #     if a%2==0:
# #         return "Even"
# #     else:
# #         return "Odd"


# # def truthy_falsy(text):
# #     return f"The value {text} is {bool(text)}"

# # print(truthy_falsy(0))
# # print(truthy_falsy(5))
# # print(truthy_falsy("hello"))
# # print(truthy_falsy(""))



# # def negative_energy(number):
# #     if number>=0:
# #         return number
# #     else:
# #         return abs(number)

# # print(negative_energy(5))
# # print(negative_energy(10))
# # print(negative_energy(-5))
# # print(negative_energy(-8))
# # print(negative_energy(0))

# def divisible(number: int)->bool:
#     if number%3==0 and number%4==0:
#         return True
#     else:
#         return False


# print(divisible(3))
# print(divisible(4))
# print(divisible(12))
# print(divisible(18))
# print(divisible(24))

# def string_theory(string: str)->bool:
#     if len(string)>3 and string.startswith("S"):
#         return True
#     else:
#         return False

# print(string_theory("Sansa"))
# print(string_theory("Story"))
# print(string_theory("See"))
# print(string_theory("Fable"))
    
# def multi(num):
#     i=1
#     while i<=10:
#         print(f"{num}X{i}={num*i}")
#         i+=1

# multi(5)

# #reverse sequence
# def reverse(num):
#     # while i<0:
#     #     print(i)
#     #     i-=1
#     # for i in range(num,0,-1):
#     #     print(i)


#     #recursion
#     if num>0:
#         print(num)
#         reverse(num-1)

# reverse(5)


# def reverse_string(str):
#     # print(str[::-1])
#     # for i in range(len(str)-1,-1,-1):
#     #     print(str[i],end="")
#     # print("")
#     # print("".join(reversed(str)))
#     # i=len(str)-1
#     # reverse=""
#     # while i>=0:
#     #     reverse +=str[i]
#     #     i-=1
#     # print(reverse)
#     if len(str)<=1:
#         return str

#     return str[-1] + reverse_string(str[:-1])

# name="Tushar"
# # print(reverse_string(name))
# print(name[:-1])


#Factorial

# def factorial(num):
#     # total=1
#     # for i in range(num,0,-1):# or for i in range(1,num+1)
#     #     total=total*i
#     # return total
#     if num<=1:
#         return num
#     return num* factorial(num-1)


# print(factorial(5))