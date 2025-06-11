import tkinter as tk
import random

# 游戏设置
WIDTH = 600
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (0, 0)  # 初始方向
        self.growing = False

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # 碰撞检测（边界）
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            return False

        # 碰撞检测（自身）
        if new_head in self.body:
            return False

        self.body.insert(0, new_head)
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False
        return True

    def grow(self):
        self.growing = True

class Food:
    def __init__(self, snake):
        self.position = self.generate_position(snake)

    def generate_position(self, snake):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake.body:
                return (x, y)

    def draw(self, canvas):
        x, y = self.position
        canvas.create_rectangle(x*GRID_SIZE, y*GRID_SIZE,
                                (x+1)*GRID_SIZE, (y+1)*GRID_SIZE,
                                fill="red")

def game_loop():
    snake.move()
    if snake.body[0] == food.position:
        snake.grow()
        food.position = food.generate_position(snake)

    canvas.delete("all")
    # 绘制蛇
    for segment in snake.body:
        x, y = segment
        canvas.create_rectangle(x*GRID_SIZE, y*GRID_SIZE,
                                (x+1)*GRID_SIZE, (y+1)*GRID_SIZE,
                                fill="green")
    # 绘制食物
    food.draw(canvas)
    root.after(100, game_loop)

def change_direction(event):
    dx, dy = 0, 0
    if event.keysym == "Up":
        dx, dy = 0, -1
    elif event.keysym == "Down":
        dx, dy = 0, 1
    elif event.keysym == "Left":
        dx, dy = -1, 0
    elif event.keysym == "Right":
        dx, dy = 1, 0
    # 防止反向移动
    if (dx, dy) != (-snake.direction[0], -snake.direction[1]):
        snake.direction = (dx, dy)

root = tk.Tk()
root.title("贪吃蛇")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
root.bind("<KeyPress>", change_direction)

snake = Snake()
food = Food(snake)
game_loop()
root.mainloop()
'''

### 如何运行：
1. 将代码保存为 `snake.py`
2. 在 VSCode 中打开文件
3. 点击右上角运行按钮（或使用快捷键 `Ctrl + F5`）

### 功能说明：
- 使用方向键控制蛇的移动
- 吃到食物后蛇会变长
- 碰到边界或自身会结束游戏
- 游戏速度可通过 `root.after(100, ...)` 调整（数值越小速度越快）

### 说明：
- 游戏区域为 600x600 像素，每个格子为 20x20 像素
- 蛇的初始位置在屏幕中央
- 食物会随机生成在空白区域

这个实现是基础版本，你可以在此基础上扩展更多功能（如得分系统、暂停功能等）。'''