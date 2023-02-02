from kd import KDTree
from quad import Quad
from range import Range
from rtree import RTree
from data import generate_data
import time
from statistics import mean
from lsh import lsh


if __name__ == '__main__':
    creation_times = []
    query_times = []

    for i in range(10):
        data = generate_data(2000)
        print(f'iteration {i}...')
        new_creation_row = []
        new_query_row = []

        start = time.time()
        kd = KDTree(data)
        end = time.time()
        new_creation_row.append(end-start)
        start = time.time()
        kd.range_query('bell', 'erdos', 7, 12)
        end = time.time()
        new_query_row.append(end-start)

        start = time.time()
        quad = Quad()
        quad.mass_insert(data)
        new_creation_row.append(end - start)
        start = time.time()
        quad.range_query('bell', 'erdos', 7, 12)
        end = time.time()
        new_query_row.append(end - start)

        start = time.time()
        rangetree = Range(data)
        new_creation_row.append(end - start)
        start = time.time()
        rangetree.range_query('bell', 'erdos', 7, 12)
        end = time.time()
        new_query_row.append(end - start)

        start = time.time()
        rtree = RTree()
        rtree.mass_insert(data)
        new_creation_row.append(end - start)
        start = time.time()
        rtree.range_query('bell', 'erdos', 7, 12)
        end = time.time()
        new_query_row.append(end - start)

        creation_times.append(new_creation_row)
        query_times.append(new_query_row)

    print(f'k-d average creation time seconds: {mean(creation_times[:][0])}')
    print(f'k-d average query time seconds: {mean(query_times[:][0])}')
    print(f'quad average creation time seconds: {mean(creation_times[:][1])}')
    print(f'quad average query time seconds: {mean(query_times[:][1])}')
    print(f'range average creation time seconds: {mean(creation_times[:][2])}')
    print(f'range average query time seconds: {mean(query_times[:][2])}')
    print(f'rtree average creation time seconds: {mean(creation_times[:][3])}')
    print(f'rtree average query time seconds: {mean(query_times[:][3])}')


