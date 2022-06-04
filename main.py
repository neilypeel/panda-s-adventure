def say_hello():
    print("Hello Panda!")


if __name__ == '__main__':
    say_hello()


# def name():
#    return name


def sara():
    action = input(
        "you walk up to sara, she hasnt noticed but she has been eating pizza and there is pizza crust on the floor. \n\n to the back of you there is the kitchen doorway leading into the hall ")
    if action == "back":
        hallway()

    else:
        print("hmm ok")
    actions_dict = {
        "examine": 'You see that sara is still on her phone,"jeez, hello??, i want some attention here, or some food at least! \n\n You look around on the kitchen floor, you see the small piece of pizza crust, and your food and water bowls by the kitchen unit on the left, you could getting saras attention by barking? she looks like she isnt in the mood for playing though. lets see what you can figure out',
        "take pizza": "You approach the table slowly, sara doesn't look up from her phone. \n\n Reaching for the pizza crust, you grab it slowly and slip out back into the hallway.",
        "bark": "You summon up all the strength you have and let out an extremely loud yap.",
        "ask to go out": "You stomp your feet and start sobbing. "}

    while True:
        action = input("whats your move? e.g. examine,take pizza, bark, ask to go out")
        if action in actions_dict.keys():
            print(actions_dict[action])
            if action == "take pizza":
                print("sara didnt notice a thing! i'm such a smartass.")
                print(
                    "to the right of you is the hallway and straight ahead in the kitchen there is sara. \n\n you can see food and water bowls, and treats.\n")
                kitchen()
            elif action == "ask to go out":
                print(
                    "sara shouts neil to ask him to take you outside, then she realises he is not home. \n\n she looks annoyed and sighs and gets up and walks to the main apartment door and opens it")
                main_apartment_door()

            elif action == "bark":
                game_over(
                    "Unfortunately it didnt impress sara at all. \n\n she picks you up and puts you back in the living room and closes the door on you. \n<GAME OVER>")
            # elif action == "examine":
            # kitchen()
            else:
                print("hmm ok")


def game_over(why):
    print("{}. end of game!".format(why))

    exit(0)


def kitchen():
    bowls = ["bone", "food", "water", "treats"]
    print(
        "You are now in the kitchen. a room with a water and food bowl on the left, and sara straight ahead, sat down at the table by the window.")
    print("whats your next move?")
    action = input("... ")
    if action == "hallway":
        hallway()
    if action == "forward":  # straight ahead
        sara()  # sara

    if action in ["bowl", "examine", "left"]:
        print("Oooh, treats! dog food! water! i wonder if i should take a sniff to investigate")

        print("whats your next move?")
        choice = input("... ")

        if choice == "sniff":
            print("Let's see what we have here..")
            print("You take a few steps towards the bowls and take a few sniffs with your little nose")
            print("You find the following items")
        else:
            print('hmm ok..\n\n')
            kitchen()
        # while True:
        #        if choice == True:

        #  print('hmm ok..\n\n')
        #  kitchen()

        for food in bowls:
            print(food)

        print("What do you want to do?")
        num_items_in_bowls = len(bowls)

        print(f"try all {num_items_in_bowls} food and drink items separately, some will help you, some wont!")
        print("leave it")

        bowl_choice = input("... ")
        if bowl_choice == "treats":
            bowls.remove("treats")
            bowls_2 = bowls[0:4]
            print("you now have the following items left..")
            print(bowls_2)
            print("\tYou devour the treats thats been left for you.")
            print("\tWoohoo! I'd rather eat some of my favorite carbs, but this will do just fine!")

        if bowl_choice == "water":
            bowls.remove("water")
            bowls_2 = bowls[0:4]
            print("you now have the following items left..")
            print(bowls_2)
            print("\tYou drink the water thats been left for you.")
            print("\tWoohoo! I just peed on the floor.")
            game_over("sara goes mad and locks you in the living room")

        if bowl_choice == "food":
            bowls.remove("food")
            bowls_2 = bowls[0:4]
            print("you now have the following items left..")
            print(bowls_2)
            print("\tYou tuck into your lunch. your tummy is heavy after all that food..")
            print("\tWoohoo! time for a sleep.")
            game_over("no more adventure for you sleepyhead")

        if bowl_choice == "bone":
            bowls.remove("bone")
            bowls_2 = bowls[0:4]
            print("you now have the following items left..")
            print(bowls_2)
            print("\tYou take the bone. I'll save this for later! could come in handy, you think to yourself")
            kitchen()

            # temp_food_list = bowls[:]
            # other_bowls = ", ".join(bowls)
            # print(f"\tYou also go for the {other_bowls}.")

            # for food in temp_food_list:
            # Use list remove() function to remove each item
            #   bowls.remove(food)

            #  bowls.append("bone")
            # print(f"\tYou decide to save the {bowls} for later.")
            #  print("Now lets see what i can do to pass the time")
        elif bowl_choice == "leave it":
            print("not feeling hungry right now, unless theres carbs involved, of course!, let's get out of here")
        else:
            print("Well, not sure what you mean there")
    else:
        print("Sorry, i dont know what you mean?")

        # else:
        #   print("Well, not sure what you mean there")
        #   sara()
    kitchen()


def hallway():
    print(
        "you are now in the hallway of the apartment. In front of you is the main apartment door and to the left is the kitchen.")
    next_move = input("... ")

    if "left" in next_move:
        kitchen()
    elif "straight ahead" in next_move:
        print("the main apartment door appears to be closed")
        hallway()
    else:
        print("Sorry, i dont know what you mean?")
        hallway()


# answer = 'yes'
# while answer == 'yes':
#   answer = input('Shall I continue? ')
# print('I have stopped')

def main_apartment_door():
    print("You see some stairs leading down to the outside, and 3 other apartment doors.\n\n")
    print(
        "Well the neighbours arent at home, and I don't care for them much anyway, they never give me treats! \n\nHmmm should i see whats going on downstairs..\n\n")
    print("Do you go downstairs or back into the hallway?")

    next_move = input("... ")

    if "downstairs" in next_move:
        downstairs()

    elif "hallway" in next_move:
        hallway()
    else:
        print("Ah well.. I think I'll just sleep a little longer! until next time...")
        exit(0)


def downstairs():
    print("you see peter the cat sat on the stairs")
    action = input(
        "you walk up to peter, he stares at you ")
    if action == "back":
        main_apartment_door()
    elif action == "drop bone":
        print("peter looks at the bone in terror, shits himself and runs away\n\n")
        print("you head down the staircase into the courtyard")
        courtyard()

    else:
        print('peter attacks you\n\n')
        print('game over')
        exit()


def courtyard():
    #        items = ["ber", "note", "treat"]
    print("you are now in the courtyard\n")
    print("you see ber sat in the garden")
    #        for name in items:
    #            print(name)
    print("whats your next move?")
    action = input("... ")
    if action == "ber":
        ber()



    else:
        print('ber smiles and says hello but looks busy and walks away\n\n')
        print('game over')
        exit()


def ber():
    action = input(
        "you walk up to ber, he smiles and stroke your head. hello panda, what can i do for you? he says.. ")
    if action == "bark":
        print(
            "ber says , panda can i put this piece of paper with a list of records?? \n\n i would like to borrow the records from neil for my party tonight?\n\n")

        f = open('/Users/apple1/Downloads/Untitled 2.txt', 'r')
        for line in f:
            print(line)
        c = f.read()
        number = len(c)
        print(number)
        print("ber gives you the paper and a treat! he walks away\n\n\n")
        courtyard()


def start_adventure():
    print("You are in the living room, to the side there is a door that leads into the hallway")
    door_picked = input("what do you want to do?")

    if door_picked == "hallway":
        print("You picked the hallway")
        hallway()

    else:
        print("Sorry, i dont know what you mean?")
        start_adventure()


def name():
    return name


def main():
    panda_mood = input("How are you feeling today?? Can you give me one word to describe? ")
    print(f"Panda replies...{panda_mood}")
    print(f"Okaaay so, you are feeling {panda_mood} huh? ")
    print("do you feel like going on a little adventure..?")
    panda_answer = input("yes or no")
    if panda_answer == "yes":
        print("ok! lets do this")
        print("You have just woke up from a beautiful dream and a long sleep..")
        start_adventure()

    else:
        print('ok, one of those days huh, fair enough')

    print("\nThe end\n")
    print(f"Thanks for playing, {name}")


if __name__ == '__main__':
    main()