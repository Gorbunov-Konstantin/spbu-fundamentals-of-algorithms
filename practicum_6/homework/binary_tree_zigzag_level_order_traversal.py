from __future__ import annotations
from typing import Any

import yaml

def zigzag_level_order_traversal(list_view: list[int]) -> list[int]:
    start = 0
    end = 1
    direction = 1
    zigzag = []
    l=len(list_view)
    while min(start,end) < l and start != end:
        z=[]

        for i in range(start, end, direction):
            if list_view[i] != None:
                z.append(list_view[i])

        if direction == 1:
            end, start = start * 2, min(end * 2, l-1)
        else:
            end, start = min(start * 2 + 3, l), end * 2 + 3

        direction *= -1
        zigzag.append(z)
    return zigzag


if __name__ == "__main__":
    # Let's solve Binary Tree Zigzag Level Order Traversal problem from leetcode.com:
    # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    # First, implement build_tree() to read a tree from a list format to our class
    # Second, implement BinaryTree.zigzag_traversal() returning the list required by the task
    # Avoid recursive traversal!

    with open(
        "binary_tree_zigzag_level_order_traversal_cases.yaml", "r"
    ) as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        zz_traversal = zigzag_level_order_traversal(c["input"])
        print(c["input"],c['output'],zz_traversal)
        print(f"Case #{i + 1}: {zz_traversal == c['output']}")
