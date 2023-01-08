# def lsh(data, threshold):
#     for d1 in data:
#         for d2 in data:
#             if lsh_ratio(d1.education, d2.education) < threshold:
#                 return []
#     return data


def lsh(data, threshold):
    out = []
    for d1 in data:
        if not out:
            out.append(d1)
            continue
        for d2 in out:
            if lsh_ratio(d1.education, d2.education) < threshold:
                out.append(d1)
    return out


def lsh_ratio(vector1, vector2):
    max_length = max(len(vector1), len(vector2))
    return count_equal_elements(vector1, vector2) / max_length


def count_equal_elements(vector1, vector2):
    count = 0
    for e in vector1:
        if e in vector2:
            count += 1
    return count

