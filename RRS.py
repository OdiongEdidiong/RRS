# Find the best way to move from one point to another 

roads={}
def add_routes(start,end,dist):
    if start not in roads:
        roads[start]={}
    if end not in roads:
        roads[end]={}
        roads[start][end]=dist
add_routes("a","b",7)
add_routes("a","c",1)
add_routes("b","e",2)
add_routes("c","d",3)
add_routes("d","e",1)
add_routes("d","f",8)
add_routes("e","f",4)
add_routes("e","g",1)
roads

def best_route(start,end,roads):
    # Assign infinity to all points in the graph
    costs={}
    for route in roads:
        costs[route]=float("inf")
    costs[start]=0
    explored=[]
    parents={}
    def find_lowest_cost():
        lowest_cost_road=None 
        lowest_cost=float("inf")
        for node,cost in costs.items():
            if cost<lowest_cost and node in explored:
                lowest_cost_road=node
                lowest_cost=cost
        return lowest_cost_road
        
    lcn=find_lowest_cost()
    while lcn is not None:
        cost=costs[lcn]
        for neighbor in roads[lcn]:
            new_cost=cost+roads[lcn][neighbor]
            if new_cost < costs[neighbor]:
                cost[neighbor]=new_cost
                parents[neighbor]=lcn
            
        explored.append(lcn)
        lcn = find_lowest_cost()
    def show_route(end):
        suggested_route=[]
        road=end
        while road in parents:
            suggested_route.append(road)
            road=parents[road]
        suggested_route.append(start)
        suggested_route.reverse()
        return suggested_route
    return show_route(end)
