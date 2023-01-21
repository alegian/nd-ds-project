from str_utils import str_diff_norm_squared


class MBR:
    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax


def calc_area(mbr, data):
    x = data.surname
    y = data.awards

    if mbr.xmin <= x <= mbr.xmax and mbr.ymin <= y <= mbr.ymax:
        return 0

    if x <= mbr.xmin and y <= mbr.ymin:
        dx = str_diff_norm_squared(mbr.xmin, x)
        dy = abs(mbr.ymin - y)
        return dx*dy
    elif x >= mbr.xmax and y >= mbr.ymax:
        dx = str_diff_norm_squared(mbr.xmax, x)
        dy = abs(mbr.ymax - y)
        return dx*dy


def find_min_child(children, data):
    min_area = float('inf')
    min_child = children[0]
    for child in children:
        area = calc_area(child.mbr, data)
        print(area)
        if area < min_area:
            min_area = area
            min_child = child
    return min_child


class RTree:
    def __init__(self, data=None):
        self.data = data
        self.children = []
        self.mbr = None

        if data is not None:
            self.mbr = MBR(data.surname, data.surname, data.awards, data.awards)

    def mass_insert(self, arr):
        for item in arr:
            self.insert(item)

    def insert(self, data):
        if len(self.children) < 3:
            self.children.append(RTree(data))
            if self.mbr is None:
                self.mbr = MBR(data.surname, data.surname, data.awards, data.awards)
            else:
                if self.mbr.xmin > data.surname:
                    self.mbr.xmin = data.surname
                if self.mbr.xmax < data.surname:
                    self.mbr.xmax = data.surname
                if self.mbr.ymin > data.awards:
                    self.mbr.ymin = data.awards
                if self.mbr.ymax < data.awards:
                    self.mbr.ymax = data.awards
        else:
            min_child = find_min_child(self.children, data)
            if not min_child.is_leaf():
                min_child.insert(data)
            else:
                new_node = RTree(min_child.data)
                min_child.data = None
                min_child.children.append(new_node)

    def range_query(self, surname_min, surname_max, award_min, award_max):
        if self.is_leaf():
            if surname_min <= self.data.surname <= surname_max and award_min <= self.data.awards <= award_max:
                return [self.data]
            else:
                return []
        else:
            out = []
            for child in self.children:
                if child is not None:
                    out.extend(child.range_query(surname_min, surname_max, award_min, award_max))
            return list(set(out))

    def is_leaf(self):
        return self.data is not None
