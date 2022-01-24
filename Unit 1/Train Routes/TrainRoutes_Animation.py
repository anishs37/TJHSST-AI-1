import sys
import time
import math
from math import pi , acos , sin , cos
from heapq import heappush, heappop, heapify
import tkinter as tk

dict_city_junction = {}
dict_city_coordinates = {}
dict_node_city = {}
lines = {}

with open("rrEdges.txt") as f:
    edges = [line.strip() for line in f]

with open("rrNodes.txt") as f:
    nodes = [line.strip() for line in f]

with open("rrNodeCity.txt") as f:
    nodeCity = [line.strip() for line in f]

for node in nodes:
    line_split = node.split(" ")
    junct = line_split[0]
    lat = float(line_split[1])
    long = float(line_split[2])
    dict_city_coordinates[junct] = (lat, long)

def create_grid(r, c):
    for line in edges:
        line_split = line.split(" ")
        city1 = line_split[0]
        city2 = line_split[1]
        
        city1lat, city1long = dict_city_coordinates.get(city1)
        city2lat, city2long = dict_city_coordinates.get(city2)

        city1lat *= 10
        city1long *= 10
        city2lat *= 10
        city2long *= 10

        line2 = c.create_line([(800-(city1long * -1-600), 800 - city1lat), (800-(city2long * - 1-600), 800 - city2lat)], tag='grid_line')
        lines[(city1, city2)] = line2
        lines[(city2, city1)] = line2

    r.update()

count2 = 0
def make_red(r, c, state, ch):
    global count2
    count2 = count2 + 1
    line = lines.get((state, ch))
    c.itemconfig(line, fill="red") 

    if(count2 % 1000 == 0):
        r.update()

count6 = 0
def make_blue(r, c, state, ch):
    global count6
    count6 = count6 + 1
    line = lines.get((state, ch))
    c.itemconfig(line, fill="blue") 

    if(count6 % 500 == 0):
        r.update()

count4 = 0
def make_green(r, c, ancestors):
    global count4
    for i in range(len(ancestors) - 1):
        state = ancestors[i]
        ch = ancestors[i + 1]
        count4 = count4 + 1
        line = lines.get((state, ch))
        c.itemconfig(line, fill="green") 

        if(count4 % 50 == 0):
            r.update()
    
count8 = 0
def make_orange(r, c, ancestors):
    global count8
    for i in range(len(ancestors) - 1):
        state = ancestors[i]
        ch = ancestors[i + 1]
        count8 = count8 + 1
        line = lines.get((state, ch))
        c.itemconfig(line, fill="orange") 

        if(count8 % 25 == 0):
            r.update()

root = tk.Tk()

canvas = tk.Canvas(root, height=800, width=800, bg='white')
create_grid(root, canvas)
canvas.pack(expand=True)

start3 = time.perf_counter()

def calcd(node1, node2):
   y1, x1 = node1
   y2, x2 = node2

   if((x1 == x2) and (y1 == y2)):
       return 0.0

   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   # approximate great circle distance with law of cosines
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

for line in edges:
    line_split = line.split(" ")
    city1 = line_split[0]
    city2 = line_split[1]
    
    city1lat, city1long = dict_city_coordinates.get(city1)
    city2lat, city2long = dict_city_coordinates.get(city2)    

    dist = calcd(dict_city_coordinates.get(city1), dict_city_coordinates.get(city2))

    if(city1 in dict_city_junction):
        junct_list = dict_city_junction.get(city1)
        elem = dict_city_junction.pop(city1, "ERROR")
        junct_list.append((city2, dist))
        dict_city_junction[city1] = junct_list

    else:
        dict_city_junction[city1] = [(city2, dist)]
    
    if(city2 in dict_city_junction):
        junct_list = dict_city_junction.get(city2)
        elem = dict_city_junction.pop(city2, "ERROR")
        junct_list.append((city1, dist))
        dict_city_junction[city2] = junct_list

    else:
        dict_city_junction[city2] = [(city1, dist)]

for city in nodeCity:
    cityList = city.split(" ")
    junct = cityList[0]
    cityItself = ' '.join(cityList[1:])
    dict_node_city[cityItself] = junct

end3 = time.perf_counter()
times3 = str(end3 - start3)
print("Time to build backing data structures: " + times3 + " seconds.")

def dijkstra(start_junct, end_junct):
    closed = set()
    fringe = []
    heappush(fringe, (0, start_junct, [start_junct]))

    while fringe:
        depth, state, ancestors = heappop(fringe)

        if(state == end_junct):
            make_green(root, canvas, ancestors)
            return depth
        
        if(state not in closed):
            closed.add(state)
            sLat, sLong = dict_city_coordinates.get(state)
            children_list = dict_city_junction.get(state)
            iter = 0
            for cAll in children_list:
                c, cDist = children_list[iter]
                cLat, cLong = dict_city_coordinates.get(c)
                make_red(root, canvas, state, c)
                #print("hi")
                if c not in closed:
                    c_ancestors = ancestors.copy()
                    c_ancestors.append(c)
                    new_depth = depth + cDist
                    heappush(fringe, (new_depth, c, c_ancestors))

                iter = iter + 1

    return None

def astar(start_junct, end_junct):
    closed = set()
    fringe = []
    heappush(fringe, (0, 0, start_junct, [start_junct]))

    while fringe:
        heuristic, depth, state, ancestors = heappop(fringe)

        if(state == end_junct):
            make_orange(root, canvas, ancestors)
            return depth
        
        if(state not in closed):
            closed.add(state)
            children_list = dict_city_junction.get(state)
            iter = 0
            for cAll in children_list:
                c, cDist = children_list[iter]
                cLat, cLong = dict_city_coordinates.get(c)
                make_blue(root, canvas, state, c)
                c, cDist = children_list[iter]

                if c not in closed:
                    c_ancestors = ancestors.copy()
                    c_ancestors.append(c)
                    new_f = calcd(dict_city_coordinates.get(c), dict_city_coordinates.get(end_junct))
                    new_depth = depth + cDist
                    heappush(fringe, (new_f + new_depth, new_depth, c, c_ancestors))

                iter = iter + 1

    return None

city1 = sys.argv[1]
city2 = sys.argv[2]

start = time.perf_counter()

coord1 = dict_node_city.get(city1)
coord2 = dict_node_city.get(city2)
dist1 = dijkstra(coord1, coord2)

end = time.perf_counter()
times = str(end - start)

print(city1 + " to " + city2 + " with Dijkstra: " + str(dist1) + " in " + times + " seconds.")
time.sleep(5)

start2 = time.perf_counter()
dist2 = astar(coord1, coord2)
end2 = time.perf_counter()
times2 = str(end2 - start2)

print(city1 + " to " + city2 + " with A*: " + str(dist2) + " in " + times2 + " seconds.")

root.mainloop()