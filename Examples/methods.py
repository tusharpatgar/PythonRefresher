# # text="google chrome"
# # print(text.find("o"))

# def vowel_count(text:str):
#     # print(text.count("a")+text.count("e")+text.count("i")+text.count("o")+text.count("u"))
#     count=0
#     for chars in text:
#         if chars in "aeiou":
#             count += 1
#     print(count)

# vowel_count("estate")
# vowel_count("helicopter")
# vowel_count("ssh")


# def find_my_letter(text,find_ele):
#     # return text.find(find_ele)
#     # for char in text:
#     #     if char == find_ele:
#     #         return text.find(find_ele)

#     for index, char in enumerate(text):
#         if char==find_ele:
#             return index
#     return -1


# print(find_my_letter("dangerous","a"))
# print(find_my_letter("bazooka","z"))
# print(find_my_letter("lollipop","z")) # -1 means no element found


# def fancy_cleanup(str):
#     # return str.strip().replace("g","z").replace(" ","!")
#     start=0
#     while len(str)>start and str[start]== " ":
#         start +=1

#     end=len(str)-1
#     while start<=end and str[end]== " ":
#         end -= 1

#     strip_str=str[start:end+1]
#     new_Str= ""
#     for char in strip_str:
#         if char==" ":
#             new_Str +="!"
#         elif char=="g":
#             new_Str += "z"
#         else:
#             new_Str +=char

#     return new_Str

# print(fancy_cleanup("       geronimo crikey  "))
# print(fancy_cleanup("       nonsense  "))       
# print(fancy_cleanup("grade"))


# def multiplication_table(x: int):
#     for i in range(10,0,-1):
#         print(f"{x} * {i}=",x*i)

# multiplication_table(5)

# if True:
#     print("hrellp")

# if False:
#     print("Bivctj")