import pygame
import random
import blocks
import sys
import time

class Game:

    WIDTH = 15
    HEIGHT = 20
    speed = 1
    stagespeed = 1
    stage = 1
    stages = [0,100,200,300,400,600,800]
    score = 0
    stageup =False
    issapce = False
    def __init__(self):
        self._gameMap = self.__initGameMap()
        self._currentBlock = self.__makeRandomBlock()
        self.nextblock = self.__makeRandomBlock()
        self._position = [6, -1]
        self._timeCounter = 0
        self.fire_state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.game = True
    def __initGameMap(self):
        gameMap = []
        for y in range(20):
            gameMap.append([])
            for x in range(15):
                gameMap[y].append(0)
        return gameMap

    def __makeRandomBlock(self): #블럭 랜덤으로 지정
        time.sleep(0.5)
        rand = random.randint(1, 7)
        if rand == 1:
            return blocks.Block1()
        elif rand == 2:
            return blocks.Block2()
        elif rand == 3:
            return blocks.Block3()
        elif rand == 4:
            return blocks.Block4()
        elif rand == 5:
            return blocks.Block5()
        elif rand == 6:
            return blocks.Block6()
        elif rand == 7:
            return blocks.Block7()

    def __addBlockToGameMap(self): #화면에 블럭 표시
        for y in range(self._currentBlock.getHeight()):
            for x in range(self._currentBlock.getWidth()):
                value = self._currentBlock.getRotatedShape()[y][x]
                if value is 0:
                    continue
                y2 = self._position[1] + y
                x2 = self._position[0] + x
                self._gameMap[y2][x2] = value

    def __doesBlockCollide(self): #블럭에 닿은 경우
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
    def __doesBlockCollidewithwall(self): #벽에 닿은 경우
        for y in range(self._currentBlock.getHeight()):
            for x in range(self._currentBlock.getWidth()):
                shapeValue = self._currentBlock.getRotatedShape()[y][x]
                y2 = self._position[1] + y
                x2 = self._position[0] + x
                if shapeValue and (x2<=-1 or x2>=15 or y2>=20):
                    return True
        return False
    def lineclear(self,line): #꽉 찬 라인 비우기
        for x in range(0,15):
            self._gameMap[line][x] = 0
        for y in range(0,line):
            for z in range(0,15):
                self._gameMap[line-y][z] = self._gameMap[line-y-1][z]
    def linesclear(self): #한 줄이 꽉 찼는지 체크
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
        for k in range(1,7): #일정 점수를 얻으면 스테이지가 올라감
            if(self.score >= self.stages[k] and self.stages[k] != -1):
                self.stage = k+1
                self.stages[k] = -1
                self.stageup = True
                if(k == 2):
                    self.stagespeed += 1
    def update(self, time):
        self._timeCounter += time
        if self.issapce == False and self._timeCounter < 500/self.speed:  # Only move down block every 1 second
            return
        self._timeCounter = 0

        self._position[1] += 1  # Move down block

        # If the block has reach the bottom or collides with a solid tile
        if self.__doesBlockCollidewithwall() or self.__doesBlockCollide(): #블럭이나 벽에 닿으면 멈추고 새로운 블럭을 만듬
            while self.__doesBlockCollidewithwall() or self.__doesBlockCollide(): #블럭끼리 겹치면 안 겹칠 때 까지 위로 밀어냄
                self._position[1] -= 1
                if self._position[1] <= -1:
                    self.game = False
                    break
                    #sys.exit()
            self.__addBlockToGameMap()
            self._position = [6, -1]
            self._currentBlock = self.nextblock
            self.nextblock = self.__makeRandomBlock()
        self.linesclear()

    def rotate(self):
        self._currentBlock.rotateCounterclockwise()
        xmove = 0
        ymove = 0
        for y in range(self._currentBlock.getHeight()): #회전했을 때 벽에 닿으면 밀어냄
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
    def moveLeft(self):
        if True:#self._position[0]:
            self._position[0] -= 1
            if self.__doesBlockCollidewithwall() or self.__doesBlockCollide():
                self._position[0] += 1

    def moveRight(self):
        if True:#self._position[0] + self._currentBlock.getWidth() < Game.WIDTH:
            self._position[0] += 1
            if self.__doesBlockCollidewithwall() or self.__doesBlockCollide():
                self._position[0] -= 1

    def getPosition(self):
        return self._position

    def getGameMap(self):
        return self._gameMap

    def getBlock(self):
        return self._currentBlock
    def getnextBlock(self):
        return self.nextblock
