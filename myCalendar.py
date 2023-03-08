# https://leetcode.com/problems/my-calendar-i/
# 729. My Calendar I


# class Node:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.left = None
#         self.right = None

#     def insert(self, node):
#         if node.end <= self.start:
#             if not self.left:
#                 self.left = node
#                 return True
#             else:
#                 return self.left.insert(node)
#         elif self.end <= node.start:
#             if not self.right:
#                 self.right = node
#                 return True
#             else:
#                 return self.right.insert(node)
#         else:
#             return False


# class MyCalendar:
#     def __init__(self):
#         self.root = None

#     def book(self, start: int, end: int) -> bool:
#         if not self.root:
#             self.root = Node(start, end)
#             return True
#         else:
#             return self.root.insert(Node(start, end))


class MyCalendar:
    def __init__(self):
        self.books = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.books:
            if s < end and start < e:
                return False
        self.books.append((start, end))
        return True


# obj = MyCalendar()
# param_1 = obj.book(start, end)


# driver code
test1 = [[10, 20], [15, 25], [20, 30], [25, 35]]
calendar = MyCalendar()

result = []
expected_result = [True, False, True, False]

for test in test1:
    result.append(calendar.book(test[0], test[1]))

print(result)
print(result == expected_result)

# for i in result:
#     print(result)

# print(result)


# https://www.youtube.com/watch?v=YZdIwAEtgIY

# Your MyCalendar object will be instantiated and called as such:
