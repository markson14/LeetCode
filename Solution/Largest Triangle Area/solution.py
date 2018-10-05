import itertools
def largestTriangleArea(points):
    """
    :type points: List[List[int]]
    :rtype: float
    """
    area = 0
    for i, j, k in itertools.combinations(points, 3):
        area = max(area, 0.5 * abs(i[0] * j[1] +
                                    j[0] * k[1] +
                                    k[0] * i[1] -
                                    j[0] * i[1] -
                                    k[0] * j[1] -
                                    i[0] * k[1]))

    return area
if __name__ == '__main__':
    points = [[9,4],[5,8],[6,1]]
    print(largestTriangleArea(points))
        
        