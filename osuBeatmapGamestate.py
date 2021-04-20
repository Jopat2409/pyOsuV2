import glob
import logging
import os
import pygame
import pygame.gfxdraw
import pygame.font
import random
import math

import osuGlobals
import osuBeatmap

#this gamestate is for when the user is browsing beatmaps
# neccessary info that will need to be loaded prior is:
# ar, cs, star rating, author, length, diff name, hit objects, bpm




class GAMESTATE_BeatmapSelection:


    def loadBeatmaps(self):

        logging.info("Loading beatmaps!")

        for beatmapFolder in glob.glob(f'{osuGlobals.osuSettings["BeatmapDirectory"]}\\*'):
            logging.info(f'checking {beatmapFolder} for beatmaps!')

            beatmapName = os.path.basename(beatmapFolder)
            self.beatmaps.update({beatmapName:osuBeatmap.BmCollection(beatmapFolder)})

        #print(self.beatmaps)

    def __init__(self, gamestateHandler):

        logging.info("Initialized beatmap selection screen!")
        self.handler = gamestateHandler

        self.eventMap = {pygame.K_DOWN:self.nextDiff, pygame.K_UP:self.prevDiff}

        self.tempCanvas = pygame.Surface((int(osuGlobals.osuSettings["Width"]),int(osuGlobals.osuSettings["Height"])), pygame.SRCALPHA)

        self.beatmaps = {}
        self.loadBeatmaps()

        self.backgroundIMG = pygame.image.load("assets/background.jpg")
        self.backgroundIMG = pygame.transform.scale(self.backgroundIMG, (osuGlobals.osuSettings["Width"], osuGlobals.osuSettings["Height"]))

        self.defaultTitleText = pygame.font.SysFont('Comic Sans MS', 20)

        self.defaultX = math.ceil(osuGlobals.osuSettings["Width"] * (2/3))
        self.defaultY = math.ceil(osuGlobals.osuSettings["Height"]/2 - 100)
        self.defaultWidth = math.ceil(osuGlobals.osuSettings["Width"]  - self.defaultX)
        self.defaultHeight = math.ceil(osuGlobals.osuSettings["Height"] / 10)

        self.cBeatmap = random.choice(list(self.beatmaps.values()))
        print(self.cBeatmap.getCurrentDiff().data)



    def update(self, events):
        pass


    def draw(self):

        self.tempCanvas.blit(self.backgroundIMG, (0,0))
        for bm in range(0,self.cBeatmap.cDiff):
            tempX = self.defaultX + (self.cBeatmap.cDiff - bm)*15
            tempY = self.defaultY - math.ceil((self.defaultHeight * (self.cBeatmap.cDiff - bm))*0.5)
            tempWidth = osuGlobals.osuSettings["Width"] - tempX
            pygame.gfxdraw.box(self.tempCanvas, (tempX, tempY, tempWidth, self.defaultHeight), (25*bm,25*bm,25*bm))
            tempTitle = self.defaultTitleText.render(f"{self.cBeatmap.diffs[bm].data['TitleUnicode']} [{self.cBeatmap.diffs[bm].data['Version']}]", True, (255,255,255))
            self.tempCanvas.blit(tempTitle, (tempX, tempY))

        for bm in range(self.cBeatmap.cDiff + 1, len(self.cBeatmap)):

            tempX = self.defaultX + (len(self.cBeatmap) - bm)*15
            tempY = self.defaultY + math.ceil((self.defaultHeight * (len(self.cBeatmap) - bm))*0.5)
            tempWidth = osuGlobals.osuSettings["Width"] - tempX
            pygame.gfxdraw.box(self.tempCanvas, (tempX, tempY, tempWidth, self.defaultHeight), (25*bm,25*bm,25*bm))
            tempTitle = self.defaultTitleText.render(f"{self.cBeatmap.diffs[bm].data['TitleUnicode']} [{self.cBeatmap.diffs[bm].data['Version']}]", True, (255,255,255))
            self.tempCanvas.blit(tempTitle, (tempX, tempY))



        pygame.gfxdraw.box(self.tempCanvas, (self.defaultX, self.defaultY, self.defaultWidth, self.defaultHeight), (200,200,200))
        tempTitle = self.defaultTitleText.render(f"{self.cBeatmap.getCurrentDiff().data['TitleUnicode']} [{self.cBeatmap.getCurrentDiff().data['Version']}]", True, (255,255,255))
        self.tempCanvas.blit(tempTitle, (self.defaultX, self.defaultY))

        return self.tempCanvas


    def nextDiff(self):
        try:
            self.cBeatmap.diffs[self.cBeatmap.cDiff + 1]
            self.cBeatmap.cDiff += 1
        except IndexError:
            return

    def prevDiff(self):
        if self.cBeatmap.cDiff - 1 < 0:
            return
        self.cBeatmap.cDiff -= 1
        
