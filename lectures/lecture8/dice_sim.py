# dice_sim.py

#
# How many times would you expect to roll 5 6-sided dice until they are all
# the same value?
#

import random

def roll_die():
  """ Randomly returns 1, 2, 3, 4, 5, or 6.
  """
  return random.randrange(1, 7)

def run_experiment_once():
    """ Rolls 5 6-sided dice until all show the same value.
    Returns the number of rolls.
    """
    num_rolls = 0
    done = False
    while not done:
        num_rolls += 1  # += means "add to"
        d1 = roll_die()
        d2 = roll_die()
        d3 = roll_die()
        d4 = roll_die()
        d5 = roll_die()
        if d1 == d2 and d2 == d3 and d3 == d4 and d4 == d5:
            #print(f'Success! All dice rolled a {d1}!')
            #print(f'It took {rolls} rolls.')
            return num_rolls

def run_experiment(times):
    total_rolls = 0.0
    for i in range(times):
        rolls = run_experiment_once()
        total_rolls += rolls

    average = total_rolls / times
    print(f'Average # rolls over {times} experiments: {average}')
