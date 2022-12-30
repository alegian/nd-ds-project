class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class RTree:
    def __init__(self, data, top_left=Point('', 0), bot_right=Point('', 0)):
        self.data = data
        self.first = None
        self.second = None
        self.third = None
        self.top_left = top_left
        self.bot_right = bot_right

    def insert(self, data):
        if not data:
            return

        if self.first is None:
            self.first = RTree(data, Point(data.surname, data.awards), Point(data.surname, data.awards))
            return
        elif self.second is None:
            self.second = RTree(data, Point(data.surname, data.awards), Point(data.surname, data.awards))
            return
        elif self.third is None:
            self.third = RTree(data, Point(data.surname, data.awards), Point(data.surname, data.awards))
            return
        else:
            # insert sto paidi me elaxisto embadon


    def range_query(self, surname_min, surname_max, award_min, award_max):
        out = []
