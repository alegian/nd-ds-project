from kd import KDTree
from quad import Quad, Point
from data import data


def lsh():
    print('lmao')


if __name__ == '__main__':
    # kd_tree = KDTree(data)
    # range_results = kd_tree.range_query("a", "l", 0, 20)
    # print(list(map(lambda x: x.surname, range_results)))

    quad_tree = Quad()
    quad_tree.mass_insert(data)
    range_results = quad_tree.range_query('abramopoulos', 'karagiannis', 0, 70)
    print(list(map(lambda x: x.surname, range_results)))

