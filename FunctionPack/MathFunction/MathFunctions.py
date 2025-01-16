# functional module
import math

class AngleUnit:
    def __init__(self):
        self.__Unit: str = "Degrees"
        
    def switch(self):
        self.__Unit = "Radians"
        
    def get(self) -> str:
        return self.__Unit
    
angle_unit = AngleUnit()

def sin(x):
    if angle_unit.get() == "Radians":
        res = round(math.sin(x),15)
    else :
        res = round(math.sin(math.radians(x)),15)
    return res

def cos(x):
    if angle_unit.get() == "Radians":
        res = round(math.cos(x),15)
    else :
        res = round(math.cos(math.radians(x)),15)
    return res

def tan(x):
    if angle_unit.get() == "Radians":
        if x%(math.pi/2)==0 and (x//(math.pi/2))%2!=0 :
            res = "Not Exist"
        else:
            res = round(math.tan(x),15)
    else :
        if x%(90)==0 and (x//(90))%2!=0 :
            res = "Not Exist"
        else:
            res = round(math.tan(math.radians(x)),15)
    return res

def sinh(x):
    if angle_unit.get() == "Radians":
        res = round(math.sinh(x),15)
    else :
        res = round(math.sinh(math.radians(x)),15)
    return res

def cosh(x):
    if angle_unit.get() == "Radians":
        res = round(math.cosh(x),15)
    else :
        res = round(math.cosh(math.radians(x)),15)
    return res

def tanh(x):
    if angle_unit.get() == "Radians":
        res = round(math.tanh(x),15)
    else :
        res = round(math.tanh(math.radians(x)),15)
    return res

def asin(x):
    if angle_unit.get() == "Radians":
        res = round(math.asin(x),10)
    else :
        res = round(math.degrees(math.asin(x)),10)
    return res

def acos(x):
    if angle_unit.get() == "Radians":
        res = round(math.acos(x),10)
    else :
        res = round(math.degrees(math.acos(x)),10)
    return res

def atan(x):
    if angle_unit.get() == "Radians":
        res = round(math.atan(x),10)
    else :
        res = round(math.degrees(math.atan(x)),10)
    return res

def asinh(x):
    if angle_unit.get() == "Radians":
        res = round(math.asinh(x),10)
    else :
        res = round(math.degrees(math.asinh(x)),10)
    return res

def acosh(x):
    if angle_unit.get() == "Radians":
        res = round(math.acosh(x),10)
    else :
        res = round(math.degrees(math.acosh(x)),10)
    return res

def atanh(x):
    if angle_unit.get() == "Radians":
        res = round(math.atanh(x),10)
    else :
        res = round(math.degrees(math.atanh(x)),10)
    return res

def fac(x):
    res = math.factorial(x)
    return res

def sqr(x):
    res = round(x**(1/2),15)
    return res

def cur(x):
    res = round(x**(1/3),15)
    return res

def abs(x):
    if x < 0 :
        res = round(x*(-1),15)
    else:
        res = round(x,15)
    return res

def log(x):
    res = math.log10(x)
    return res

def ln(x):
    res = math.log(x)
    return res