class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        key = (point[0],point[1])
        self.points[key]=self.points.get(key,0)+1

    def count(self, point: List[int]) -> int:
        x,y = point
        ans = 0
        for (px,py) in self.points:
            if abs(px-x) != abs(py-y) or px==x:
                continue
            p1 = (px, y)
            p2 = (x, py)
            ans += (self.points[(px,py)]*self.points.get(p1,0)*self.points.get(p2,0)) 
        return ans