from utils import *
from a_star import a_star
from dfs import dfs
from bfs import bfs
from dijkstra import dijkstra

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A* Path Finding Algorthm")

def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			node = Node(i, j, gap, rows)
			grid[i].append(node)
	return grid

def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def clean_grid(grid, rows, start, end):
	for i in range(rows):
		for j in range(rows):
			if(grid[i][j] != start and grid[i][j] != end and not grid[i][j].is_barrier()):
				grid[i][j].reset()

def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for node in row:
			node.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()

def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos
	row = y // gap
	col = x // gap

	return row, col

def main(win, width):
	ROWS = 50
	grid = make_grid(ROWS, width)
	algs = ["a_star", "dijkstra", "dfs", "bfs"]
	curr_alg = 0

	start = None
	end = None

	run = True

	while run:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				node = grid[row][col]
				if not start and node != end:
					start = node
					start.make_start()

				elif not end and node != start:
					end = node
					end.make_end()

				elif node != end and node != start:
					node.make_barrier()

			elif pygame.mouse.get_pressed()[2]:
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				node = grid[row][col]
				node.reset()
				if node == start:
					start = None
				elif node == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for node in row:
							node.update_neighbors(grid)
					clean_grid(grid, ROWS, start, end)
					if(algs[curr_alg] == "a_star"):
						a_star(lambda: draw(win, grid, ROWS, width), grid, start, end)
					elif(algs[curr_alg] == "dijkstra"):
						dijkstra(lambda: draw(win, grid, ROWS, width), grid, start, end)
					elif(algs[curr_alg] == "dfs"):
						dfs(lambda: draw(win, grid, ROWS, width), start, end)
					elif(algs[curr_alg] == "bfs"):
						bfs(lambda: draw(win, grid, ROWS, width), start, end)
						
				if event.key == pygame.K_RIGHT:
					curr_alg = (curr_alg + 1)%4
					if(algs[curr_alg] == "a_star"):
						pygame.display.set_caption("A* Path Finding Algorthm")
					elif(algs[curr_alg] == "dijkstra"):
						pygame.display.set_caption("Dijkstra's Path Finding Algorthm")
					elif(algs[curr_alg] == "dfs"):
						pygame.display.set_caption("DFS Path Finding Algorthm")
					elif(algs[curr_alg] == "bfs"):
						pygame.display.set_caption("BFS Path Finding Algorthm")

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)

	pygame.quit()

main(WIN, WIDTH)

