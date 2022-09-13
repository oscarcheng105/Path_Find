from queue import PriorityQueue
from utils import reconstruct_path
import pygame

def dijkstra(draw, grid, start, end):
    count = 0
    pq = PriorityQueue()
    pq.put((count, start))
    pq_hash = {start}
    came_from = {}
    score = {node: float("inf") for row in grid for node in row}
    score[start] = 0

    while not pq.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
        current = pq.get()[1]
        pq_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, start, end, draw)
            return True
        
        for neighbor in current.neighbors:
            temp_score = score[current] + 1
            if(temp_score < score[neighbor]):
                came_from[neighbor] = current
                score[neighbor] = temp_score
                if neighbor not in pq_hash:
                    count += 1
                    pq.put((count, neighbor))
                    pq_hash.add(neighbor)
                    if neighbor != end:
                        neighbor.make_unvisited()
        
        draw()
        if current != start:
            current.make_visited()
    
    return False
