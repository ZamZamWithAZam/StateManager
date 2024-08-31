running = True
living = True

def livingLoop(living):
    while living:
        
        playerInput = input("Do you wish to kill it (y/n) ?\n>").lower()

        if playerInput == "y":
            print("\nYou have decided to end it...End...\"It\"")
            return False
        elif playerInput == "n":
            print("\nNone were harmed, \"It\" continues on...\n")
        else:
            print("\nDid you give any input?\nFor all I got waas that which cannot be deciphered...\n")

        

def transition(num : int):
    match num:
        case 1:
            print('He dies, one killed, and yet nothing gained... \n')
        case 2:
            print('Will death persist towards them? I am not one to know... \n')


def manager(*args):
    states = []
    transitions = []
    breakNum = None

    for i, arg in enumerate(args):
        if isinstance(arg, int):
            breakNum = arg
            states = args[:i]
            transitions = args[i+1:]
            break
    
    stateCount = len(states)
    finishedStates = 0

    print("Finished calculating...\n")

    while finishedStates < stateCount:
        currentLoop = states[finishedStates](living)

        currentLoop

        currentLoop = transitions[0](finishedStates+1)

        currentLoop

        finishedStates += 1

    print("The \"End\" of all, has been reached.\n"
         "Yet question \"It\"...\n"
         "Whether \"It\" shall remain...\n"
         "Oh shall it remain...\n")


while running:
    manager(
        livingLoop,
        livingLoop,
        0,
        transition
    )

    running = False