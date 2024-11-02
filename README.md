# Insertion Sort

Takes a list of numbers and sorts the list by inserting the numbers into the right spots.

## Necessities for sorting

For this algorithm to sort the list you need 2 lists. A ```sorted_list``` and an ```unsorted_list```. Make sure that your unsorted list has numbers in it.
You can do that one of the following ways:

1. Adding random numbers.
   This method can be done in a for loop and might look similar to this:
   ```
   for i in range(10):
     unsorted_list.insert(i, randint(1, 10))
     i += 1
   ```
   if you choose to import the whole ```random``` library, than it will look slightly different in the sense that the ```randint()``` function will be written as ```random.randint()``` instead because you are importing the whole library, not just one specific function from the library.
   
2. Manual input.
   This method is done when creating your variables.
   ```
   unsorted_list = [4, 3, 1, 0, 0, 8, 7, 1, 6, 2, 5]
   ```
3. User input.
   By simply asking the user for numbers you can collect your data. you can do this in a for loop as well.
   ```
   for i in range(10):
     num = float(input("Enter a random number: "))
     unsorted_list.insert(i, num)
     i += 1
   ```
   Just make sure you check that the item input by the user is either a ```float``` or an ```integer```.

4. Input from an existing data set.
   ```
   for i in range(len(data_set)):
      unsorted_list.insert(i, data_set[i])
      i += 1
   ```
You will also need a ```while``` loop for the actual sorting process.

## How it works
Take the ```unsorted_list```  and insert the number at index 0 into the index 0 of the ```sorted_list``` and remove that number from the ```unsorted_list```. Then you are going to compare the next number to the number at index 0 of the ```sorted_list``` and check for one of the following:
- The number at index 0 of ```sorted_list``` is greater than the number at index 0 of the ```unsorted_list```
- The number at index 0 of ```sorted_list``` is less than the number at index 0 of the ```unsorted_list```
- The number at index 0 of ```sorted_list``` is equal to the number at index 0 of the ```unsorted_list```

It's then going to check those conditions until it is a position where more than one condition is true, or there are no other spots in front of or behind the number for it to compare itself to.

## Whats it used for
 This is an algorithm used for sorting lists of numbers, but it is also a good way to practice writing algorithms and thinking things through like a computer.
