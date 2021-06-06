#  and, or y not
#  and
resultado_final = True and True and 200 > 100 #False 10 > 20
print(resultado_final)

# or
resultado_final = True or True or 200 > 400 #False 10 > 20
print(resultado_final)

resultado_final = True and (False or 200 > 100) #False 10 > 20
print(resultado_final)

# not
resultado_final = not True
print(resultado_final)
