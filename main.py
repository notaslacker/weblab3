import math

class Sphere:
    def __init__(self, r=1, x=0, y=0, z=0):
        self.__radius = r
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
    
    @property
    def radius(self):
        return self.__radius
        
    @radius.setter
    def radius(self, r):
        if r > 0:
            self.__radius = r
        else:
            raise ValueError
    
    @property
    def pos_x(self):
        return self.__pos_x
    
    @pos_x.setter
    def pos_x(self, x):
        self.__pos_x = x
        
    @property
    def pos_y(self):
        return self.__pos_y
        
    @pos_y.setter
    def pos_y(self, y):
        self.__pos_y = y
    
    @property
    def pos_z(self):
        return self.__pos_z
        
    @pos_z.setter
    def pos_z(self, z):
        self.__pos_z = z
        
    def get_volume(self):
        return 4 * math.pi * self.radius**3 / 3
    
    def get_square(self):
        return 4 * math.pi * self.radius**2
        
    def get_radius(self):
        return self.radius
        
    def get_center(self):
        center = (self.pos_x, self.pos_y, self.pos_z)
        return center
    
    def set_radius(self, r):
        self.radius = r
    
    def set_center(self, x, y, z):
        self.pos_x = x
        self.pos_y = y  
        self.pos_z = z
    
    def is_point_inside(self, x, y, z):
        return (self.pos_x - x)**2 + (self.pos_y - y)**2 + (self.pos_z - z)**2 < self.radius**2
    
    
class Matrix:
    def __init__(self, m):
        self.__matrix = m
    
    @property
    def matrix(self):
        return self.__matrix
    
    @matrix.setter
    def matrix(self, m):
        self.__matrix = m
    
    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                sum = other[i][j] + self.matrix[i][j]
                numbers.append(sum)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)
    
    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)
    
    def __getitem__(self, pos):
        return self.matrix[pos]
        
    def __mul__(self, other):
        other = Matrix(other)
        sum  = 0
        temp = []
        result = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                for k in range(len(self.matrix[0])):
                   sum = sum + self.matrix[i][k] * other[k][j]
                temp.append(sum)
                sum = 0
            result.append(temp)
            temp = []           
        return Matrix(result)
    
    def det(self, mul):
        width = len(self.matrix)
        if width == 1:
            return mul * self.matrix[0][0]
        else:
            sign = -1
            answer = 0
            for i in range(width):
                temp = []
                for j in range(1, width):
                    buff = []
                    for k in range(width):
                        if k != i:
                            buff.append(self.matrix[j][k])
                    temp.append(buff)
                sign *= -1
                m = Matrix(temp)
                answer = answer + mul * m.det(sign * self.matrix[0][i])
        return answer
    
    def __lt__(self, other):
        return self.det(1) < other.det(1)
    
    def __le__(self, other):
        return self.det(1) <= other.det(1)
    
    def __eq__(self, other):
        return self.det(1) == other.det(1)
        
    def __ne__(self, other):
        return self.det(1) != other.det(1)
    
    def __gt__(self, other):
        return self.det(1) > other.det(1)
    
    def __ge__(self, other):
        return self.det(1) >= other.det(1)

import requests

class Client:
    def __init__(self):
        self.s = requests.Session()
    
    def req(self, url):
        return self.s.get(url)
    
    def __del__(self):
        self.s.close()
        
print("TASK 1")
   
default_sphere = Sphere()
print(default_sphere.get_volume())
print(default_sphere.get_square())
print(default_sphere.get_radius())
print(default_sphere.get_center())
default_sphere.set_radius(4)
print(default_sphere.get_radius())
default_sphere.set_center(-1, 2, -3)
print(default_sphere.get_center())
print(default_sphere.is_point_inside(0, 0, 0))
print(default_sphere.is_point_inside(0, 5, 0))

print('\n')

param_sphere = Sphere(10, 234, -39, 0)
print(param_sphere.get_volume())
print(param_sphere.get_square())
print(param_sphere.get_radius())
print(param_sphere.get_center())
param_sphere.set_radius(8)
print(param_sphere.get_radius())
param_sphere.set_center(1.1, 2.3, 3.9)
print(param_sphere.get_center())
print(param_sphere.is_point_inside(5, 6, 7))
print(param_sphere.is_point_inside(10, 10, 10))

print("TASK 2")
m1 = Matrix([[1, 1], [2, 2]])
m2 = Matrix([[1, 2], [3, 4]])
print(m1)
print('\n')
print(m2)
print('\n')
print(m1 + m2)
print('\n')
print(m1 * m2)
print('\n')
print(m1.det(1))
print(m2.det(1))
print(m2 < m1)
print(m2 <= m1)
print(m2 > m1)
print(m2 >= m1)
print(m2 == m1)
print(m2 != m1)
