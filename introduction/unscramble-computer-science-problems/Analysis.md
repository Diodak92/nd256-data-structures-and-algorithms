###  Worst Case Scenario Analysis - Big-O Notation

## Task0

The function simply returns the first and last elements from the list without any sorting, so its time complexity is constant O(1).

## Task1

The script iterates over the list of calls O(n) and the list of texts O(p) sequentially, each loop having linear time complexity. Finally, the program converts a list to a set, which also requires linear time O(r).
Overall, the complexity remains linear, growing proportionally to the combined sizes of the calls and texts lists.

## Task2

The script iterates over all elements in the list, which results in linear time complexity, and performs insert/update operations on a dictionary, which run in constant time. Finding the maximum value in the results dictionary also requires scanning all elements, giving it a time complexity of O(n). Therefore, the overall complexity is O(n).

## Task3

The third script contains two loops. The first loop checks whether each element is in a list, which requires scanning all elements of that list. Because this check occurs inside the loop, the time complexity is O(n^2).
The sorting operation has a computational complexity of O(n log n), and the constant time calculations are O(1). Overall, the dominant part of the script is the first loop, resulting in a total time complexity of O(n^2)

## Task4

The last script contains three loops, each performing a membership check with a computational complexity of O(n). Because each loop runs this check inside an iteration over all elements, each loop operates in O(n^2) time. Since all loops have the same complexity, the overall computational complexity of the script is also O(n^2).
