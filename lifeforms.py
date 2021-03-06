import cellset

class Lifeforms():
    """
    Common lifeforms to place
    Can be stored in set without specified cell id, which makes them placed as selected id
    OR
    The points are stored with their cell id specified, and placed with the corresponding id
    """
    def __init__(self, sel='glider'):
        self.funcList = {'Flip Horizontal': self.flipHorizontal, 'Flip Vertical': self.flipVertical,
                         'Rotate Right': self.rotateRight, 'Rotate Left': self.rotateLeft}
        self.species = {'glider': {(-1,-1),(1,0),(-1,0),(0,-1),(-1,1)},
                        'LWSS': {(0,1),(0,4),(1,0),(2,0),(2,4),(3,0),(3,1),(3,2),(3,3)},
                        'toad': {(0,2),(1,0),(1,3),(2,0),(2,3),(3,1)},
                        'beacon': {(0,0),(0,1),(1,0),(2,3),(3,2),(3,3)},
                        'pentadecathlon': {(0,1),(1,1),(2,0),(2,2),(3,1),(4,1),
                                           (5,1),(6,1),(7,2),(7,0),(8,1),(9,1)},
                        'R-pentomino': {(0,1),(0,2),(1,0),(1,1),(2,1)},
                        'Diehard': {(0,6),(1,0),(1,1),(2,1),(2,5),(2,6),(2,7)},
                        'Acorn': {(0,1),(1,3),(2,0),(2,1),(2,4),(2,5),(2,6)},
                        'Infinity Line': {(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,9),
                                                   (0,10),(0,11),(0,12),(0,13),(0,17),(0,18),(0,19),(0,26),
                                                   (0,27),(0,28),(0,29),(0,30),
                                                   (0,31),(0,32),(0,34),(0,35),(0,36),(0,37),(0,38)},
                        'Clipboard':set(),
               }
        self.selection = sel
        self.setPoints = self.species[self.selection]
        
        
    def rotateLeft(self):
        newSet = set()
        for p in self.setPoints:
            if type(p) is cellset.Cell:
                newP = cellset.Cell(p[1], p[0], p.cid)
            else:
                newP = (p[1], p[0])
            newSet.add(newP)
        self.setPoints = newSet.copy()
        self.flipVertical()

    def rotateRight(self):
        self.flipVertical()
        newSet = set()
        for p in self.setPoints:
            if type(p) is cellset.Cell:
                newP = cellset.Cell(p[1], p[0], p.cid)
            else:
                newP = (p[1], p[0])
            newSet.add(newP)
        self.setPoints = newSet.copy()

    def flipHorizontal(self):
        newSet = set()
        for p in self.setPoints:
            if type(p) is cellset.Cell:
                newP = cellset.Cell(p[0], p[1]*-1, p.cid)
            else:
                newP = (p[0], p[1]*-1)
            newSet.add(newP)
        self.setPoints = newSet.copy()

    def flipVertical(self):
        newSet = set()
        for p in self.setPoints:
            if type(p) is cellset.Cell:
                newP = cellset.Cell(p[0]*-1, p[1], p.cid)
            else:
                newP = newSet.add((p[0]*-1, p[1]))
            newSet.add(newP)
        self.setPoints = newSet.copy()
            
        
    def getLifeformSet(self, row, col, rowOffset, colOffset, cid):
        translatedSet = set()
        for coordPair in self.setPoints:
            x = coordPair[1] + col + colOffset
            y = coordPair[0] + row + rowOffset
            if type(coordPair) is cellset.Cell:
                newCell = cellset.Cell(y,x,coordPair.cid)
            else:
                newCell = cellset.Cell(y,x,cid)
            translatedSet.add(newCell)
        return translatedSet

    def setSpecies(self, sel):
        self.selection = sel
        self.setPoints = self.species[sel]
