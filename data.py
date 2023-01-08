import random
import names


class Scientist(object):
    def __init__(self, s, a, e):
        self.surname = s
        self.awards = a
        self.education = e


class Scientist(object):
    def __init__(self, s, a, e):
        self.surname = s
        self.awards = a
        self.education = e


def generate_data(length):
    computer_science_universities = [
        "MIT",
        "Stanford University",
        "Carnegie Mellon University",
        "UC Berkeley",
        "Princeton University",
        "Harvard University",
        "Caltech",
        "Cornell University",
        "University of Chicago",
        "Columbia University",
    ]

    scientists = []
    for i in range(length):
        surname = names.get_full_name().lower()
        awards = random.randint(0, 30)
        education = random.sample(computer_science_universities, 5)
        scientist = Scientist(surname, awards, education)
        scientists.append(scientist)
    return scientists
