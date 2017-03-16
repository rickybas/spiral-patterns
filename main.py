import pygame
from decimal import Decimal


class Base:
    spiral_type = "prime"
    draw_numbers = False
    num_squares = 40000
    num_box_width = 2
    num_box_height = 2
    multiple = 2

    def get_center(self):
        return self.display_width / 2, self.display_height / 2

    def is_prime(self, a):
        return all(a % i for i in xrange(2, a))

    def is_multiple(self, a, mul):
        return a % mul == 0

    def draw_num_box(self, x, y, num):
        if self.spiral_type == "prime":
            mark = self.is_prime(num)
        else:
            mark =self.is_multiple(num, Decimal(str(self.multiple)))

        pygame.draw.rect(self.game_display, self.black if mark else self.white,
                         (x, y, self.num_box_width, self.num_box_height))
        if self.draw_numbers:
            self.game_display.blit(self.font.render(str(num), True, self.white if mark else self.black),
                                   (x + self.num_box_width / 4, y + self.num_box_height / 4))

    def draw_spiral(self):
        center = self.get_center()

        self.game_display.fill(self.white)

        directions = ["right", "up", "left", "down"]
        dir_num = 0

        cur_pos = (center[0] - self.num_box_width / 2, center[1] - self.num_box_height / 2)

        rep_dir_num = 1  # number of times to repeat in that direction
        num_reps = 1  # number of reps in direction
        rep = 0  # every 2 reps in num of direction steps

        num = 1
        while num != self.num_squares + 1:
            direction = directions[dir_num]

            self.draw_num_box(cur_pos[0], cur_pos[1], num)

            # print direction
            if direction == "right":
                x_change = self.num_box_width + self.num_box_width / 4
                y_change = 0
            elif direction == "up":
                x_change = 0
                y_change = -(self.num_box_height + self.num_box_height / 4)
            elif direction == "left":
                x_change = -(self.num_box_width + self.num_box_width / 4)
                y_change = 0
            else:  # down
                x_change = 0
                y_change = self.num_box_height + self.num_box_height / 4

            cur_pos = (cur_pos[0] + x_change, cur_pos[1] + y_change)

            print str(int(num * 100 / self.num_squares)) + "%"

            if num_reps == rep_dir_num:
                if rep == 1:
                    rep_dir_num += 1
                    rep = 0
                else:
                    rep += 1
                num_reps = 1
                # increment direction
                if dir_num == 3:
                    dir_num = 0
                else:
                    dir_num += 1

            else:
                num_reps += 1
            num += 1

        pygame.display.update()

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            self.clock.tick(120)

    def __init__(self):
        while True:
            prime_or_mul = raw_input("(1) Display prime spiral or \n(2) Display multiple spiral\n")
            if prime_or_mul == "1":
                self.spiral_type = "prime"
                break
            elif prime_or_mul == "2":
                self.spiral_type = "mul"
                while True:
                    try:
                        self.multiple = float(input("Enter multiple for the spiral: "))
                        break
                    except NameError:
                        pass
                break

        self.display_width = 600 + self.num_box_width
        self.display_height = 600 + self.num_box_height

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        self.font = pygame.font.SysFont('Arial', self.num_box_width / 3)

        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("Spirals")
        self.clock = pygame.time.Clock()

        self.draw_spiral()
        self.game_loop()

        pygame.quit()
        quit()


if __name__ == "__main__":
    pygame.init()
    Base()
