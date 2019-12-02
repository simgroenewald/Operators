# Compulsory Task

# Variables for the three times that can be entered by the user in seconds
swimTime = float(input("Please enter your finishing time for the swimming event in minutes:"))
cycleTime = float(input("Please enter your finishing time for the cycling event in minutes:"))
runTime = float(input("Please enter your finishing time for the running event in minutes:"))
position = float (input ("Which position did you place in the triathlon?"))
qualTime = int(100*60)

# Converting the times to seconds
swimInt = int(swimTime)
swimDec = swimTime-swimInt
swimSec = (swimInt * 60) + swimDec

cycleInt = int(cycleTime)
cycleDec = cycleTime-cycleInt
cycleSec = (cycleInt * 60) + cycleDec

runInt = int(runTime)
runDec = runTime-runInt
runSec = (runInt * 60) + runDec

# Adding all three together for the total qualifying time and saving it in string variable aswell as integer variable.
total = (swimSec + cycleSec + runSec)
strtotal = str(total)
print ("Your total time was: " + strtotal +"s") # Not sure if it should display the time in minutes or seconds.

# Else if statements to determine which prize the user gets based on their total time in seconds.
# Making use of and statements in the if statements as both conditions need to be true for the string to print.
if total < qualTime:
    print ("Congradulations! You will recieve provicial colours!")
elif total > qualTime and total < (qualTime + (10*60)):
    print ("Well done! You will recieve half colours.")
elif total > (qualTime + (10*60)) and total < (qualTime + (15*60)):
    print ("Good job. You will recieve a provicial scroll")
elif total > (qualTime + (15*60)) and total < (qualTime + (20*60)):
    print ("You recieve a provincial certificate.")
elif total > (qualTime + (20 * 60)):
    print ("Unfortunately,you do not recieve a prize.")
    

