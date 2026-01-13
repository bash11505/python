#1st programme
value = "apple"
hash_value = hash(value)

print("Original value:", value)
print("Hashed value:", hash_value)

#2nd programme
num = 12345
print("hash of numbers",hash(num))

#3rd programme
items = ["apple","orange","banana"]
for item in items:
    print(item,"->",hash(item))

    #4th programme
    hash_table = {
    "id": 101,
    "name": "VRAM",
    "city": "elul"
}

key = "name"

if key in hash_table:
    print("Found:", hash_table[key])
else:
    print("Not Found")
