from kd import KDTree
from quad import Quad
from range import Range
from rtree import RTree
from data import generate_data
from lsh import lsh


if __name__ == '__main__':
    data = generate_data(200)
    mode = input("""
    Enter operation mode: 
        mode 0: k-d tree
        mode 1: quad tree
        mode 2: range tree
        mode 3: r-tree
    """)
    mode = int(mode)
    range_results = []

    if mode == 0:
        kd_tree = KDTree(data)
        range_results = kd_tree.range_query("h", "l", 5, 20)
    elif mode == 1:
        quad_tree = Quad()
        quad_tree.mass_insert(data)
        range_results = quad_tree.range_query('abramopoulos', 'karagiannis', 0, 70)
    elif mode == 2:
        tree = Range(data)
        range_results = tree.range_query('p', 'zz', 0, 99)
    elif mode == 3:
        rtree = RTree()
        rtree.mass_insert(data)
        range_results = rtree.range_query('g', 'p', 5, 9)

    lsh_results = lsh(range_results, 0.6)
    print(list(map(lambda x: f'{x.surname} {x.awards}', lsh_results)))
