import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
BALL_SIZE = 25
OVER_TEXT = 'GAME OVER'
RESET_TEXT = 'Press the space bar'
REPLAY_TEXT = 'Then you can continue'
GUIDE_TEXT = 'Press the LEFT and RIGHT key'
RESULT_TEXT = 'Your point is '
font = pygame.font.SysFont('Consolas', 30)
font0 = pygame.font.SysFont('Consolas', 100)
P = 0

class Ball:
    ''' 공을 표현하는 클래스 '''
    def __init__(self):
        # 공의 중심 좌표를 임의로 지정
        self.x = 400
        self.y = 200

        # 다음 이동 방향을 설정
        self.change_x = 0
        while self.change_x == 0 or self.change_y == 0:
            self.change_x = random.randint(0,1)
            self.change_y = random.randint(0,1)
            if self.change_x == 0:
                self.change_x = -4
            elif self.change_x == 1:
                self.change_x = 4
            
            if self.change_y == 0:
                self.change_y = -4
            elif self.change_y == 1:
                self.change_y = 4

        # 공의 색상을 지정
        r = 255
        g = 255
        b = 255
        self.color = (r, g, b)

class Bar:
    def __init__(self):
        self.x = 350
        self.y = 720
        self.width = 100
        self.height = 10
        self.color = WHITE

        self.change_x = 0

def show_text():
    screen.blit(text1, [100, 300])
    screen.blit(text2, [100, 340])
    screen.blit(text3, [100, 380])
    screen.blit(text6, [100, 260])

def count_point(count):
    point = str(count)
    return point

# 메인 프로그램
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pygame.display.set_caption("PING-PONG")
clock = pygame.time.Clock()

# 여러 볼의 갖는 리스트에 첫 볼을 저장
lstball = []
lstball.append(Ball())
lstbar = []
lstbar.append(Bar())

text1 = font.render(OVER_TEXT, True, WHITE)
text2 = font.render(RESET_TEXT, True, WHITE)
text3 = font.render(REPLAY_TEXT, True, WHITE)
text4 = font.render(GUIDE_TEXT, True, WHITE)
text5 = font0.render('0', True, WHITE)

isTextView = False
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            #스페이스 바를 누르면 새로운 공이 나오도록
            if event.key == pygame.K_SPACE:
                P = 0
                POINT = count_point(P)
                text5 = font0.render(POINT, True, WHITE)
                lstball.pop()
                lstball.append(Ball())
                lstbar.pop()
                lstbar.append(Bar())
                isTextView = not isTextView;
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
                POINT = count_point(P)
                text6 = font.render(RESULT_TEXT + POINT, True, WHITE)
                
                bar.change_x = 0
                ball.change_x = 0
                ball.change_y = 0
                isTextView = True
 
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
                    P += 1
                    POINT = count_point(P)
                    text5 = font0.render(POINT, True, WHITE)
                    
                    ball.change_y *= -1.2
                    ball.change_x *= 1.2


    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [0, 750], [800, 750], 5) # 라인 설정

    # 모든 볼을 그리기
    for ball in lstball:
        pygame.draw.circle(screen, ball.color, [ball.x, ball.y], BALL_SIZE)

    for bar in lstbar:
        pygame.draw.rect(screen, bar.color, (bar.x, bar.y, bar.width, bar.height))
    
    screen.blit(text4, [100, 180])
    screen.blit(text5, [385, 50])
    if isTextView:
        show_text()

    # 초당 60 프레임으로 그리기
    clock.tick(60)
    pygame.display.update()

pygame.quit()
