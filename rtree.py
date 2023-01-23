from str_utils import str_diff_norm_squared


class MBR:
    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def contains(self, x, y):
        return self.xmin <= x <= self.xmax and self.ymin <= y <= self.ymax

    def extend(self, x, y):
        new_mbr = MBR(self.xmin, self.xmax, self.ymin, self.ymax)
        if new_mbr.xmin > x:
            new_mbr.xmin = x
        if new_mbr.xmax < x:
            new_mbr.xmax = x
        if new_mbr.ymin > y:
            new_mbr.ymin = y
        if new_mbr.ymax < y:
            new_mbr.ymax = y
        return new_mbr

    def calc_area(self):
        dx = str_diff_norm_squared(self.xmax, self.xmin)
        dy = self.ymax - self.ymin
        return dx * dy

    def area_increase(self, x, y):
        if self.contains(x, y):
            return 0
        else:
            extended = self.extend(x, y)
            diff = extended.calc_area() - self.calc_area()
            return diff


def find_min_child(children, data):
    min_area = float('inf')
    min_child = children[0]
    for child in children:
        area = child.mbr.area_increase(data.surname, data.awards)
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
                self.mbr = self.mbr.extend(data.surname, data.awards)
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
