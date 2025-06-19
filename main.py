from homlib import Graph, hom

# T = Graph(3)
# T.addEdge(0,1)
# T.addEdge(1,2)
#
# G = Graph(3)
# G.addEdge(0,1)
# G.addEdge(1,2)
# G.addEdge(2,0)
#
# print(hom(T, G)) # 12

# K5,5/C10
H = Graph(10)
#H.addEdge(0, 5)
#H.addEdge(0, 6)
H.addEdge(0, 7)
H.addEdge(0, 8)
H.addEdge(0, 9)
H.addEdge(1, 5)
#H.addEdge(1, 6)
#H.addEdge(1, 7)
H.addEdge(1, 8)
H.addEdge(1, 9)
H.addEdge(2, 5)
H.addEdge(2, 6)
#H.addEdge(2, 7)
#H.addEdge(2, 8)
H.addEdge(2, 9)
H.addEdge(3, 5)
H.addEdge(3, 6)
H.addEdge(3, 7)
#H.addEdge(3, 8)
#H.addEdge(3, 9)
#H.addEdge(4, 5)
H.addEdge(4, 6)
H.addEdge(4, 7)
H.addEdge(4, 8)
#H.addEdge(4, 9)

# K4,4
# H = Graph(8)
# H.addEdge(0, 4)
# H.addEdge(0, 5)
# H.addEdge(0, 6)
# H.addEdge(0, 7)
# H.addEdge(1, 4)
# H.addEdge(1, 5)
# H.addEdge(1, 6)
# H.addEdge(1, 7)
# H.addEdge(2, 4)
# H.addEdge(2, 5)
# H.addEdge(2, 6)
# H.addEdge(2, 7)
# H.addEdge(3, 4)
# H.addEdge(3, 5)
# H.addEdge(3, 6)
# H.addEdge(3, 7)

# G = Graph(2)
# G.addEdge(0, 1)
# print(hom(H, G)) # 2

# G = Graph(4)
# G.addEdge(0, 1)
# G.addEdge(0, 3)
# G.addEdge(1, 2)
# G.addEdge(1, 3)
# print(hom(H, G)) # 848

G = Graph(6)
G.addEdge(0, 3)
G.addEdge(0, 4)
G.addEdge(0, 5)
G.addEdge(1, 3)
G.addEdge(1, 4)
G.addEdge(1, 5)
G.addEdge(2, 3)
G.addEdge(2, 4)
G.addEdge(2, 5)
print(hom(H, G)) # 118098

# G = Graph(10)
# G.addEdge(0, 5)
# G.addEdge(0, 6)
# G.addEdge(0, 7)
# G.addEdge(0, 8)
# G.addEdge(0, 9)
# G.addEdge(1, 5)
# G.addEdge(1, 6)
# G.addEdge(1, 7)
# G.addEdge(1, 8)
# G.addEdge(1, 9)
# G.addEdge(2, 5)
# G.addEdge(2, 6)
# G.addEdge(2, 7)
# G.addEdge(2, 8)
# G.addEdge(2, 9)
# G.addEdge(3, 5)
# G.addEdge(3, 6)
# G.addEdge(3, 7)
# G.addEdge(3, 8)
# G.addEdge(3, 9)
# G.addEdge(4, 5)
# G.addEdge(4, 6)
# G.addEdge(4, 7)
# G.addEdge(4, 8)
# G.addEdge(4, 9)
# print(hom(H, G)) # 19531250

'''
Approximations
[1865, 18650000.0]
[1973, 19730000.0]
[1986, 19860000.0]
[1928, 19280000.0]
[2029, 20290000.0]
[1950, 19500000.0]
[1942, 19420000.0]
[1959, 19589999.999999996]
[1942, 19420000.0]
[1935, 19350000.0]
'''

#12 Vertex G
# G = Graph(12)
# G.addEdge(0,1)
# G.addEdge(0,2)
# G.addEdge(0,4)
# G.addEdge(0,8)
# G.addEdge(0,9)
# G.addEdge(0,10)
# G.addEdge(1,2)
# G.addEdge(1,5)
# G.addEdge(1,7)
# G.addEdge(1,9)
# G.addEdge(1,11)
# G.addEdge(2,3)
# G.addEdge(2,7)
# G.addEdge(2,8)
# G.addEdge(2,11)
# G.addEdge(3,6)
# G.addEdge(3,7)
# G.addEdge(3,8)
# G.addEdge(3,10)
# G.addEdge(4,5)
# G.addEdge(4,6)
# G.addEdge(4,8)
# G.addEdge(4,11)
# G.addEdge(5,6)
# G.addEdge(5,8)
# G.addEdge(5,10)
# G.addEdge(6,10)
# G.addEdge(7,8)
# G.addEdge(7,10)
# G.addEdge(7,11)
# G.addEdge(8,9)
# G.addEdge(8,10)
# G.addEdge(9,10)
# G.addEdge(9,11)
# print(hom(H, G)) # 5654308

