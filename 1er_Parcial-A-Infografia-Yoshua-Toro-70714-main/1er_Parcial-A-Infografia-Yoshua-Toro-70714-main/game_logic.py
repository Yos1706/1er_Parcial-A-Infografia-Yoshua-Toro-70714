import math
import arcade
from dataclasses import dataclass
from logging import getLogger
from math import sin, cos, sqrt, atan2, radians


logger = getLogger(__name__)


@dataclass
class ImpulseVector:
    angle: float
    impulse: float


@dataclass
class Point2D:
    x: float = 0
    y: float = 0


def get_angle_radians(point_a: Point2D, point_b: Point2D) -> float:
    R = 6730
    rad1 = radians(point_a[0])
    lad1 = radians(point_a[1])
    rad2 = radians(point_b[0])
    lad2 = radians(point_b[1])

    dlad = lad2 - lad1
    drad = rad1 - rad2

    a = R (3.1416/180)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    angle = c / a
    return math.atan2(dlad,drad,angle) 



def get_distance(point_a: Point2D, point_b: Point2D) -> float:
    R = 6730
    lat1 = radians(point_a[0])
    lon1 = radians(point_a[1])
    lat2 = radians(point_b[0])
    lon2 = radians(point_b[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon /2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance


def get_impulse_vector(start_point: Point2D, end_point: Point2D,point_a,point_b) -> ImpulseVector:
    R = 6730
    start_point = point_a
    end_point = point_b
    rad1 = radians(point_a[0])
    lad1 = radians(point_a[1])
    rad2 = radians(point_b[0])
    lad2 = radians(point_b[1])

    dlad = lad2 - lad1
    drad = rad1 - rad2
    lat1 = radians(point_a[0])
    lon1 = radians(point_a[1])
    lat2 = radians(point_b[0])
    lon2 = radians(point_b[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    return ImpulseVector(dlad,drad,dlon,dlat)
    
