from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n ", '-' * 10
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name) 

class Death(Scene):
    quips = [
        "You died. You kind suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print "The Gothons of Plaent Percal #25 have invaded your ship and destoyed"
        print "you entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the brdige, and blow the ship up after getting into an"
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body. He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim. Your laster hits his costume but misses him entirely. This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into insane rage and blast you repeatedly in the face until"
            print "you are dead. Then he eats you."

        elif action == "dodge!":
            print """
                    Like a world class boxer you dodge, weave, slip and slide right
                    as the Gothon's blaster cranks a laser past your head.
                    In the middle of your artful dodge your foot slips and you
                    bang your head on the metal wall and pass out.
                    You wake up shortly after only to die as the Gothon stomps on
                    your head and eats you.
                """
                return 'death'
        
        elif action == "tell a joke":
            print """
                    Lucky for you they made you learn Gothon insults in the academy.
                    You tell the one Gothon joke you know:
                    The quick brown fox jumps over the lazy dog
                    The Gothon stops, tries not to laugh, then busts out laughing and can't move.
                    While he's laughing you run up and shoot him square in the head
                    putting him down, then jump through the Weapon Armory door.
                """
                return 'laser_weapon_armory'
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print """
                You do a dive roll into the Weapon Armory, crouch and scan the room
                for more Gothons that might be hiding. It's dead quite, too quite.
                You stand up and run to the far side of the room and find the
                neutron bomb in its container. There's a keypad lock on the box
                and you need the code to get the bomb out. If you get the code
                wrong 10 times then the lock closes forever and you can't
                get the bomb. The code is 3 digits.
            """
            code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
            guess = raw_input("[keypad]> ")
            guesses = 0
class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

