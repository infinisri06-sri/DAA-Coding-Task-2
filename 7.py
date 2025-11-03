import math
def brute_force(points):
    min_distance = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            if dist < min_distance:
                min_distance = dist
    return min_distance


def check_strip(strip, min_dist):
    strip.sort(key=lambda p: p[1])  
    min_strip_dist = min_dist
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_strip_dist:
            dist = math.sqrt((strip[i][0] - strip[j][0])*2 + (strip[i][1] - strip[j][1])*2)
            if dist < min_strip_dist:
                min_strip_dist = dist
            j += 1
    return min_strip_dist

def closest_pair(points_sorted_by_x):
    n = len(points_sorted_by_x)

    if n <= 3:
        return brute_force(points_sorted_by_x)


    mid = n // 2
    midpoint = points_sorted_by_x[mid]
    left_half = points_sorted_by_x[:mid]
    right_half = points_sorted_by_x[mid:]

   
    left_min = closest_pair(left_half)
    right_min = closest_pair(right_half)

    min_dist = min(left_min, right_min)

  
    strip = []
    for p in points_sorted_by_x:
        if abs(p[0] - midpoint[0]) < min_dist:
            strip.append(p)

    strip_min = check_strip(strip, min_dist)
    return min(min_dist, strip_min)

points = [(4, 3), (5, 6), (40, 30), (5, 1), (12, 10), (3, 4)]
points_sorted_by_x = sorted(points, key=lambda p: p[0])
print("Closest distance:", closest_pair(points_sorted_by_x))
