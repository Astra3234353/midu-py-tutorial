nums = [1, 2, 3, 4]
goal = 6

def find_goal(list, goal):
  for i in range(len(list)):
    for j in range(i + 1, len(list)):
      if list[i] + list[j] == goal:
        return f"For {goal}, i:{i}, j:{j}"
  return None

print(find_goal(nums, goal))