import math

class Point :
    def __init__(self,x:float = 0.0,y:float = 0.0):
        self.__x = x
        self.__y = y

    #accesseur
    def get_x(self)->float:
        return self.__x

    def set_x(self,x:float):
        self.__x = x

    def get_y(self) -> float:
        return self.__y

    def set_y(self, y: float):
        self.__y = y

    x = property (get_x,set_x)
    y = property(get_y, set_y)

    """deuxieme methode des accesseurs
    
    @x.getter #ou @property
    def x(self)->float:
        return self.__x
    
    @x.setter
    def x(self,x:float):
        self.__x = x

    @y.getter
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y
        """""
    def __str__(self)->str:
        return f"Point ({self.__x};{self.__y})"

    def distanceCoord(self,x:float,y:float)->float:
        return math.sqrt((self.__x -x)**2 +
                         (self.__y +y)**2)

    def distancePoint(self,camarade)->float:
        return math.sqrt((self.__x - camarade.__x)**2 +
                         (self.__y - camarade.__y)**2)





if __name__ == "__main__":
    p1:Point = Point()
    p2:Point= Point(3,4)
    p3:Point = Point(2.1,3)
    print(p1)
    print(vars(p1))
    print(p2.__dict__)
    print(p2)
    print(p1.distanceCoord(2.1,3)) #distance entre p1 et 2.1 ,3 (p3)
    print(p3.distanceCoord(0, 0))  #distance entre p3 et 0 , 0 (p1)
    print(p1.distancePoint(Point(2.1,3)))