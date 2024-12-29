import matplotlib.animation

class Visualizer:
    def animate_solution(self, board, solution):
        fig, ax = plt.subplots()
        def animate(i):
            board.apply_solution(solution[:i+1])
            ax.clear()
            ax.imshow(board.grid, cmap='binary')
        ani = matplotlib.animation.FuncAnimation(fig, animate, frames=len(solution), interval=100)
        plt.show()