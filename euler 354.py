import math
class cell:
    population = 0
    def __init__(self,coordx,coordy):
        self.coordx=coordx
        self.coordy=coordy
        self.distance = cell.distance(coordx,coordy)
        cell.population +=1
        
    def __del__(self):
        cell.population -=1
        
    def distance(coordx,coordy):
        dist = math.sqrt(coordx**2 +coordy**2)
        return dist
    

cells=[cell(0,0)]
for cel in cells:
    for n in range (225):
        cells.append (cell(cel.coordx+(n*math.sqrt(3/4)),cel.coordy+(n*1.5)))
        cells.append (cell(cel.coordx+(n*math.sqrt(3/4)),cel.coordy-(n*1.5)))
for cel in cells:
    for n in range (225):
        cells.append (cell(cel.coordx),cel.coordy+(n*math.sqrt3))
        cells.append (cell(cel.coordx),cel.coordy-(n*math.sqrt3))
print ('there are {0} cells so far in the honey comb'.format(len(cells)))
