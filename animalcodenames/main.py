import os
import random

adjectives = None
animals = None
colors = None

def gen_name():
  """Return a string describing a colorful animal.
  Example: \'Happy-Purple-Baboon-34\'
  """
  install_location = os.path.abspath(os.path.dirname(__file__))

  global adjectives, animals, colors
  if adjectives is None:
    adjectives = open(os.path.join(install_location, "adjectives.txt"), "r").read().split("\n")
    animals = open(os.path.join(install_location, "animals.txt"), "r").read().split("\n")
    colors = open(os.path.join(install_location, "colors.txt"), "r").read().split("\n")
    assert "" not in adjectives
    assert "" not in animals
    assert "" not in colors
    print("read files")

  name = '-'.join([random.choice(adjectives),
                  random.choice(colors),
                  random.choice(animals),
                  str(random.randint(1, 99))])
  return name