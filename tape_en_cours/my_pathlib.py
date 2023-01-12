class Path:
    def __init__(self):
        self.paths = []

    def __str__(self):
        return self.join_path()

    def __truediv__(self, other: str):
        return self


if __name__ == "__main__":
    p = Path() / "etc" / "nginx"
