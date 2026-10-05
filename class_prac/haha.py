# From my stupid AU

import random

class BandMate:
    def __init__(self, name, age, instrument, f_genre, bandName):
        self.name = name
        self.age = age
        self.instrument = instrument
        self.f_genre = f_genre
        self.bandName = bandName
        

    def intro(self):
        print(f"{self.name} is {self.age}, plays {self.instrument}, and their favorite genre is {self.f_genre}.")
        print(f"They're in {self.bandName}.")

cass = BandMate("Cassandra Wayne", 20, "Lead Guitar", "MeloDeath", "Lazarus Pitt")
cass.intro()

print()

rose = BandMate("Rose Wilson", 21, "Bass", "Death Metal", "Lazarus Pitt")
rose.intro()

print()

steph = BandMate("Stephanie Brown", 20, "Vocalist/Frontman", "Shoegaze/Noise Pop", "Lazarus Pitt")
steph.intro()

print()

duke = BandMate("Duke Thomas", 19, "Drummer", "Punk/Blackened Thrash Metal", "Lazarus Pitt")
duke.intro()

print()

jason = BandMate("Jason Todd", 23, "Rhythm Guitar", "Phychobilly/Doom Metal", "Lazarus Pitt")
jason.intro

print()

tim = BandMate("Tim Drake", 19, "Manager", "Who gaf. Get back to work bud", "Lazarus Pitt")
tim.intro()

dice = random.choice = (BandMate)
print(dice)