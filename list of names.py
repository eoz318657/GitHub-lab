def find_name(names_list, target_name):
    if target_name in names_list:
        print(names_list.index(target_name))
    else:
        print("Not Found")

# Example usage:
names = ["Alice", "Bob", "Charlie", "David"]
find_name(names, "Bob")    # Output: 1
find_name(names, "Eve")    # Output: Not Found