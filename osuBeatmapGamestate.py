import glob
import logging

import osuGlobals

#this gamestate is for when the user is browsing beatmaps
# neccessary info that will need to be loaded prior is:
# ar, cs, star rating, author, length, diff name, hit objects, bpm




class GAMESTATE_BeatmapSelection:


    def loadBeatmaps(self):

        logging.info("Loading beatmaps!")

        for beatmapFolder in glob.glob(f'{osuGlobals.osuSettings["BeatmapDirectory"]}\\*'):
            logging.info(f'checking {beatmapFolder} for beatmaps!')
            for beatmap in glob.glob(f'{beatmapFolder}\\*.osu'):

                print(beatmap)

    def __init__(self, gamestateHandler):

        logging.info("Initialized beatmap selection screen!")
        self.handler = gamestateHandler
        self.loadBeatmaps()



    def update(self):
        pass


    def draw(self, graphics):

        pass

        
