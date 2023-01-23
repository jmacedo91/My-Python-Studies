#TODO: Create a letter using starting_letter.txt 
with open("Input/Letters/starting_letter.txt") as letter:
    content = letter.read()

#for each name in invited_names.txt
invited_names = list()
with open("Input/Names/invited_names.txt") as names:
    list_names = names.readlines()
    for name in list_names:
        invited_names.append(name.replace("\n", ""))

#Replace the [name] placeholder with the actual name.
for name in invited_names:
    invitation = content.replace("[name]", name)
    with open("Output/ReadyToSend/" + name + "_InvitationCard.txt", mode = "w") as card:
         card.write(invitation)

#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
