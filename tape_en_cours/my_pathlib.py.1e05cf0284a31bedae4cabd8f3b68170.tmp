class Path:
    def __init__(self):
        self.paths = []

    def __str__(self):
        return self.join_path()

    def join_path(self):
        return "/" + "/".join(self.paths)

    def add_path(self, other_path: str):
        other_paths = other_path.split("/")
        self.paths.extend(other_paths)

    def __truediv__(self, other: str):
        self.add_path(other)
        return self


if __name__ == "__main__":
    p = Path() / "etc" / "nginx"
    print(p)
