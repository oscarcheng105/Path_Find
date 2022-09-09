import queue
import pygame
from utils import reconstruct_path

def bfs(draw, start, end):
    current = start
    came_from = {}
    que = []
    que.append(current)

    while len(que) != 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = que.pop(0)

        if current == end:
            reconstruct_path(came_from, start, current, draw)
            return True

        for neighbor in current.neighbors:
            if neighbor not in que and not neighbor.is_visited() and neighbor != start:
                came_from[neighbor] = current
                que.append(neighbor)
                if neighbor != end:
                    neighbor.make_unvisited()

        draw()

        if current != start:
            current.make_visited()

    return False