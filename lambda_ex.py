# def mx(x,y):
#     if x > y:
#         return x
#     else:
#         return y

mx = lambda x,y : x if x > y else y

a = int(input("Número x: "))
b = int(input("Número y: "))
print(mx(a,b))