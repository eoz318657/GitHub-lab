# List a single most frequent word
from ctypes import HRESULT

words1 = ["apple", "banana", "apple", "orange", "banana", "apple", "grape"]

print("Example 1:")
print(f"Word list:{words1}")
print(f"Most frequent word(s): {HRESULT}")
print(f"frequency: {words1.count(HRESULT[0])}")
print()