from helpers import getNum
<<<<<<< HEAD
from random import randint

# STEP 3: Define a randomNumbers function that takes a number as a parameter.
	# STEP 4a: Create an empty array called result
	# STEP 5: Create a loop that runs n times
		# STEP 6: Generate a random number between 0 and 100. Add the number to the result array.
	# STEP 4b: Return the result array variable

# STEP 9: Define a largerThan function that takes an array of numbers and a single number as parameters.
    # STEP 10: Create an empty array called result
    # STEP 11: Create a loop that runs once for each item in the list/array parameter
    	# STEP 12: Write an if statement to test if the current value in the list is greater than the number parameter
    		# STEP 13: If true, write another if statement to test if the current value in the list is not already in the result array
    			# STEP 14: If true, add the current value in the list to the result array
    # STEP 15: Print the list array variable. Label it "List of numbers".
    # STEP 16: Sort the result array variable and print it. Label it "Numbers that are greater than [n]"


def main():
  # STEP 1: Prompt the user for a number between 10 and 20. Assign the user's response to a variable called howMany.
  # STEP 2: Call a randomNumbers function, passing the howMany variable as an argument. Assign the result to a variable called list.
  # STEP 7: Prompt the user for a number between 0 and 100. Assign the user's response to a variable called n.
  # STEP 8: Call a largerThan function, passing the list and n variables as arguments.
=======

def getRainfallData():
	result = [] 
	months = ["March", "April", "May", "June"]
	for i in range(len(months)):
		question = "Enter " + months[i] + "'s rainfall total: "
		result.append(getNum(question, 0.0, 100.0))
	return result

def getSum(rainfallData):
    sum = 0
    for value in rainfallData:
        sum += value
    return sum

def getAverage(sum, count):
    return sum / count

def main():
    rainfall = getRainfallData()
    total = getSum(rainfall)
    average = getAverage(total, len(rainfall))
    print("Total: " + str(total))
    print("Average: " + str(average))
    print("Highest: " + str(max(rainfall)))
    print("Lowest: " + str(min(rainfall)))
  # STEP 16: Print the total, average, highest, and lowest amounts
>>>>>>> 9c7d0a222af0e4d6332910c5e46674cec20bdf9d
  
main()