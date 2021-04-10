
global game_objects, possessions
game_objects = ['Axe', 'Hammer', 'Sword', 'flint',
                'steel', 'gold', 'silver', 'branch', '']
possessions = ['bag of stuff']


def work_command(command):
    global north_count, south_count, east_count, west_count
    # print(command.split())
    match command.split():

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
        case["get", obj] | ["pick", "up", obj] | ["pick", obj, "up"]:
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


global north_count, south_count, east_count, west_count
north_count = south_count = east_count = west_count = 0

work_command('go North')
work_command('go South')
work_command('go East')
work_command('go West')
work_command('go Up')
work_command('pick Axe up')
work_command('inventory')
work_command('get gun')
work_command('drop Axe')
