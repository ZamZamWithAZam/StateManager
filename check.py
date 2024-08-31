running = True
living = True

def livingLoop(living):
    if living:
        if input("Do you wish to kill it (y/n) ? \n>").lower() == "y":
            print("You have decided to end it...End...\"It\"")
            return False
        else:
            return True
        

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

        currentLoop = transitions[finishedStates](finishedStates+1)

        currentLoop

        finishedStates += 1

    print("The \"End\" of all, has been reached.\n"
         "Yet question \"It\"...\n"
         "Whether \"It\" shall remain\n")


while running:
    manager(
        livingLoop,
        livingLoop,
        0,
        transition,
        transition
    )

    running = False