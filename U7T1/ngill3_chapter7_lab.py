room_list = [
    {  # 0
        'name': 'Front Yard',
        'description_1': 'The grass is dead. The front door to the North looks weak, maybe you can kick it open?',
        'description_2': 'The grass is still dead and the front door still looks weak.',
        'visited': False,
        'connections': {'n': 1, 'e': None, 's': None, 'w': None}
    },
    {  # 1
        'name': 'Entrance',
        'description_1': 'You kicked in the door and it flies off it\'s hinges.\nAs you walk in the frame collapses, blocking you from leaving.\n'
                         'The entrance of this house leads to two rooms; Some stairs up to the second floor straight ahead (North) and a doorway to the kitchen (East).',
        'description_2': 'The entrance of this house leads to two rooms; Some stairs up to the second floor straight ahead (North) and a doorway to the kitchen (East).\n'
                         'Be careful, there\'s still wood splinters on the floor!',
        'visited': False,
        'connections': {'n': 2, 'e': 3, 's': None, 'w': None}
    },
    {  # 2
        'name': 'Upstairs Bedroom',
        'description_1': 'There isn\'t anything here other than a bed. Looks like it hasn\'t been used in a very long time. The stairs back are behind you to the South.',
        'description_2': 'The room hasn\'t changed since the last time you checked. The stairs back are to the South.',
        'visited': False,
        'connections': {'n': None, 'e': None, 's': 1, 'w': None}
    },
    {  # 3
        'name': 'Kitchen',
        'description_1': 'A fancy modern kitchen. Something to the South catches your eye.',
        'description_2': 'You try and look around but something to the South is calling you...',
        'visited': False,
        'connections': {'n': None, 'e': None, 's': 4, 'w': 1}
    },
    {   # 4
        'name': 'Cupboard',
        'description_1': 'You walk up to a closet and open it. It\'s very spacious, you wonder if you can fit inside. You can.\n'
                         'Just as you were about to leave you accidentally knock something off the shelf.\nScrambling to grab it before it hits '
                         'the floor, you kick the door closed and you hear a *click*.\nYou are now locked in the closet with no escape.\nThe end.',
        'description_2': 'You are already dead. This text shouldn\'t appear.',
        'visited': False,
        'connections': {'n': None, 'e': None, 's': 4, 'w': 1}
    }
]
current_room = 0
last_room = -1
running = True

print("Commands:\n"
      "\t[L]ook\t: look around\n"
      "\t[N]orth\t: Travel north\n"
      "\t[E]ast\t: Travel east\n"
      "\t[S]outh\t: Travel south\n"
      "\t[W]est\t: Travel west\n"
      "Commands are case-insensitive and you only need to use the first letter")
input("Press enter to begin.")
print("\n" * 5)

while running:
    room = room_list[current_room]
    if last_room == current_room:
        print(f"You are still in the {room['name']}.")
    elif room['visited']:
        print(f"You are in the {room['name']}")
    else:
        print(f"You are in the {room['name']}.\n{room['description_1']}")
        room_list[current_room]['visited'] = True

    if current_room == 4:
        break

    last_room = current_room
    inp = input("> ")[0].lower()

    if inp == 'l':
        print(room['description_2'])
    elif inp in ['n', 'e', 's', 'w']:
        new_room = room['connections'][inp]
        if new_room is None:
            print("You can't travel in that direction")
        else:
            print("You make your way into another room.")
            current_room = new_room
