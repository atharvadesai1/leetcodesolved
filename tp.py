# ***********************************************************
# name = "atharva"
# solution = set()

# def subsequene(index, s):
#     if index == len(name):
#         solution.add(s)
#         s = ''
#         return 

#     subsequene(index+1, s + name[index])
#     subsequene(index+1, s)
#     return solution

# ans = subsequene(0, '')
# print(list(ans))
# ***********************************************************



# ***********************************************************
# name = "atharva"
# solution = set()

# def subsequene(index, s):
#     if index == len(name):
#         solution.add(s)
#         s = ''
#         return 

#     subsequene(index+1, s + name[index])
#     subsequene(index+1, s)
#     return solution

# ans = subsequene(0, '')
# print(list(ans))
# ***********************************************************



# ***********************************************************
## If lenght of string is two
# name = "atharva"
# solution = set()

# def subsequene(index, s):
#     if index == len(name):
#         if len(s) == 2:
#             solution.add(s)
#         return 
    

#     subsequene(index+1, s + name[index])
#     subsequene(index+1, s)
#     return solution

# ans = list(subsequene(0, ''))
# print(ans)
# print(len(ans))
# ***********************************************************



# ************************************************************
name = "abcdefghijklmnopqrstuvwxyz"
k = int(input("Enter the value of k: "))
solution = set()

def subsequene(index):
    if index == len(name)-k+1:
        return 
    
    solution.add(name[index:index+k])
    subsequene(index+1)
    return solution

ans = list(subsequene(0))
print(ans)
print(len(ans))
# ********************************************