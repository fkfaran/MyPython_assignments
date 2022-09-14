import random
words = [
    "dance",	"high",	"our",	"spouse",
    "able",	"danger",	"hill",	"out",	"spring",
    "about",	"dark",	"him",	"outside",	"square",
    "above",	"daughter",	"himself",	"over",	"stairs",
    "accident",	"day",	"hint",	"own",	"stairway",
    "acid",	"decide",	"oxygen", "stand",
    "Africa",	"dentist",	"hope", "paper", "stay",
    "after", "deposit", "horse",	"paragraph",	"step",
    "again"	"describe",	"hospital",	"parents",	"stick",
    "against",	"desert",	"hot",	"park",	"still",
    "amount",	"directions",	"inches",	"person",	"such",
    "anything",	"doll",	"internet",	"plan",	"sure",
    "appear",	"done",	"into",	"planet",	"surprise",
    "ask",	"driver",	"join",	"police",	"tall",
    "drop",	"jumped",	"poor",	"taste",
    "ATM",	"drugs",	"just",	"pose",	"tax",
    "aunt",	"dry",	"keep",	"possible",	"teach",
    "base",	"easy",	"lake",	"probably",	"than",
    "beautiful",	"eggs",	"large",	"promise",	"them",
    "beauty	eight	last	proof	themselves",
    "below",	"engine",	"legs",	"radio",	"thought",
    "beside",	"England",	"length",	"railroad",	"thousand",
    "black",	"ever",	"link",	"reason",	"toll",
    "book",	"exactly",	"live",	"record",	"total"
    "but",	"female",	"math",	"rock",	"upset",
    "captain",	"firefighter",	"metal",	"scale",	"walk",
    "car",	"first", "method",	"scared",	"wall",
    "care",	"fish",	"middle",	"schedule",	"want",
    "careful",	"five",	"might",	"school",	"war",
    "carry",	"flammable",	"mile",	"science",	"warm",
    "case",	"floor",	"milk",	"scientist",	"warning",
    "cash",	"flowers",	"million",
    "cashier",	"fly",	"mind",	"search",	"wash",
    "change	fragile	mountain	seven	well",
    "choose	game	multiply	should	where",
    "college" < "grass", "north", "sky", "wish",
    "computer",	"had",	"notice",	"wonder",
    "confidential",	"hair",	"now",	"sofa",	"wood",
    "controls",	"happy",	"ocean",	"solve",	"world",
    "cool",	"hard"
    "correct",	"office",	"something",	"would"
    "cost",	"hat",	"often", "sometimes",	"write",
    "country",	"hear",	"once",	"sound",	"year"
    "couple",	"heart",	"one",	"south",	"yell",
    "coupon"	"heat",	"online",	"southbound",	"yes",
    "course"	"heavy",	"only",	"space",	"yet"
    "covered",	"height",	"open",	"speak",	"you"
    "cup",	"her",	"order",	"spell",	"your",
    "cut",	"here",	"other",	"spoon"	, "yourself"]


class PuzzleGame:
    def __init__(self, words):
        self.words = words
        random.shuffle(self.words)
        self.points = 0

    def add_points(self):
        self.points += 1
        return self.points

    def shuffle(self, a):
        random.shuffle(a)
        b = "".join(a)
        return b

    def get_points(self):
        return self.points


obj = PuzzleGame(words)
n = 0
while n < 5:
    print('-'*40)
    a = list(obj.words[n])
    b = obj.shuffle(a)
    ui = input(f"Arrange the letters to form a valid word\n{b}\n")
    if ui == obj.words[n]:
        obj.add_points()
        print("correct")
    else:
        print(f"wrong\nCorrect word is '{obj.words[n]}'")
    n += 1
print(f"your final points are: {obj.get_points()}")
