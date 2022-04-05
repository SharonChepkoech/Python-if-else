print("Welcome to the game!")

playing = input("Do you wnat to play? ")
# print(playing)
score = 0

if playing.lower() != "yes":
    # if they type anything otehr than yes, you quit the program
    quit()

print("Okay, let the games begin!")
# use .lower() so that whatever answe the user inpts is converted 
# to lowercase and therefore meeting the specified requirement
answer = input("What year are we in? ")
if answer.lower() == "2022":
# if answer != 2022:
    print("Correct! Let's proceed")
    score +=1
else:
    print("That is incorect!")

    
    
answer = input("How many letters does the word Kenya have? ")
if answer.lower()  == "5":

    print("Correct! Let's proceed")
    score +=1
else:
    print("That is incorect!")

answer = input("Who is the current Kenyan president? ")
if answer.lower()  == "Uhuru Kenyatta":

    print("Correct! Let's proceed")
    score +=1
else:
    print("That is incorect!")

answer = input("What year did Kenya get its independence? ")
if answer.lower()  == "1963":
    print("Correct! Let's proceed")
    score +=1
else:
    print("That is incorect!")

print("you got " + str(score)+ " questions corect!")
print("you got " + str((score/4)*100)+ "%!")
