import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0.3)


def intro():
    print_pause("""You find yourself standing in an open field,
    filled with grass and yellow wildflowers.""")
    print_pause("""Rumor has it that a wicked fairie is somewhere around here,
    and has been terrifying the nearby village.""")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")


def cave(items):
    print_pause("You find an item.")
    items_list = ["lighter", "candle", "a box of match", "cigarette"]
    c = random.choice(items_list)
    if c == "cigarette":
        print_pause("yay :D")
    print_pause(c)
    items.append(c)
    choose_number(items)


def house(items):
    print_pause("You meet a old man.")
    print_pause("Talk to him")
    if items.count("cigarette") < 5:
        print_pause("He is saying, not enough cigarettes!!!")
    else:
        print_pause("He is saying, you won!")
    choose_number(items)


def choose_number(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("Enter 0 to quit.")
    print_pause("What would you like to do?")
    response = input("Please enter 1 or 2.\n")
    while response > "0" and response <= "2":
        print_pause("Please enter 1 or 2")
        response = input("Please enter 1 or 2.\n")
        if response == "1":
            house(items)
            break
        elif response == "2":
            cave(items)
            break
        elif response == "0":
            print_pause("bye")
            quit()


def play_game():
    items = []
    intro()
    choose_number(items)


play_game()
