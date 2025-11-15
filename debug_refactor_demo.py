# ❌ Buggy function with a logical error
def is_even_buggy(n):
    # This incorrectly returns True for odd numbers
    return n % 2 != 0

# 🧪 Test the buggy function
print("Testing buggy function:")
print("is_even_buggy(2):", is_even_buggy(2))  # Expected: True, Actual: False
print("is_even_buggy(3):", is_even_buggy(3))  # Expected: False, Actual: True

# 🤖 Copilot Suggestion:
# "Did you mean n % 2 == 0 to check for even numbers?"

# ✅ Corrected function
def is_even_fixed(n):
    # This correctly returns True for even numbers
    return n % 2 == 0

# 🧪 Test the fixed function
print("\nTesting fixed function:")
print("is_even_fixed(2):", is_even_fixed(2))  # Expected: True
print("is_even_fixed(3):", is_even_fixed(3))  # Expected: False
