from __future__ import annotations
from math import sqrt, cos, sin


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def get_tuple(self) -> tuple[float, float]:
        return self.x, self.y

    def get_string(self) -> str:
        return f"x: {self.x}, y:  {self.y}"

    def sub(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def add(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def norm(self, vector: 'Vector' = None) -> float:
        if vector is None:
            return sqrt(self.dot_product(other=self))
        else:
            return sqrt(vector.x ** 2 + vector.y ** 2)

    def distance_to(self, other: 'Vector') -> float:
        return self.norm(self.sub(other))

    def dot_product(self, other: 'Vector') -> float:
        return self.x * other.x + self.y * other.y

    # orthographic projection of other on itself
    def ortho_projection(self, other: 'Vector') -> 'Vector':
        return self.multiply(self.dot_product(other) / (self.norm() ** 2))

    def multiply(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)

    def ortho_vector(self) -> 'Vector':
        return Vector(self.y, self.multiply(-1).x)

    def get_cos_bet_vectors(self, other: 'Vector') -> float:
        cosine = self.dot_product(other) / (self.norm() * other.norm())
        return cosine

    def rotate(self, rotation: float) -> 'Vector':
        rot_matrix: tuple[Vector, Vector] = Vector(cos(rotation), sin(rotation)), Vector(-1 * sin(rotation),
                                                                                         cos(rotation))
        new_vector: Vector = Vector(rot_matrix[0].dot_product(self), rot_matrix[1].dot_product(self))
        return new_vector

    def normalize(self) -> 'Vector':
        return self.multiply(1 / self.norm())

    def reflect(self, mirror: 'Vector'):
        v = mirror.multiply(self.dot_product(mirror)).multiply(-2)
        refl: Vector = self.add(v)
        return refl
