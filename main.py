z = ["яблоко", "апельсин", "банан", "кот"]

def length(list):
    return sorted(list, key=len)

print(length(z))
