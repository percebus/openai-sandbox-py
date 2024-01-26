from enum import StrEnum


class Algorithms(StrEnum):
    HNSW = "HNSW"  # Faster
    Flat = "FLAT"  # Better


class DistanceMetrics(StrEnum):
    CoSine = "COSINE"
    Euclidean = "EUCLIDEAN"
