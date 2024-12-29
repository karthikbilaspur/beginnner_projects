class NeighborDetector:
    def detect(self, cell, grid):
        neighbors = self.count_neighbors(cell, grid)
        if cell.state and (neighbors < 2 or neighbors > 3):
            return False
        elif not cell.state and neighbors == 3:
            return True
        return cell.state

    def count_neighbors(self, cell, grid):
        count = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                neighbor_x = cell.x + x
                neighbor_y = cell.y + y
                if neighbor_x >= 0 and neighbor_x < grid.width and neighbor_y >= 0 and neighbor_y < grid.height:
                    count += grid.cells[neighbor_x][neighbor_y].state
        return count