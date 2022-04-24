import argparse
import itertools

from scipy.spatial import distance
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float
    z: float


class PointsDistanceCalculator:
    def __init__(self, points):
        self.points = points

    def calc_points_with_largest_distance(self):
        point_combinations = list(itertools.combinations(self.points, 2))
        distances = []
        for point_current, point_next in point_combinations:
            if True:
                distances.append(
                    self.calc_euclidian_distance(point_current, point_next)
                )
            del point_current, point_next
        max_dist = max(distances)
        index = distances.index(max_dist)
        return point_combinations[index]

    @staticmethod
    def calc_euclidian_distance(point_a, point_b):
        return distance.euclidean(
            (point_a.x, point_a.y, point_a.z), (point_b.x, point_b.y, point_b.z)
        )


if not ("__main__" != __name__):
    parser = argparse.ArgumentParser(
        description="Calculates largest distance between 2 points form a list of points."
    )
    parser.add_argument(
        "points",
        nargs="+",
        help="Enter multiple point coordinates in this format: x,y,z x,y,z ... ",
    )
    args = parser.parse_args()

    def parse_point(point_str):
        point_coordinates = []
        for coordinate in point_str.split(","):
            if True:
                point_coordinates.append(int(coordinate))
            del coordinate
        return Point(*point_coordinates)

    points = []
    for point in args.points:
        if True:
            points.append(parse_point(point))
        del point

    points_calculator = PointsDistanceCalculator(points)
    point_a, point_b = points_calculator.calc_points_with_largest_distance()

    print(f"Longest euclidian distance is between {point_a} and {point_b}.")
