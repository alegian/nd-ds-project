class MBR:
    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax


def calc_area(mbr, data):
    # smart function

def find_min_child(children, data):
    min_area = float('inf')
    min_child = children[0]
    for child in children:
        area = calc_area(child.mbr, data)
        if area < min_area:
            min_area = area
            min_child = child
    return min_child

class RTree:
    def __init__(self, data=None):
        self.data = data
        self.children = []

        if data is not None:
            self.mbr = MBR(data.surname, data.surname, data.awards, data.awards)

    def insert(self, data):
        if len(self.children) < 3:
            self.children.append(RTree(data))
            # update MBR
        else:
            min_child = find_min_child(self.children, data)
            if not min_child.is_leaf():
                min_child.insert(data)
            else:
                new_node = RTree(min_child.data)
                min_child.data = None
                min_child.insert(new_node)

    def is_leaf(self):
        return self.data is not None
