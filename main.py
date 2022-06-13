from sys import exit


inv = []
bowls = []
items = ["food", "treats", "water", "bone"]
shopping_bag_items = ["toy", "sausages", "flowers", "butter", "bread", "sweet potato", "newspaper"]
location = ""
treats = 0
treats_taken = []
treats_in_location = {
    "living room": 3,
    "kitchen": 4,
    "main apartment door": 1,
    "courtyard": 1,
    "sara": 2,
    "ber": 3,
    "neil": 4,
    "hallway": 1,
    "street": 1
}
define = {
    "game": "This game will unlock multiple pleasures if you can crack it.",
    "pills": "These pills are your magic elixier that will give you super powers.",

}



def start():
    global location

    print("""
       panda's adventure
    """)
    location = ""


    panda_mood = input("Hello Panda! How are you feeling today?? Can you give me one word to describe? ")
    print(f"Panda replies...{panda_mood}")
    print(f"Okaaay so, you are feeling {panda_mood} huh? ")
    print("Do you feel like going on a little adventure..?")
    panda_answer = input("yes or no, or help to read game instructions")
    if panda_answer == "yes":
        print("ok! lets do this")
        print("You have just woke up from a beautiful dream and a long sleep..")
        living_room()
    if panda_answer == "help":
        instructions()
    else:
        print('Ok, one of those days huh, fair enough')
        exit()



def instructions():
    print("these are the rules of the game..\n")
    print(
        "your name is Panda the little Shih Tzu lioness and you have a mission.. cause pandamonium!\n you have to find your way through your apartment building and complete various missions on the way with obstacles in the way such as neighbours and dodgy pets!\n\n")
    print("Use commands such as forward, back, left, right, down etc. and commands such as bark, sniff, take, examine, poop!")
    navigate = input("press 'b' to go back to main menu, or 'c' if you are in the middle of the game")
    if navigate == "b":
        start()
    if navigate == "c":
        return
    else:
        print("sorry, i dont know what you mean?")
        return instructions()




def living_room():
    global inv, location, treats
    location = "living room"
    if "pills" not in inv:
        print("You are in the living room in your apartment. A small apartment in Berlin.")
        print(
            "Outside of your window, the sun beats down.\n")
    else:
        print(
            "The light outside is almost blinding and inescapable. You feel as though your heart is full and you struggle to breath.")
        print(
            "You could definitley use your medication.")

    action = input("what do you want to do?")

    if action == "left":
        print("You picked the hallway")
        hallway()
    if action == "take treats":
        treats_adder(location)
    if action == "search":
        search(location)
    if action == "inventory":
        inventory()
    if action == "help":
        instructions()
    if action == "bark":
        bark(location)

        return living_room()


    else:
        print("")
        living_room()





def hallway():
    global inv, location
    location = "hallway"
    print(
        "You are in the hallway of the apartment. In front of you is the main apartment door and to the right is the kitchen you can see Sara pottering about")

    action = input("what do you want to do?")

    if "right" in action:
        kitchen()
    elif "forward" in action:
        print("the main apartment door appears to be closed")
        hallway()
    if action == "take treats":
        treats_adder(location)
    if action == "search":
        search(location)
    if action == "inventory":
        inventory()
    if action == "help":
        instructions()
    if action == "bark":
        bark(location)
    if action == "examine":
        examine()



    else:
        print("")
        hallway()

        return hallway()



#
def kitchen():
    global inv, location, treats, bowls, items, define
    location = "kitchen"
    print(
        "You are now in the kitchen. a sunny bright room with a water and food bowl on the left, and sara straight ahead, sat down at the table by the window.")
    print("whats your next move?")
    action = input("... ")
    if action == "hallway":
        hallway()

    if action == "forward":
        sara()
    if action == "take treats":
        treats_adder(location)
    if action == "search":
        search(location)
    if action == "inventory":
        inventory()
    if action == "bark":
        bark(location)
    if action == "help":
        instructions()
    if action == "examine":
        examine(location)

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
        for stuff in items, inv:
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
                treats_adder(location)
                items.remove("treats")
                bowls_2 = items[0:4]
                print("you see following items..")
                print(bowls_2)
                treats_adder(location)

            elif bowl_choice == "take water":
                items.remove("water")
                bowls.append("water")
                bowls_2 = bowls[0:4]
                print("you now have the following items left..")
                print(bowls_2)
                print("\tYou drink the water thats been left for you.")
                print("\tWoohoo! I just peed on the floor.")
                game_over("Sara goes mad and locks you in the living room")

            elif bowl_choice == "take food":
                items.remove("food")
                bowls.append("food")
                bowls_2 = bowls[0:4]
                print("You now have the following items left..")
                print(bowls_2)
                print("\tYou tuck into your lunch. your tummy is heavy after all that food..")
                print("\tWoohoo! time for a sleep.")
                game_over("No more adventure for you sleepyhead")

            elif bowl_choice == "take bone":
                items.remove("bone")
                inv.append("bone")
                bowls_2 = items[0:4]
                print("you now see the following items in the kitchen:\n")
                print(bowls_2)
                print("\tYou take the bone. I'll save this for later! could come in handy, you think to yourself")



            elif bowl_choice == "leave it":
                print("not feeling hungry right now, unless theres carbs involved, of course!, let's get out of here")
            else:
                print("Well, not sure what you mean there")

                kitchen()
        return bowls



def main_apartment_door():
    global inv, location, treats, items
    location = "street"
    print("You see some stairs leading down to the outside, and 3 other apartment doors.\n\n")
    print(
        "Well the neighbours arent at home, and I don't care for them much anyway, they never give me treats! \n\nHmmm should i see whats going on downstairs..\n\n")
    print("Do you go downstairs or back into the hallway?")

    next_move = input("... ")

    if "down" in next_move:
        downstairs()

    elif "back" in next_move:
        hallway()
    elif "take treats" in next_move:
        treats_adder(location)
    else:
        print("not sure what you mean there...")
        return main_apartment_door()


def downstairs():
    global inv, location, treats
    location = "downstairs"
    print("you see peter the cat sat on the stairs")

    action = input("you walk up to peter, he stares at you ")
    if action == "up":
        main_apartment_door()
    if action == "take treats":
        treats_adder(location)
    if action == "search":
        search(location)
    if action == "inventory":
        inventory()
    if action == "bark":
        bark(location)
    if action == "examine":
        peter()

    if action == "scratch door":
        inv.remove("flowers")
        print(
            "You scratch on Carolin's door for help..\nCarolin open's the door, she looks puzzled.. she lets out an extremely loud wail.. MYYYYYYYYYYYYLOOO!! milo the cat comes out into the hallway..\n")
        print("Mylo attacks Peter. Well that worked well! You continue upstairs and back into the apartment\n")
        final_installment()
    else:
        print('peter attacks you\n\n')
    print('game over')
    exit()
    downstairs()



def peter():
    global inv, location, treats
    location = "peter"
    print("peter is looking at the things you are carrying")


    next_move = input("... ")

    if "drop bone" in next_move:
        inv.remove("bone")
        print("peter looks at the bone in terror, shits himself and runs away\n\n")
        print("you head down the staircase into the courtyard")
        courtyard()
  #  if "bone" not in inv:
   #     del inv
   #     print("you don't have that..\n")
   # return downstairs()

def courtyard():
    global inv, location, treats
    location = "courtyard"

    print("you are now in the courtyard\n in front of you there is an open door leading to the front entrance")
    print("whats your next move?")
    action = input("... ")

    if action == "search":
        search(location)
    if action == "inventory":
        inventory()
    if action == "bark":
        bark(location)
    if action == "examine":
        examine(define[obj])
    if action == "take bone":
        inv.append("bone")

    if action == "back":
        downstairs()
    if action == "forward":
        print("the front entrance door to the apartment building seems to be closed")
        courtyard()
    if action == "poop":
        print("you take a dump and ber looks at you in disgust")
        exit()

    if action in ["go to ber", "walk to ber", "ber", "see ber"]:
        ber()


    else:
        print('ber smiles and says hello but looks busy\n\n')
        courtyard()



def front_entrance():
    global inv, location, treats, define, treats_taken
    location = "street"

    print("You are just outside the front entrance looking out onto the street.\nyou see various familiar faces\n")

    action = input("... ")
    if action == "take treats":
        treats_adder(location)
    if action == "search":
        search(location)
    if action == "inventory":
        inventory()
    if action == "bark":
        bark(location)
    if action == "help":
        instructions()
    if action == "examine":
        examine(location)

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
                inv.append("toy")
                print(items_2)



            if item_choice == "take butter":
                shopping_bag_items.remove("butter")
                items_2 = shopping_bag_items[0:6]
                print("there are now the following items left..")
                print(items_2)
                print("\tYou take a big bite out of the cube of butter, 'eww no thanks' ")

            if item_choice == "take flowers":
                shopping_bag_items.remove("flowers")
                items_2 = shopping_bag_items[0:6]
                inv.append("flowers")
                print("you now have the following items left..")
                print(items_2)
                print("\tYou smell the flowers, very nice! .")
                print("you are now carrying the following items:")


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
                inv.append("sweet potato")
                print("you now have the following items left..")
                print(items_2)
                print("\tthese will do for my weekly groceries!.")

            else:
                break
    print("In front you see some people outside the shop, and somebody who looks familiar riding a bike\n")
    print("Behind you there is the front entrance leading into the courtyard\n")
    action = input("... ")
    if action == "back":
        courtyard()
    if action == "forward":
        neil()
    if action == "inventory":
        inventory()
        return front_entrance()
def neil():
    global inv, location, treats,  items
    location = "neil"
    print("You see neil on the street biking home from work..\n")
    print("He looks really happy to see you! 'hi panda!! What are you doing out here on your own??' he says")

    item_choice = input("what should you do now?")
    if item_choice == "drop note":
        inv.remove("note")

        print("\tYou drop the note written by ber on the floor in front of neil.")
        print("'Wow Panda, is this for me?? you clever girl!', neil says.\n\n 'Lets take you back inside now..' ")
        final_installment()

    if item_choice == "drop toy":
        inv.remove("toy")
        print("\tneil sees you playing with the toy that you found\n\n.")
        print(
            "He attempts to take it from you.\n\n not easy! but he manages to get it from you and throws it for you to chase.. \nas you come to the toy, you spot a dog activity game someone has left out ")
        found_secret_game()



def final_installment():
    global inv, location, treats

    print("you go back to the apartment with neil\n")
    print("neil tells sara everything that you have been upto.. uh oh, she doesnt seem too impressed.\n")
    print("'i wonder if i can somehow make her as happy as i made neil'..\n")


    action = input("any ideas?\n")

    if action == "drop flowers":
        inv.remove("flowers")


        print("\tYou show Sara the flowers.")
        print("'Panda, thanks for the flowers!!', sara says.\n\n 'do you have anything else..?' ")
        dog_treat_game()




    if action == "inventory":
        inventory()
        return final_installment()



    else:
        print("sara looks annoyed at you for going on your little adventure")
        action = input("maybe its better to keep out of her way just for now..")
        if action == "back":
            main_apartment_door()
        else:
            print("i dont know what you mean but you better get out of here.. you still have stuff to do!..\n\n")
            return final_installment()

def dog_treat_game():
    action = input("hmm do i have something for all these treats, you think")

    if action == "examine":
        examine()

    if action == "play game":
        inv.remove("game")
        print("Go for it Panda!")
        import random

        num = random.randint(0, 10)
        print('Number:', num)
        attempt = 4
        msg = 'hard luck panda!'

        while attempt > 0:
            user_input = int(input('which box number do the treats lie in.. take a sniff!'))

            if user_input == num:
                msg = 'CONGRATULATIONS!! YOU COMPLETED YOUR ADVENTURE! I guess now its time for a sleep right? Well done Panda. Until next time.'
                break
            else:
                print(f'Try again! {attempt} attempt left.')
                attempt -= 1
                continue

        print(msg)
        exit()
    else:
        print("you don't have that!")
        final_installment()

def sara():
    global location, inv, treats
    location = "sara"
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
        "beg": "You get on your hind legs and do your best balancing act while dancing in a circle.. very impressive! ",
        "ask to go out": "You stomp your feet and start sobbing. "}

    while True:
        action = input("whats your move? e.g. examine,take pizza, bark, ask to go out")
        if action in actions_dict.keys():
            print(actions_dict[action])
            if action == "take pizza":
                inv.append("pizza crust")
                print("sara didnt notice a thing! i'm such a smartass.")
                print(
                    "to the right of you is the hallway and straight ahead in the kitchen there is sara. \n\n you can see food and water bowls, and treats.\n")
                kitchen()
            elif action == "ask to go out":
                print(
                    "sara shouts neil to ask him to take you outside, then she realises he is not home. \n\n she looks annoyed and sighs and gets up and walks to the main apartment door and opens it")
                main_apartment_door()
            elif action == "beg":
                print("sara gives you treats!")
                treats_adder(location)

            elif action == "bark":
                game_over(
                    "Unfortunately it didnt impress sara at all. \n\n she picks you up and puts you back in the living room and closes the door on you. \n<GAME OVER>")

            else:
                print("hmm ok")




def ber():
    global location, inv, treats
    location = "ber"
    print(
        "you walk up to ber, he smiles and gently strokes your head. 'hello panda, what can i do for you?' , he says.. ")
    actions_dict = {
        "examine": 'ber seems to be busy with something\n\n You look around the courtyard smelling the grass, hmm do you need to poop panda?',
        "drop pizza crust": "ber laughs and says 'do you want a treat instead of that crusty pizza leftover?' \nhe gives you a treat",
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
            elif action == "drop pizza crust":
                 inv.remove("pizza crust")
                 treats_adder(location)


            elif action == "bark":
                inv.append("note")
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
                break


    action = input("what do you want to do now panda?")
    if action == "forward":
        front_entrance()

    if action == "back":
        downstairs()

    if action == "search":
        search(location)
    if action == "inventory":
        inventory()
    if action == "talk":
        bark(location)
    if action == "examine":
        examine(location)
    else:

        print("hmm ok")
        courtyard()

def search(location):

    search_answers = {
        "living room": "Your living room is spacious, on the side next to the couch you can see what looks like a bag of treats thats nearly finished but quite a few left!. You . Your toy box is in the floor by neil's records.",
        "hallway": "Sara looks at you briefly before returning her gaze skyward. You look up at her as she steps into the kitchen and you are dazzled by the sunlight blazing through the window. You search in neil's bag laid on the floor and see a treat inside..",
        "kitchen": "The kitchen is silent, except for sara making soft humming and coughing sounds. You run your nose along the floor, nothing much about. Without noticing while pulling something from a kitchen shelf, Sara drops a packet of treats on the floor.",
        "downstairs": "A treat lies near the bottom of the stairs. Peter looks on at you, awaiting your next move",
        "street": "The street seems like a hive of activity, theres kids playing, people seems to be enjoying the weather. \nOn the ground near the bus stop, you see a treat that someone apparently dropped. \nFurther down the street there is what looks like a zu vershenken box in a doorway.",
        "courtyard": "You are in the courtyard, you see tables and chairs in the recreational area, also bikes and plants. You also see Ber, Peter's owner sat down in the recreational area of the courtyard."
    }
    print(search_answers[location])

def take(s):
    global inv, define, location
    if len(s) <=10:
        print("You take the treats.")
    else:
        obj = s.split(None, 1)
        obj = obj[1].capitalize()
        if obj in inv:
            print("You already took that.")
        elif obj == "treats":
            treats_adder()

        else:
            print(f"You can't take the {obj}.")




def inventory():

    print("\nYou are carrying...")
    for i in inv:
        print(i)
    print(f"{treats} treats\n")


def bark(location):

    global inv, treats
    if location == "hallway":

        print("You approach sara, who smiles at you. She opens her mouth to speak, and the voice that you hear is high pitched and excited.")

        print("'Hello panda, how are you enjoying your morning? Have we given you your heart medicine yet?? The question takes you aback. You respond with a grunt. You could really do with a wee.")

        print("'Beautiful weather today isnt it?? As she speaks, the glow grows brighter. Its as if the sun was on the other side of the planet, shining so brightly its light penetrated the very ground. Shadows fade and from somewhere you feel a deep, ominous hum. Your vision turns black and suddenly you find yourself standing on a dark, gravely shore. You watch as a single, giant hand breaches the surface of the water. The flesh of the beast is grotesque, scaly, as it reaches out to you...")

        print("Just as suddenly you are again standing in front of Sara, her smile suggesting she knows where you were and what you saw.")

        print("You walk away in a slight daze. Not until a little later do you realize youve been walking in a circle. You find yourself once again in the hallway as Sara saunters into the kitchen")
        hallway()
    elif location == "street":
        print("You wag your tail at Jonas to get his attention. He looks down after a drag of his cigarette. \n'Oh! Sorry, I didn't see you there Panda!'")

    elif location == "kitchen":
        print("""
        Sara looks up. "Hii baby!! How are you doing?" She coughs and hums as you do a little grunt, she can't seem to help it. She reads something on her phone which sends her into a coughing fit.

        "Oooh I nearly forgot," she continues coughing as she bends down. "Here it is!" She has your medication.
        """)
        if "Pills" in inv:
            print("You feel weird about taking the pills.")
        else:

            inv.append("pills")


    else:
        print("nobody to bark at")

def examine():
    global inv, treats

    a = define
    if a in inv:
        print(define[:])
    elif a == "Treats":
        print(f"{treats} in small pieces. Good idea to collect these to come in use at some point.")
    else:
        print("Examine what?")
        return


def found_secret_game():
    global inv, treats, treats_taken
    print("You see if you have enough treats to go in the game.")



    a = [treats]
    if a <= [1]:
     print("you don't have enough treats.")





    if a >= [1]:
      print("Hey Panda you collected enough treats! tha game is yours!.")
      inv.append("game")
      neil()
    else:
        print("You take a sniff and do a little grunt. Its of no interest to you.")



def treats_adder(location):
    global treats_taken, treats
    if location in treats_taken:
        print("There is no more treats to take.")
    else:
        print(f"You take the {treats_in_location[location]} you found.")
        treats += treats_in_location[location]
        treats_in_location[location] = 0
        treats_taken.append(location)



start()