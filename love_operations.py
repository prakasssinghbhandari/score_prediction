# name1=input("enter your name\n")
# name2=input("enter your name\n")
def check_love(name1,name2):
     length1=len(name1)
     length2=len(name2)
     diff=length1-length2
     if diff==1 or diff == -1:
      return ("your love percentage is 98%")
     elif diff==2 or diff == -2:

        return ("your love percentage is 8%")


    
     elif diff==3 or diff == -3:

         return("your love percentage is 48%")
     elif diff==4 or diff == -4:

       return("your love percentage is 58%")
     else:
      return("unmatched")


#     love="98%"
#     return love
# elif diff=="2":
#     love="93%"
#     return love
#     elif diff=="3":
#         love="88%"
#         return love
#     elif diff=="4":
#         love="49%"
#         return love
#     elif diff=="5":
#         love="25%"
#         return love
#     else:
#         return("imperfect match")
# print(check_love(name1,name2))


