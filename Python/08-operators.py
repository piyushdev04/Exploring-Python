print(5+2) #add
print(5-2) #sub
print(5*2) #multiply
print(5/2) #divide
print(5//2) #if we don't want num after point 
print(5%2) #modules for remainder
print(5**2) #5 to the power 2

#shortcuts
i = 5
i += 2
i -= 2
i *= 2

#Operator Precedence
result = 2 + 3 / 5 # "*" , "/" have higher precedence in python
print(result)

# Comparison Operators
print(3>2)
print(3<2)
print(3<=2)
print(3>=2)
print(3 == 2)
print(3 == 3)
print(3 != 2)
print(3 != 3)

#Logical Operators
# "OR" T or T = T, T or F = T, F or F = F
print(2 > 3 or 2 > 1)
print(2 > 3 or 2 > 8)

# "AND" T and T = T, T and F = F, F and F = F
print(3 > 2 and 2 > 1)
print(3 > 2 and 2 > 6)

# "NOT" T = F, F = T
print(not 3 > 2)
print(not 3 > 4)