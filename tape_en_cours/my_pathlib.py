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
        return self.get_separator() + self.get_separator().join(self.paths)

    @abc.abstractmethod
    def get_separator(self) -> str:
        pass

    def add_path(self, other_path: str):
        other_paths = other_path.split(self.get_separator())
        self.paths.extend(other_paths)
        return self

    def __str__(self):
        return self.join_path()

    def __truediv__(self, other: str):
        PathClass = self.__class__
        new_path = PathClass(self)
        return new_path.add_path(other)

    @classmethod
    def create(cls, *args):
        platform = "windows"
        if platform == "linux":
            return UnixPath
        if platform == "windows":
            return WindowsPath


class UnixPath(AbstractPath):
    def get_separator(self) -> str:
        return "/"


class WindowsPath(AbstractPath):
    def get_separator(self) -> str:
        return "\\"

    def join_path(self):
        return f"C:{self.get_separator()}" + self.get_separator().join(self.paths)


if __name__ == "__main__":
    p = AbstractPath.create()
    p1 = p / "etc"
    p2 = p1 / "nginx"
    print(id(p1), id(p2))
    print(p2)

    p = UnixPath()
    print(p.add_path("etc").add_path("nginx"))

    pw = WindowsPath()
    pw1 = pw / "etc"
    pw2 = pw1 / "nginx"
    print(id(pw1), id(pw2))
    print(pw2)

    pw = WindowsPath()
    print(pw.add_path("etc").add_path("nginx"))

import pathlib
