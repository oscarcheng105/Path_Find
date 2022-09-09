import pygame
from utils import reconstruct_path

def dfs(draw, start, end):
    current = start
    came_from = {}
    stack = list()
    stack.append(current)

    while len(stack) != 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = stack.pop()

        if current == end:
            reconstruct_path(came_from, start, current, draw)
            return True

        for neighbor in current.neighbors:
            if neighbor not in stack and not neighbor.is_visited() and neighbor != start:
                came_from[neighbor] = current
                stack.append(neighbor)
                if neighbor != end:
                    neighbor.make_unvisited()

        draw()

        if current != start:
            current.make_visited()

    return False
