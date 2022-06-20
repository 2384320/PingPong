import pygame
import random
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
BALL_SIZE = 25

class Ball:
    ''' 공을 표현하는 클래스 '''
    def __init__(self):
        # 공의 중심 좌표를 임의로 지정
        self.x = 400
        self.y = 200

        # 다음 이동 방향을 설정
        self.change_x = 0
        while self.change_x == 0 or self.change_y == 0:
            self.change_x = 4
            self.change_y = 4

        # 공의 색상을 지정
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        self.color = (r, g, b)

class Bar:
    def __init__(self):
        self.x = 350
        self.y = 720
        self.width = 100
        self.height = 10
        self.color = WHITE
        self.move = 0

        self.change_x = 0
    
# 메인 프로그램
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pygame.display.set_caption("공의 자동 이동(스페이스바를 누르면 공이 더 생깁니다.)")
clock = pygame.time.Clock()

# 여러 볼의 갖는 리스트에 첫 볼을 저장
lstball = []
lstball.append(Ball())
lstbar = []
lstbar.append(Bar())

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            #스페이스 바를 누르면 새로운 공이 나오도록
            if event.key == pygame.K_SPACE:
                lstball.append(Ball())
                # reset()
            if event.key == pygame.K_LEFT:
                bar.change_x = -4
            elif event.key == pygame.K_RIGHT:
                bar.change_x = 4

    for ball in lstball:
        # 볼의 중심 좌표를 이동
        ball.x += ball.change_x
        ball.y += ball.change_y

        # 윈도 벽에 맞고 바운싱
        # x 좌표가 위 이래를 벗어나면
        if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
            ball.change_x *= -1 # 다음 이동좌표의 증가 값을 부호 변경
        # y 좌표가 위 이래를 벗어나면
        if ball.y < BALL_SIZE:
            ball.change_y *= -1 # 다음 이동좌표의 증가 값을 부호 변경
        # 바닥에 떨어진 공
        for bar in lstbar:
            if ball.y > SCREEN_WIDTH - BALL_SIZE:
                ball.change_x = 0
                ball.change_y = 0
                bar.change_x = 0
 
    for bar in lstbar:
        # 막대 이동
        bar.x += bar.change_x
        # 윈도 벽과 막대
        if bar.x > SCREEN_WIDTH - bar.width or bar.x < 0:
            bar.change_x *= -1 # 다음 이동좌표의 증가 값을 부호 변경

    # 막대와 공
    for ball in lstball:
        for bar in lstbar:
            if ball.y + BALL_SIZE > bar.y:
                if ball.x - BALL_SIZE < bar.x + bar.width and ball.x + BALL_SIZE > bar.x:
                    ball.change_y *= -1

    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [0, 750], [800, 750], 5) # 라인 설정

    # 모든 볼을 그리기
    for ball in lstball:
        pygame.draw.circle(screen, ball.color, [ball.x, ball.y], BALL_SIZE)

    for bar in lstbar:
        pygame.draw.rect(screen, bar.color, (bar.x, bar.y, bar.width, bar.height))
    
    # 초당 60 프레임으로 그리기
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
