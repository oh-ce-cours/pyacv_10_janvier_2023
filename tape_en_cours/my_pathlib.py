from typing import Optional
import abc


class AbstractPath(abc.ABC):
    def __init__(self, path: Optional["Path"] = None):
        if path is None:
            root = []
        else:
            root = path.paths
        self.paths = root

    def join_path(self):
        return "/" + "/".join(self.paths)

    def add_path(self, other_path: str):
        other_paths = other_path.split("/")
        self.paths.extend(other_paths)
        return self

    def __str__(self):
        return self.join_path()

    def __truediv__(self, other: str):
        new_path = Path(self)
        return new_path.add_path(other)


if __name__ == "__main__":
    p = Path()
    p1 = p / "etc"
    p2 = p1 / "nginx"
    print(id(p1), id(p2))
    print(p2)

    p = Path()
    print(p.add_path("etc").add_path("nginx"))
