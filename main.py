from kd import KDTree


def lsh():
    print('lmao')


if __name__ == '__main__':
    points = [
        [1, 2, 3],
        [4, 5, 5],
        [2, 1, 2],
        [7, 7, 7],
    ]
    kd_tree = KDTree(points, 3)
    knn = kd_tree.get_knn([1, 1, 1], 1, False)
    print(knn)
