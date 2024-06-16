numbers = [3, 1, 4, 1, 5, 9, 2]

# Predictions
# 1. numbers[0]
# Predicted value: 3
# Should print 3

# 2. numbers[-1]
# Predicted value: 2
# Should print 2

# 3. numbers[3]
# Predicted value: 1
# Should print 1

# 4. numbers[:-1]
# Predicted value: [3, 1, 4, 1, 5, 9]
# Should print [3, 1, 4, 1, 5, 9]

# 5. numbers[3:4]
# Predicted value: [1]
# Should print [1]

# 6. 5 in numbers
# Predicted value: True
# Should print True

# 7. 7 in numbers
# Predicted value: False
# Should print False

# 8. "3" in numbers
# Predicted value: False
# Should print False

# 9. numbers + [6, 5, 3]
# Predicted value: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# Should print [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"
numbers[-1]=1
print(numbers[2:])
print( 9 in numbers)
