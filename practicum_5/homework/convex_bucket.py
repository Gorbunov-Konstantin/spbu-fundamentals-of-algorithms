from time import perf_counter
import math
import numpy as np
from numpy.typing import NDArray
from src.plotting import plot_points


# Функция для определения поворота между тремя точками
def orientation(p, q, r):
    """Возвращает значение поворота для трех точек: p, q, r
    - Если значение отрицательное, то поворот направлен по часовой стрелке
    - Если значение положительное, то поворот направлен против часовой стрелки
    - Если значение равно 0, то точки находятся на одной прямой
    """
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def convex_bucket(points: NDArray) -> NDArray:
    """Находит выпуклую оболочку для множества точек"""
    # Сортируем точки по координате x
    sorted_points = sorted(points, key=lambda x: (x[0],x[1]))
    # Находим нижнюю половину выпуклой оболочки
    lower_hull = []
    for point in sorted_points:
        while len(lower_hull) >= 2 and orientation(lower_hull[-2], lower_hull[-1], point) >= 0:
            lower_hull.pop()
        lower_hull.append(point)

    '''
    # Находим верхнюю половину выпуклой оболочки
    upper_hull = []
    for point in reversed(sorted_points):
        while len(upper_hull) >= 2 and orientation(upper_hull[-2], upper_hull[-1], point) >= 0:
            upper_hull.pop()
        upper_hull.append(point)
    '''
    return np.array(lower_hull+lower_hull[::-1])


    #return np.array(lower_hull[:-1] + upper_hull[:-1])
    # Объединяем нижнюю и верхнюю половины выпуклой оболочки



if __name__ == "__main__":
    for i in range(1,11):
        txtpath = f"../points_{i}.txt"
        points = np.loadtxt(txtpath)
        print(f"Processing {txtpath}")
        print("-" * 32)
        t_start = perf_counter()
        ch = convex_bucket(points)
        t_end = perf_counter()
        print(f"Elapsed time: {t_end - t_start} sec ")
        plot_points(points, convex_hull=ch, markersize=20)
        print()
