# def surfaceArea(self, grid: List[List[int]]) -> int:
#         surfacearea = 0
#         for box in grid:
#             for e in box:
#                 if e > 0:
#                     surfacearea += 1
#         surfacearea *= 2

#         sidearea = 0
#         for box in grid:
#             a = max(grid)
#             sidearea += int(a)
#         sidearea *= 2
#         surfacearea += sidearea

#         sidearea = 0
#         new_list = []
#         for i in range(len(grid)):
#             for j in range(len(grid[j])):
#                 new_list.append(grid[j][i])
#             a = max(new_list)
#             sidearea += int(a)
#             new_list = []
#         sidearea *= 2
#         surfacearea += sidearea

#         return surfacearea

# surfaceArea()


#working code
# class Solution(object):
#     def surfaceArea(self, grid):
#         n = len(grid)
#         surfacearea = 0

#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j] > 0:
#                     # Add top and bottom surface
#                     surfacearea += 2
#                     # Add sides
#                     surfacearea += grid[i][j] * 4

#                     # Subtract overlaps with adjacent cells
#                     if i > 0:
#                         surfacearea -= min(grid[i][j], grid[i-1][j]) * 2
#                     if j > 0:
#                         surfacearea -= min(grid[i][j], grid[i][j-1]) * 2

#         return surfacearea
