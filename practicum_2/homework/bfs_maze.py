import queue
from time import perf_counter


class Maze:
    def __init__(self, list_view: list[list[str]]) -> None:
        self.list_view = list_view
        self.start_j = None
        for j, sym in enumerate(self.list_view[0]):
            if sym == "O":
                self.start_j = j
    @classmethod
    def from_file(cls, filename):
        list_view = []
        with open(filename, "r") as f:
            for l in f.readlines():
                list_view.append(list(l.strip()))
        obj = cls(list_view)
        return obj
    def print(self, path="") -> None:
        i = 0
        print()


def solve(maze: Maze) -> None:
    path = ""
    cord_i_j = (0, maze.start_j)
    q = queue.Queue()
    q.put((path, cord_i_j))
    Front = set()
    Current = set()
    Back = set()
    len_0 = len(maze.list_view)
    len_1 = len(maze.list_view[0])
    while not q.empty():
        n=q.qsize()
        for i in range(n):
            (t_path, t_cord_i_j) = q.get()
            if maze.list_view[t_cord_i_j[0]][t_cord_i_j[1]] == "X":
                path = t_path
                break
            a = (t_cord_i_j[0]+1, t_cord_i_j[1])
            if len_0 > a[0] >= 0 and len_1 > a[1] >= 0 and \
                    (maze.list_view[a[0]][a[1]] != "#") and \
                    (a not in Front) and (a not in Back) and (a not in Current):
                q.put((t_path + 'D', a))
                Front.add(a)
            a = (t_cord_i_j[0] -1, t_cord_i_j[1])
            if len_0 > a[0] >= 0 and len_1 > a[1] >= 0 and \
                    (maze.list_view[a[0]][a[1]] != "#") and \
                    (a not in Front) and (a not in Back) and (a not in Current):
                q.put((t_path + 'U', a))
                Front.add(a)
            a = (t_cord_i_j[0] , t_cord_i_j[1]+1)
            if len_0 > a[0] >= 0 and len_1 > a[1] >= 0 and \
                    (maze.list_view[a[0]][a[1]] != "#") and \
                    (a not in Front) and (a not in Back) and (a not in Current):
                q.put((t_path + 'R', a))
                Front.add(a)
            a = (t_cord_i_j[0] , t_cord_i_j[1]-1)
            if len_0 > a[0] >= 0 and len_1 > a[1] >= 0 and \
                    (maze.list_view[a[0]][a[1]] != "#") and \
                    (a not in Front) and (a not in Back) and (a not in Current):
                q.put((t_path + 'L', a))
                Front.add(a)

        Back = Current.copy()
        Current = Front.copy()
        Front=set()
    print(f"Found: {path}")




if __name__ == "__main__":
    maze = Maze.from_file("maze_2.txt")
    t_start = perf_counter()
    solve(maze)
    t_end = perf_counter()
    print(t_end-t_start)