from typing import Optional


class Path:
    def __init__(self, path: Optional["Path"] = None):
        if path is None:
            root = []
        else:
            root = path.paths
        self.paths = root

    def __str__(self):
        return self.join_path()

    def join_path(self):
        return "/" + "/".join(self.paths)

    def add_path(self, other_path: str):
        other_paths = other_path.split("/")
        self.paths.extend(other_paths)

    def __truediv__(self, other: str):
        new_path = Path(self)
        self.add_path(other)
        return self


if __name__ == "__main__":
    p1 = Path() / "etc"
    p2 = p1 / "nginx"
    print(id(p1), id(p2))
    print(p2)
