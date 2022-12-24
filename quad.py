from alphabetical_average import str_average


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node(object):
    def __init__(self, pos, data):
        self.pos = pos
        self.data = data


class Quad(object):
    def __init__(self, top_left=Point(' ', 0), bot_right=Point(' ', 0), n=None, top_left_tree=None, top_right_tree=None,
                 bot_left_tree=None, bot_right_tree=None):
        self.top_left = top_left
        self.bot_right = bot_right
        self.n = n
        self.top_left_tree = top_left_tree
        self.top_right_tree = top_right_tree
        self.bot_left_tree = bot_left_tree
        self.bot_right_tree = bot_right_tree

        def range_query(node, surname_min, surname_max, award_min, award_max):
            out = []

            if not node.intersect(range): # edw thelei douleia
                return out

            if node.isLeaf():
                out.append(node.getNodes())
                return out

            out.append(range_query(node.top_left_tree, surname_min, surname_max, award_min, award_max))
            out.append(range_query(node.top_right_tree, surname_min, surname_max, award_min, award_max))
            out.append(range_query(node.bot_right_tree, surname_min, surname_max, award_min, award_max))
            out.append(range_query(node.bot_left_tree, surname_min, surname_max, award_min, award_max))

            return out

    def insert(self, node):
        if node is None:
            return

        # if not self.in_boundary(node.pos):
        #     return

        # if abs(self.top_left.x - self.bot_right.x) <= 1 and abs(self.top_left.y - self.bot_right.y) <= 1:
        #     if self.n is None:
        #         self.n = node
        #     return

        if str_average(self.top_left.x, self.bot_right.x) >= node.pos.x:
            if (self.top_left.y + self.bot_right.y) / 2 >= node.pos.y:
                if self.top_left_tree is None:
                    self.top_left_tree = Quad(
                        Point(self.top_left.x, self.top_left.y),
                        Point(str_average(self.top_left.x, self.bot_right.x),
                              (self.top_left.y + self.bot_right.y) / 2))
                self.top_left_tree.insert(node)
            elif self.bot_left_tree is None:
                self.bot_left_tree = Quad(
                    Point(self.top_left.x, (self.top_left.y + self.bot_right.y) / 2),
                    Point(str_average(self.top_left.x, self.bot_right.x), self.bot_right.y)
                )
                self.bot_left_tree.insert(node)
        elif (self.top_left.y + self.bot_right.y) / 2 >= node.pos.y:
            if self.top_right_tree is None:
                self.top_right_tree = Quad(
                    Point(str_average(self.top_left.x, self.bot_right.x), self.top_left.y),
                    Point(self.bot_right.x, (self.top_left.y + self.bot_right.y) / 2)
                )
                self.top_right_tree.insert(node)
            elif self.bot_right_tree is None:
                self.bot_right_tree = Quad(
                    Point(str_average(self.top_left.x, self.bot_right.x), (self.top_left.y + self.bot_right.y) / 2),
                    Point(self.bot_right.x, self.bot_right.y))
                self.bot_right_tree.insert(node)

    def mass_insert(self, data_array):
        for d in data_array:
            new_point = Point(d.surname, d.awards)
            new_node = Node(new_point, d)
            self.insert(new_node)

    def in_boundary(self, p):
        return self.top_left.x <= p.x <= self.bot_right.x and self.top_left.y <= p.y <= self.bot_right.y
