# We're expecting an integer instead of a float. This shows an exception
integer_result = 7 / 0 #Exception occurs when the code is running
print(integer_result)

# Explanation of explicit is better than implicit
"""
for i in range(5):
    if i % 2 == 0:
        print(i, end=" ")

print()

complex_ = [i for i in range(5) if i % 2 == 0]
print(*complex_)
"""