n = int(input())
boxes = list(map(int, input().split()))

# Sort the boxes by their side lengths
boxes.sort()

# Initialize variables
visible_boxes = 1
max_side = boxes[0]

# Iterate through the boxes starting from the second one
for i in range(1, n):
    # If the current box's side length is greater than max_side,
    # update max_side and increment the count of visible boxes
    if boxes[i] > max_side:
        visible_boxes += 1
        max_side = boxes[i]

print(visible_boxes)
