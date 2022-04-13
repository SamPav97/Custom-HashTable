# Custom-HashTable
Creating my own HashTable (Dictionary) and unit testing its functionalities.


HashTable class should have the needed functionality for a hash table, such as:
•	hash(key: str) - a function that should figure out where to store the key-value pair
•	add(key: str, value: any) - adds a new key-value pair usign the hash function
•	get(key: str) - returns the value corresponding to the given key
•	additional "magic" methods, that will make the code in the example work correctrly
The HashTable should have an attribute called array of type: list, where all the values will be stored. Upon initialization the default length of the array should be

After each addition of an element if the HashTable gets too populated, double the length of the array and re-add the existing data.
