# Insertion Sort

Takes a list of numbers and sorts the list by inserting the numbers into the right spots.

## Necessities for sorting

For this algorithm to sort the list you need 2 lists. A ```sorted_list``` and an ```unsorted_list```. Make sure that your unsorted list has numbers in it.
You can do that one of the following ways:

1. Adding random numbers.
   This method can be done in a for loop and might look similar to this:
   ```
   for i in range(10):
     unsorted_list.append(i, randint(1, 10)
     i += 1
   ```
   if you choose to import the whole ```random``` library, than it will look slightly different in the sense that the ```randint()``` function will be written as ```random.randint()``` instead because you are importing the whole library, not just one specific function from the library.
   
3. Manual input.
   This method is done when creating your variables.
   ```
   unsorted_list = [4, 3, 1, 0, 0, 8, 7, 1, 6, 2, 5]
   ```
4. User input.
   By simply asking the user for numbers you can collect your data. you can do this in a for loop as well.
   ```
   for i in range(10):
     num = float(input("Enter a random number: "))
     unsorted_list.append(i, num)
     i += 1
   ```
   Just make sure you check that the item input by the user is either a ```float``` or an ```integer```.
