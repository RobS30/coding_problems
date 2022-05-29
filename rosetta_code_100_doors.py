# There are 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, visit every door and 'toggle' the door (if the door is closed, open it; 
# if it is open, close it). The second time, only visit every 2nd door (i.e., door #2, #4, #6, ...) and toggle it. The third time, visit every 3rd door (i.e., door #3, #6, #9, ...), etc., 
# until you only visit the 100th door.

# Implement a function to determine the state of the doors after the last pass. Return the final result in an array, with only the door number included in the array if it is open.

#getFinalOpenedDoors should be a function.
# getFinalOpenedDoors should return an array.


# **** incomplete *** 

def getFinalOpenedDoors(numDoors):
    doors = []
    i = 1
    ii = i * i

    while ii <= numDoors:
        doors.append(ii)
        i += 1
        ii = i * i
        return doors




if __name__ == "__main__":
    print(getFinalOpenedDoors(100))
    
