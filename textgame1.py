#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     textgame1.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue # 168
# Written by G.D. Walters
# Copyright (c) 2021 by G.D. Walters
# This source code is released under the MIT License
# ======================================================

import random

global directions, items, monsters, possessions, this_location, game_running
global north_count, south_count, east_count, west_count
north_count = south_count = east_count = west_count = 0
directions = ['North', 'South', 'East', 'West']
# items = ['Axe', 'Sword', 'gold', 'silver', 'diamonds',
#         'flint and steel', 'shovel', 'flower', 'apple']
monsters = ['Ogre', 'Dragon', 'Imp', 'Sea Serpent']
possessions = ['bag of holding']
global game_objects
game_objects = ['Axe', 'Hammer', 'Sword', 'flint',
                'steel', 'gold', 'silver', 'branch', 'shovel', 'flower', 'apple', '']


game_running = True
this_location = 'Start'


def quit_game():
    global game_running
    game_running = False


def describe(location):
    # pass
    print('Sorry, but the describe feature is not available yet.')


def display_help():
    # pass
    # print('Sorry, but the help feature is not available yet.')
    commands = ['hit', 'use', 'drop', 'get', 'inventory',
                'go {direction}', 'look', 'help', 'quit']
    exps = ['Use this to strike a foe', 'Takes an object out of your bag of holding (if you have it)', 'Removes an object from your bag of holding (or hand) and leaves it behind.', 'Adds an object to your bag of holding',
            'Displays a list of all the objects in your bag of holding.', 'Use this command to move in a direction.', 'Describes the area around you.', 'Displays this message.', 'Ends the game.']
    print('Help:')
    print('~'*20)
    # print(len(commands))
    # print(len(exps))
    cntr = 0
    for cmd in commands:
        print(f'    {cmd} - {exps[cntr]}')
        cntr += 1
    print('~'*20)


def work_command(command):
    global directions, monsters, possessions, this_location, game_running, game_objects
    global north_count, south_count, east_count, west_count
    print(command)
    print(command.split())
    match command.split():
        case["quit"]:
            print("Goodbye!")
            quit_game()
        case["help"]:
            display_help()
        case["look"]:
            describe(this_location)
        # case["inventory"]:
        #     response = f'You currently have {possessions}'
        #     print(response)
        case 'go', 'North' | 'South' | 'East' | 'West' as direction:
            print(f'Direction: {direction}')
            match direction:
                case 'North':
                    print('Moving North')
                    north_count += 1
                case 'South':
                    print('Moving South')
                    north_count -= 1
                case 'East':
                    print('Moving East')
                    east_count += 1
                case 'West':
                    print('Moving West')
                    east_count -= 1
        case 'go', *wth:
            print(f'{wth} is not supported')
        case["inventory"]:
            print('~'*25)
            message = f'You currently have {len(possessions)-1} object(s) in your bag:'
            print(message)
            # print('~'*25)
            for pos in possessions:
                print(f'   {pos}')
            print("~"*25)
        case["get", obj] | ["pick", "up", obj] | ["pick", obj, "up"] | ["take", obj]:
            if obj in game_objects:
                print(f"Pick up {obj}")
                possessions.append(obj)
            else:
                print(f'I do not see the {obj}')
        case["drop", obj]:
            if obj in possessions:
                print(f'Ok.  {obj} dropped')
                possessions.remove(obj)
            else:
                print(f'You do not have {obj}')
        case["use", obj]:
            if obj in possessions:
                print(f'You are now holding the {obj}')
            else:
                print(f"You don't have the {obj}")

        # case["North"] | ["go", "North"]:
        #     north_count += 1
        #     south_count -= 1
        #     message = "Ok.  Going North"
        #     print(message)
        # case["South"] | ["go", "South"]:
        #     south_count += 1
        #     north_count -= 1
        #     message = "Ok.  Going South"
        #     print(message)
        # case["East"] | ["go", "East"]:
        #     east_count += 1
        #     west_count -= 1
        #     message = "Ok.  Going East"
        #     print(message)
        # case["West"] | ["go", "West"]:
        #     west_count += 1
        #     east_count -= 1
        #     message = "Ok.  Going West"
        #     print(message)
        case _:
            print("I'm sorry, I don't recognize that command.")


message = """
Welcome to my silly text adventure game!  I know you haven't been here before
so, I'll let you know what's happening.  Last night, you were with your friends
at the local tavern and you had WAY too much to drink!  You have just awakened
and have a horrible headache and your tongue feels like it's coated with nettles. 
"""
print(message)
message = """
As you can tell, you are in a forest and you have no idea how to get out.  Basically,
you have to wander around until you get back to the town.  However, I won't tell you 
which direction that is.  You can only go North, South, East and West.  To move, you 
can say 'Go North' or 'Go South' and so on.  You can say 'Look' to see what is around 
you.  You can say 'Get {item}' to get an item (that is there).  You can also 'Drop {item}' 
to get rid of it.  You can say 'Inventory' to find out what items there are.  You can 
say 'Quit' to end the game and you can say 'Help' to get a list of all the things you
can do. 

Good luck!
"""
print(message)

game_running = True
while game_running:
    response = input('What would you like to do? -> ')
    work_command(response)
    print(f'GameRunning: {game_running}')
