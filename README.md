# StateManager
This is a simple State Manager for Python, to manage around functions and transitions between said functions.
This was just a simple project to see whether functions could be called by other functions, and the way
you can manage them. I did this by storing the "Name" of the functions in an array, with the functions
before the "Integer" being the states, and the functions after the integer being the transitions.

Currently, the transition is **always set** to call the first instance of the function after the integer, 
so you can never call upon any transitions outside of what's inside that, but this can be easily changed 
by having the transitions being called to be equal to the "finishedStates", i.e. the 'n'th index,
which will correspond the 'n'th amount of times that a set of States has finished.
