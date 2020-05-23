def solution(x, y, r, d, target):
    answer = 0

    import math

    def angle(a, b, c):
        ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
        return ang + 360 if ang < 0 else ang



    for t in target:
        ang = angle([x, y], [0, 0], t)
        if ang > 180:
            ang = 360 - ang
        if ang <= d:
            if math.hypot(t[0], t[1]) <= r:
                answer += 1

    return answer

print(solution(-1, 2, 2, 60, [[0, 1], [-1, 1], [1, 0], [-2, 2]]))