from random import randint

unsorted_db = []
sorted_db = []

# adds numbers to the unsorted list
for i in range(5):
  unsorted_db.insert(i, randint(1, 10))
  i += 1

print(f"Unsorted List: {unsorted_db}")
print(f"Sorted List: {sorted_db}")

# put first number into the sorted list
sorted_db.insert(0, unsorted_db[0])
unsorted_db.pop(0)

print(f"Unsorted List: {unsorted_db}")
print(f"Sorted List: {sorted_db}")

# sorting logic
while len(unsorted_db) != 0:
  i = 0
  j = 0

  if unsorted_db[i] < sorted_db[j]:
    sorted_db.insert(j, unsorted_db[i])
    unsorted_db.pop(i)

    print(f"Unsorted List: {unsorted_db}")
    print(f"Sorted List: {sorted_db}")

  elif unsorted_db[i] > sorted_db[j]:
    if len(sorted_db) == 1:
      j += 1
      sorted_db.insert(j, unsorted_db[i])
      print(f"Unsorted List: {unsorted_db}")
      print(f"Sorted List: {sorted_db}")

    else:
      while unsorted_db[i] > sorted_db[j] and j < len(sorted_db):
          j += 1
    
      sorted_db.insert(j + 1, unsorted_db[i])
      unsorted_db.pop(i)

    print(f"Unsorted List: {unsorted_db}")
    print(f"Sorted List: {sorted_db}")

  elif unsorted_db[i] == sorted_db[j]:
    j += 1

    sorted_db.insert(j, unsorted_db[i])
    unsorted_db.pop(i)

    print(f"Unsorted List: {unsorted_db}")
    print(f"Sorted List: {sorted_db}")