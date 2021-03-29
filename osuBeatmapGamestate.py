import glob
import logging
import os
import pygame
import random

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

        self.tempCanvas = pygame.Surface((int(osuGlobals.osuSettings["Width"]),int(osuGlobals.osuSettings["Height"])), pygame.SRCALPHA)

        self.beatmaps = {}
        self.loadBeatmaps()

        self.backgroundIMG = pygame.image.load("assets/background.jpg")
        self.backgroundIMG = pygame.transform.scale(self.backgroundIMG, (osuGlobals.osuSettings["Width"], osuGlobals.osuSettings["Height"]))

        self.cBeatmap = random.choice(list(self.beatmaps.values()))
        print(self.cBeatmap)



    def update(self, events):
        pass


    def draw(self):

        self.tempCanvas.blit(self.backgroundIMG, (0,0))

        return self.tempCanvas

        
