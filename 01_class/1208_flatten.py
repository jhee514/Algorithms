import sys
sys.stdin = open("input_flatten.txt", "r")

def flatten(d, heights):
    for t in range(d):
        maxValue = heights[0]
        minValue = heights[0]
        for i in range(1, len(heights)):
            if heights[i] > maxValue:
                maxValue = heights[i]
            if heights[i] < minValue:
                minValue = heights[i]
        heights[heights.index(maxValue)] -= 1
        heights[heights.index(minValue)] += 1
    return maxValue - minValue

# def flatten(d, heights):
    # for t in range(d):
    #     heights[heights.index(max(heights))] -= 1
    #     heights[heights.index(min(heights))] += 1
    # return max(heights) - min(heights)


for tc in range(1, 11):
    d = int(input())
    heights = list(map(int, input().split()))
    print("#%d %d" % (tc, flatten(d, heights)))


# sol.
def