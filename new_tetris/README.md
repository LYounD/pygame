![](https://github.com/gusalsdmlwlq/SE-2017/blob/master/Project2/s1.png)
![](https://github.com/gusalsdmlwlq/SE-2017/blob/master/Project2/s2.png)
![](https://github.com/gusalsdmlwlq/SE-2017/blob/master/Project2/s3.png)
![](https://github.com/gusalsdmlwlq/SE-2017/blob/master/Project2/s4.png)
![](https://github.com/gusalsdmlwlq/SE-2017/blob/master/Project2/s5.png)
![](https://github.com/gusalsdmlwlq/SE-2017/blob/master/Project2/s6.png)
![](https://github.com/gusalsdmlwlq/SE-2017/blob/master/Project2/s7.png)
![](https://github.com/gusalsdmlwlq/SE-2017/blob/master/Project2/s8.png)
![](https://github.com/gusalsdmlwlq/SE-2017/blob/master/Project2/s9.png)
![](https://github.com/gusalsdmlwlq/SE-2017/blob/master/Project2/s10.png)
# 게임 설명
* 기본적인 테트리스
* 7종류의 블럭
* 좌.우 방향키로 블럭을 이동
* 위 방향키로 블럭을 회전
* 아래 방향키, 스페이스로 블럭을 가속
* 한 줄을 터뜨리면 score +100
* score가 1000 올라갈 때 마다 stage up
* 맵은 가로 15칸 세로 20칸

# 기능 설명
* 테트리스의 기본 기능 수행
* 아래 방향키, 스페이스로 블럭을 가속시킬 수 있음
* 15*20 배열로 테트리스의 맵을 만듬
* 각 블럭은 4*4 배열로 만듬
* 블럭은 7 종류이며 각각 다른 색깔을 가짐
* 블럭이 다른 블럭이나 벽에 닿으면 밀려나는 방식을 사용
* 텍스트로 score와 stage를 표시
* 일정 score마다 stage가 올라감
* 다음 블럭 표시
* 게임 시작 전 게임 설명 표시
* stage가 올라갈 때 마다 특수 효과들 추가
* stage 2,4,6 달성시 이미지를 띄워 흥미 유발
* stage 3 달성시 이미지를 띄우고 블럭의 내려오는 속도 증가
* stage 5 달성시 이미지를 띄우고 랜덤으로 블럭들을 제거
* 1000점을 달성하지 못하고 블럭이 천장에 닿아 게임이 끝날 경우 자동으로 게임이 다시 시작됨
* 게임을 종료하면 특수 효과를 띄우고 '갓 겜' <히어로즈 오브 더 스톰> 홈페이지를 띄움
* Battlenet 앱이 기본 경로에 설치 되어 있으면 홈페이지를 띄운 후 Battlenet 앱을 강제로 실행시킴
* <히어로즈 오브 더 스톰>이 설치 되어 있으면 바로 실행 가능
* bgm 추가
* stage 올라갈 때 효과음 추가
* 블럭이 터질 때 이펙트와 효과음 추가

# 코드 설명
Main.py, game.py, blocks.py 3개의 파일로 나눔.

colors = {1: (255, 0, 0), 2: (0, 255, 0), 3: (0, 0, 255), 4: (255, 255, 0),
    5: (0, 255, 255), 6: (255, 0, 255), 7: (255,255,255)}

블록들의 색깔을 변수로 지정해둠.

    while tetris.game: ##메인 루프 / 화면 표시
        newTick = pygame.time.get_ticks()
        diff = newTick - lastTick
        lastTick = newTick
        update(diff)

        screen.fill((0, 0, 0))

        drawBlock(screen, rect, tetris.getGameMap(), (0, 0))
        drawBlock(screen, rect, tetris.getBlock().getRotatedShape(),tetris.getPosition())
        drawBlock(screen, rect, tetris.getnextBlock().getnextblock(), (25,3))
        pygame.draw.rect(screen, (50, 50, 50), (375, 0, 150, 500))
        screen.blit(text_nextblock, textrect_nextblock)
        screen.blit(text_stage,textrect_stage)
        screen.blit(text_score, textrect_score)
        text_stage_ = font2.render(str(tetris.stage), True, (200, 0, 0))
        screen.blit(text_stage_, textrect_stage_)
        text_score_ = font2.render(str(tetris.score), True, (100, 100, 100))
        screen.blit(text_score_, textrect_score_)
def drawBlock(screen, rect, shape, position): #블록 그리기
    for y in range(len(shape)):
        for x in range(len(shape[0])):
            if not shape[y][x] == 0:
                rect.fill(colors[shape[y][x]])
                screen.blit(rect, (25 * (x + position[0]), 25 * (y + position[1])))
main에서 while문을 사용
Screen.fill로 screen을 모두 비운 후
Screen.blit으로 screen변수에 블록들과 텍스트를 그리고
Pygame.display.flip으로 screen을 사용자의 게임 창에 표시함.

def __initGameMap(self):
    gameMap = []
    for y in range(20):
        gameMap.append([])
        for x in range(15):
            gameMap[y].append(0)
    return gameMap

테트리스 맵을 20*15의 배열로 만듬.(가로 15 세로 20)

class Block1(Block):
    
    def __init__(self):
        Block.__init__(self, [[0,0,0,0],
                              [0,1,1,0],
                              [1,1,0,0],
                              [0,0,0,0]], 1)
class Block7(Block):
    def __init__(self):
        Block.__init__(self, [[0, 0, 0, 0],
                              [0, 7, 0, 0],
                              [7, 7, 7, 0],
                              [0, 0, 0, 0]], 7)

블록 종류별로 class를 만들고 4*4 배열로 블록의 모양을 만듬.
0 : 검은색(빈칸) 
1~7 : 블록 종류별 색깔

def __addBlockToGameMap(self):
    for y in range(self._currentBlock.getHeight()):
        for x in range(self._currentBlock.getWidth()):
            value = self._currentBlock.getRotatedShape()[y][x]
            if value is 0:
                continue
            y2 = self._position[1] + y
            x2 = self._position[0] + x
            self._gameMap[y2][x2] = value

블록의 4*4 배열을 모두 돌며 테트리스 맵 배열의 색을 바꿔 블록을 추가함.

def __doesBlockCollide(self):
    for y in range(self._currentBlock.getHeight()):
        for x in range(self._currentBlock.getWidth()):
            shapeValue = self._currentBlock.getRotatedShape()[y][x]
            y2 = self._position[1] + y
            x2 = self._position[0] + x
            if(x2<=-1 or x2>=15 or y2>=20):
                mapValue = 0
            else :
                mapValue = self._gameMap[y2][x2]
            if shapeValue and mapValue:
                return True
    return False
def __doesBlockCollidewithwall(self):
    for y in range(self._currentBlock.getHeight()):
        for x in range(self._currentBlock.getWidth()):
            shapeValue = self._currentBlock.getRotatedShape()[y][x]
            y2 = self._position[1] + y
            x2 = self._position[0] + x
            if shapeValue and (x2<=-1 or x2>=15 or y2>=20):
                return True
    return False

블록이 다른 블록이나 벽과 닿았는지 검사하는 함수를 만듬.


def lineclear(self,line):
    for x in range(0,15):
        self._gameMap[line][x] = 0
    for y in range(0,line):
        for z in range(0,15):
            self._gameMap[line-y][z] = self._gameMap[line-y-1][z]
def linesclear(self):
    for y in range(0,20):
        x = 0
        while x<15:
            if self._gameMap[y][x] == 0:
                break
            x += 1
        if x == 15:
            self.fire_state[y] = 1
            self.lineclear(y)
            self.score += 100

한 줄이 꽉 찼는지 검사하고 꽉 찬 줄을 0으로 바꿔 블록을 제거하는 함수를 만듬.

def rotate(self):
    self._currentBlock.rotateCounterclockwise()
    xmove = 0
    ymove = 0
    for y in range(self._currentBlock.getHeight()):
        for x in range(self._currentBlock.getWidth()):
            shapeValue = self._currentBlock.getRotatedShape()[y][x]
            y2 = self._position[1] + y
            x2 = self._position[0] + x
            if shapeValue and x2<=-1:
                xmove += 1
            if shapeValue and x2>=15:
                xmove -= 1
            if shapeValue and y2>=20:
                ymove -= 1
    self._position[0] += xmove
    self._position[1] += ymove

블록을 회전시키고 벽에 닿으면 블록을 밀어내는 함수를 만듬.

def getRotatedShape(self):
    rotatedShape = self._shape
    for n in range(int(self._angle / 90)):
        rotatedShape = list(zip(*rotatedShape))[::-1]
    return rotatedShape

회전이 적용된 블록 모양을 리턴해주는 함수를 만듬.

for x in range(len(tetris.fire_state)):
    makefire = drawfire(screen,x)
    next(makefire)
    if(tetris.fire_state[x]==1):
        makefire.send(fire_1)
    elif(tetris.fire_state[x]==2):
        makefire.send(fire_2)
    elif (tetris.fire_state[x] == 3):
        makefire.send(fire_3)
    elif (tetris.fire_state[x] == 4):
        makefire.send(fire_4)
    elif (tetris.fire_state[x] == 5):
        makefire.send(fire_5)
    elif (tetris.fire_state[x] == 6):
        makefire.send(fire_6)
pygame.display.flip()

def drawfire(screen,line):
    while(True):
        state = yield
        screen.blit(state,(0,line*25))
        tetris.fire_state[line] += 1
        if(tetris.fire_state[line] == 7):
            tetris.fire_state[line] = 0
        pygame.mixer.Sound.play(clearsound)
        time.sleep(0.02)

블록이 지워질 때 이펙트를 추가하는 함수를 만들고 코루틴을 사용하여 이펙트가 표시되는 동안에도 게임이 멈추지 않게 만듬.

if(tetris.score < 1000):
    os.startfile('main.py')

score 1000을 달성하지 못하고 게임에서 패배하면 게임을 다시 실행시킴.

if(tetris.stageup):
    pygame.mixer.music.stop()
    tetris.stageup = False
    if(tetris.stage == 3):
        pygame.mixer.Sound.play(speedup_)
        screen.fill((0, 0, 0))
        screen.blit(speedup, (0, 0))
        pygame.display.flip()
    elif(tetris.stage == 2):
        pygame.mixer.Sound.play(stageup_)
        screen.fill((0, 0, 0))
        screen.blit(stageup2,(0,0))
        pygame.display.flip()
    elif (tetris.stage == 5):
        pygame.mixer.Sound.play(stageup4)
        screen.fill((0, 0, 0))
        screen.blit(stageup4_, (0, 0))
        pygame.display.flip()
        justice = 50
    elif (tetris.stage == 4):
        pygame.mixer.Sound.play(stageup_)
        screen.fill((0, 0, 0))
        screen.blit(stageup3, (0, 0))
        pygame.display.flip()
    else:
        pygame.mixer.Sound.play(stageup_)
        screen.fill((0, 0, 0))
        screen.blit(stageup, (0, 0))
        pygame.display.flip()
    time.sleep(2)
    pygame.mixer.music.play(-1, 0.0)

stage가 올라가면 특수 효과를 만드는 기능.

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('bgm2.mp3')
        pygame.mixer.music.play()
        screen.fill((0,0,0))
        screen.blit(jigsaw_1,(500,400))
        pygame.display.flip()
        time.sleep(1)
        screen.fill((0, 0, 0))
        screen.blit(jigsaw_2,(100,100))
        pygame.display.flip()
        time.sleep(1)
        screen.fill((0, 0, 0))
        screen.blit(jigsaw_3,(400,100))
        pygame.display.flip()
        time.sleep(1)
        screen.fill((0, 0, 0))
        screen.blit(jigsaw_4,(100,300))
        pygame.display.flip()
        time.sleep(1)
        screen.fill((0, 0, 0))
        screen.blit(jigsaw_5,(300,200))
        pygame.display.flip()
        time.sleep(1)
        screen.fill((0, 0, 0))
        screen.blit(jigsaw,(0,0))
        pygame.display.flip()
        time.sleep(1)
        screen.fill((0, 0, 0))
        pygame.display.flip()
        time.sleep(1)
        pygame.display.set_caption('★☆★☆★☆☞히어로즈 오브 더 스톰☜☆★☆★☆★ 무료가입 ☞☞http://kr.battle.net/heroes/ko/☜☜')
        pygame.mixer.music.stop()
        pygame.mixer.music.load('storm.mp3')
        pygame.mixer.music.play(1, 0.0)
        accel = 0.01
        for x in range(0, 720):
            screen.fill((0, 0, 100))
            storm = pygame.transform.rotate(storm_, x * accel)
            screen.blit(storm, (400 - storm.get_rect().width / 2, 250 - storm.get_rect().height / 2))
            pygame.display.flip()
            accel += 0.01
        screen.fill((0, 0, 100))
        screen.blit(hots,(0,0))
        pygame.display.flip()
        time.sleep(1)
        webbrowser.open(url)
        if(os.path.exists('C:\Program Files (x86)\Blizzard App\Battle.net Launcher.exe')):
            os.startfile('C:\Program Files (x86)\Blizzard App\Battle.net Launcher.exe')
        sys.exit()

게임을 종료하면 효과음을 재생시키고 이미지를 띄운 후 이미지를 회전시키다가 webbrowser.open으로 ‘히어로즈 오브 더 스톰’ 홈페이지를 띄우고 사용자의 컴퓨터에 Battle.net 앱이 기본 경로에 설치되어 있으면 Battle.net 앱을 실행시킴.

