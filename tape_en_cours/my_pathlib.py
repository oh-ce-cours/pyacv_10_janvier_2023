from typing import Optional


class Path:
    def __init__(self, path: Optional["Path"] = None):
        if path is None:
            root = []
        else:
            path: Path
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
        new_path.add_path(other)
        return new_path


if __name__ == "__main__":
    p = Path() / "etc" / "nginx"
    print(p)
