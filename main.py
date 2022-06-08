def say_hello():
    print("Hello Panda!")


if __name__ == '__main__':
    say_hello()


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

            else:
                print("hmm ok")

other_things =["note"]

def ber():
    global other_things
    print(
        "you walk up to ber, he smiles and gently strokes your head. 'hello panda, what can i do for you?' , he says.. ")
    actions_dict = {
        "examine": 'ber seems to be busy with something\n\n You look around the courtyard smelling the grass, hmm do you need to poop panda?',
        "bark": "ber says , 'panda can i give you this piece of paper with a list of records??' \n\n 'i would like to borrow the records from neil for my party tonight..'\n\n",
        "poop": "ber looks at you in a disgusted manner and storms off. "}

    while True:
        action = input("whats your move? e.g. examine, bark, poop")
        if action in actions_dict.keys():
            print(actions_dict[action])
            if action == "poop":
                exit()
            elif action == "examine":
                courtyard()

            elif action == "bark":
                other_things.append("note")
                print(
                    "he puts a note in your collar with writing scrawled on it.. \nit seems to be some kind of list of neil's music, maybe i should keep this..\n\n")
                f = open('/Users/apple1/Downloads/Untitled 2.txt', 'r')
                for line in f:
                    print(line)
                c = f.read()
                number = len(c)
                print(number)
                print(
                    "ber gives you the paper and a treat! he gets up and opens the building front entrance door and leaves\n\n")

                print(
                    "you now sniff around on the ground, do a few twirls and take a poop.. \nyou now decide to walk closer to the front entrance, still in the courtyard")
                # front_entrance()

            # else:
            # print("hmm ok")
            # courtyard()
    action = input("what do you want to do now panda?")
    if action == "forward":
        front_entrance()

    if action == "back":
        downstairs()
    else:

        print("hmm ok")
        courtyard()


def game_over(why):
    print("{}. end of game!".format(why))

    exit(0)


bowls = []


def kitchen():
    global bowls
    items = ["food", "treats", "water", "bone"]
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

        if choice in ["sniff", "examine", "sniff bowl", "examine bowl", 'go to bowl']:
            print("Let's see what we have here..")
            print("You take a few steps towards the bowls and take a few sniffs with your little nose")
            print("You find the following items")
        else:
            print('hmm ok..\n\n')
            kitchen()
        for stuff in items:
            print(stuff)
        for food in bowls:
            print(food)

        print("What do you want to do?")
        num_items_in_bowls = len(items)

        print(f"try all {num_items_in_bowls} food and drink items separately, some will help you, some wont!")
        print("leave it")
        while True:
            bowl_choice = input("... ")
            if bowl_choice == "take treats":
                items.remove("treats")
                bowls.append("treats")
                bowls_2 = bowls[0:4]
                print("you see following items..")
                print(bowls_2)
                print("\tYou devour the treats thats been left for you.")
                print("\tWoohoo! I'd rather eat some of my favorite carbs, but this will do just fine!")

            elif bowl_choice == "take water":
                items.remove("water")
                bowls.append("water")
                bowls_2 = bowls[0:4]
                print("you now have the following items left..")
                print(bowls_2)
                print("\tYou drink the water thats been left for you.")
                print("\tWoohoo! I just peed on the floor.")
                game_over("sara goes mad and locks you in the living room")

            elif bowl_choice == "take food":
                items.remove("food")
                bowls.append("food")
                bowls_2 = bowls[0:4]
                print("you now have the following items left..")
                print(bowls_2)
                print("\tYou tuck into your lunch. your tummy is heavy after all that food..")
                print("\tWoohoo! time for a sleep.")
                game_over("no more adventure for you sleepyhead")

            elif bowl_choice == "take bone":
                items.remove("bone")
                bowls.append("bone")
                bowls_2 = items[0:4]
                print("you now see the following items in the kitchen:\n")
                print(bowls_2)
                print("\tYou take the bone. I'll save this for later! could come in handy, you think to yourself")

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
                kitchen()
        return bowls  # else:
        # print("Sorry, i dont know what you mean?")

    # kitchen()
    # print("whats your next move?")
    # action = input("... ")
    # if action == "hallway":
    # hallway()
    # if action == "forward":  # straight ahead
    # sara()  # sara


def hallway():
    print(
        "you are now in the hallway of the apartment. In front of you is the main apartment door and to the left is the kitchen.")
    next_move = input("... ")

    if "left" in next_move:
        kitchen()
    elif "forward" in next_move:
        print("the main apartment door appears to be closed")
        hallway()
    else:
        print("Sorry, i dont know what you mean?")
        hallway()


def main_apartment_door():
    print("You see some stairs leading down to the outside, and 3 other apartment doors.\n\n")
    print(
        "Well the neighbours arent at home, and I don't care for them much anyway, they never give me treats! \n\nHmmm should i see whats going on downstairs..\n\n")
    print("Do you go downstairs or back into the hallway?")

    next_move = input("... ")

    if "down" in next_move:
        downstairs()




    elif "hallway" in next_move:
        hallway()
    else:
        print("Ah well.. I think I'll just sleep a little longer! until next time...")
        exit(0)


items = []
other_things = ["note"]


def downstairs():
    global items
    global other_things

    print("you see peter the cat sat on the stairs")
    output = bowls, items

    print("you have the following items..")
    print(output)

    action = input("you walk up to peter, he stares at you ")
    if action == "up":
        main_apartment_door()
    elif action == "drop bone":
        bowls.remove("bone")
        print("you have the following items..")
        print(output)
        print("peter looks at the bone in terror, shits himself and runs away\n\n")
        print("you head down the staircase into the courtyard")
        courtyard()

    if action == "scratch door":
        items.remove("flowers")
        print("you scratch on carolin's door for help..\ncarolin open's the door and milo the cat comes out into the hallway..\n")
        print("milo attacks peter. you continue upstairs and back into the apartment\n")
        final_installment()
    if items.remove != ("flowers"):
        print("nobody opens the door..\n")
        downstairs()

    else:
        print('peter attacks you\n\n')
    print('game over')
    exit()
    downstairs()

    downstairs()


def courtyard():
    global items
    print("you are now in the courtyard\n in front of you there is an open door leading to the front entrance")
    print("you see ber sat in the garden")

    print("whats your next move?")
    action = input("... ")
    if action == "back":
        downstairs()
    if action == "forward":
        print("the front entrance door to the apartment building seems to be closed")
        courtyard()
    if action == "poop":
        print("you take a dump and ber looks at you in disgust")
        exit()
    # if action == "ber":
    #    ber()
    if action in ["go to ber", "walk to ber", "ber", "see ber"]:
        ber()

    else:
        print('ber smiles and says hello but looks busy and walks away\n\n')
        print('game over')
        exit()

other_things =[]
items = []
shopping_bag_items = ["toy", "sausages", "flowers", "butter", "bread", "sweet potato", "newspaper"]


def front_entrance():
    global items
    global shopping_bag_items
    # output = items, shopping_bag_items
    # return output

    print("You are just outside the front entrance looking out onto the street.\nyou see various familiar faces\n")
    print("'ooh look! someone left a bag of shopping by the bus stop! what should i do..'?\n ")
    # print("you are currently carrying the following items:")
    # print(items)
    print("whats your next move?")
    action = input("... ")
    if action in ["examine", "bag", "examine bag", "go to bag", "sniff", "sniff bag"]:
        print("you get closer to inspect whats been left in the bag.")

        for stuff in shopping_bag_items:
            print(stuff)
        num_of_items = len(shopping_bag_items)

        print(f"there seems to be {num_of_items} items in the bag on the floor ")

        while True:
            item_choice = input("... ")
            if item_choice == "take sausages":
                shopping_bag_items.remove("sausages")
                items_2 = shopping_bag_items[0:6]
                print("you now have the following items left..")
                print(items_2)
                print("\tYou devour the sausages.")
                print("\tyummy! why cant i have these to eat all the time?!")

            if item_choice == "newspaper":
                shopping_bag_items.remove("take newspaper")
                items_2 = shopping_bag_items[0:6]
                print("you now have the following items left..")
                print(items_2)
                print("\tYou tear the newspaper to bits.")
                print("\tWell.. that was fun!")
                game_over("the person on the street gets mad and chases you back into the building")

            if item_choice == "take toy":
                shopping_bag_items.remove("toy")
                items_2 = shopping_bag_items[0:6]
                items.append("toy")
                print(items_2)
                print("\tYou take the toy..")
                print("you are now carrying the following items")
                print(items)

            if item_choice == "take butter":
                shopping_bag_items.remove("butter")
                items_2 = shopping_bag_items[0:6]
                print("there are now the following items left..")
                print(items_2)
                print("\tYou take a big bite out of the cube of butter, 'eww no thanks' ")

            if item_choice == "take flowers":
                shopping_bag_items.remove("flowers")
                items_2 = shopping_bag_items[0:6]
                items.append("flowers")
                print("you now have the following items left..")
                print(items_2)
                print("\tYou smell the flowers, very nice! .")
                print("you are now carrying the following items:")
                print(items)

            if item_choice == "take bread":
                shopping_bag_items.remove("bread")
                items_2 = shopping_bag_items[0:6]
                print("you now have the following items left..")
                print(items_2)
                print(
                    "\tYou eat the bread.. that is a LOT of bread you just ate panda, not good.\nyou decide to call it a day with the adventure and laze in the garden")
                game_over()

            if item_choice == "take sweet potato":
                shopping_bag_items.remove("sweet potato")
                items_2 = shopping_bag_items[0:6]
                items.append("sweet potato")
                print("you now have the following items left..")
                print(items_2)
                print("\tthese will do for my weekly groceries!.")
                print("you are now carrying the following items:")
                print(items)
            else:
                break
    print("in front you see some people outside the shop, and somebody who looks familiar riding a bike\n")
    print("behind you there is the front entrance leading into the courtyard\n")
    action = input("... ")
    if action == "back":
        courtyard()
    if action == "forward":
        neil()


def neil():
    global items
    global other_things
    # global shopping_bag_items
    # return shopping_bag_items, items
    print("you see neil on the street biking home from work..\n")
    print("he looks really happy to see you! 'hi panda!! what are you doing out here on your own??' he says")
    # output = items
    # print("you have the following items..")
    # return output
    # print(output)

    item_choice = input("what should you do now?")
    if item_choice == "drop note":
        other_things.remove("note")
        # items_2 = shopping_bag_items[0:6]
        # print("you now have the following items left..")
        # print(items_2)
        print("\tYou drop the note written by ber on the floor in front of neil.")
        print("'wow panda, is this for me?? you clever girl!', neil says.\n\n 'lets take you back inside now..' ")
        final_installment()

    if item_choice == "drop toy":
        items.remove("toy")
        # items_2 = shopping_bag_items[0:6]
        # print("you now have the following items left..")
        # print(items_2)
        print("\tneil sees you playing with the cuddly toy that you found\n\n.")
        print(
            "he attempts to take it from you.\n\n not easy! but he manages to get it from you and throws it for you to chase.. ")
        front_entrance()

    # print("\tyummy! why cant i have these to eat all the time?!")
    # action = input("and now?")
    # if action == items.remove("note"):

    # if action == "drop note":
    #   print("you won the game!")
    # print(output)


def final_installment():
    global items
    global other_things

    print("you go back to the apartment with neil\n")
    print("neil tells sara everything that you have been upto.. uh oh, she doesnt seem too impressed.\n")
    print("'i wonder if i can somehow make her as happy as i made neil'..\n")
    action = input("... ")
    if action == "check items":
        print("you are carrying:")
        for stuff in items, other_things:
            print(stuff)
    # if action in ["check items"]:
    # print(f"you are carrying: {items}")
    else:
        print("pardon?\n")
        # for stuff in items:
        # print(stuff)

        # print(f"you are carrying: {items}")
    item_choice = input("any ideas?\n")

    if item_choice == "drop flowers":
        items.remove("flowers")

        print("\tYou put the flowers on the floor.")
        print("'panda!! are these for me??', sara says.\n\n 'how lovely, they are beautiful!..' ")
        you_won()



    else:
        print("sara looks annoyed at you for going on your little adventure")
        action = input("maybe its better to keep out of her way just for now..")
        if action == "back":
            main_apartment_door()
        else:
            print("i dont know what you mean but you better get out of here.. you still have stuff to do!..\n\n")
            final_installment()


def you_won():
    print("CONGRATULATIONS!! YOU WON!!\n\n")
    print(
        "sara and neil reward you with a shopping trip to futterhaus where you get lots of nice stuff and then afterwards a trip to the lake for a nice picnic! what a lovely adventure!")
    main()


def start_adventure():
    print("You are in the living room, to the side there is a door that leads into the hallway")
    door_picked = input("what do you want to do?")

    if door_picked == "hallway":
        print("You picked the hallway")
        hallway()

    else:
        print("Sorry, i dont know what you mean?")
        start_adventure()


def instructions():
    print("these are the rules of the game..\n")
    print(
        "your name is panda and you have a mission!\n you have to find your way through your apartment building and complete various missions on the way with obstacles in the way such as neighbours and dodgy pets!\n\n")
    print("use commands such as forward, back, left, right, down etc. and commands such as bark, sniff, examine, poop!")
    navigate = input("press 'b' to go back to main menu")
    if navigate == "b":
        main()
    else:
        print("sorry, i dont know what you mean?")
        instructions()


def name():
    return name


def main():
    panda_mood = input("How are you feeling today?? Can you give me one word to describe? ")
    print(f"Panda replies...{panda_mood}")
    print(f"Okaaay so, you are feeling {panda_mood} huh? ")
    print("do you feel like going on a little adventure..?")
    panda_answer = input("yes or no, or i to read game instructions")
    if panda_answer == "yes":
        print("ok! lets do this")
        print("You have just woke up from a beautiful dream and a long sleep..")
        start_adventure()
    if panda_answer == "i":
        instructions()
    else:
        print('ok, one of those days huh, fair enough')

    # print("\nThe end\n")
    # print(f"Thanks for playing, {name}")


if __name__ == '__main__':
    main()