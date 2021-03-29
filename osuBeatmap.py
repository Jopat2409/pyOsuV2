import os
import glob
import logging


# a beatmap collection, a collection of difficulties
class BmCollection:

    def __init__(self, path):

        self.name = os.path.basename(path)
        diffs = []
        for beatmap in glob.glob(f'{path}\\*.osu'):

            diffs.append(BaseBeatmap(beatmap))


# a specific beatmap within a collection - IE a specific difficulty
# contains basic info about a beatmap - enough to display data and play the beatmap if needed
class BaseBeatmap:


    def __init__(self, path):

        self.data = {"AudioFilename":"",
                     "PreviewTime":0,
                     "TitleUnicode":"",
                     "ArtistUnicode":"",
                     "Creator":"",
                     "HPDrainRate":0.0,
                     "CircleSize":0.0,
                     "OverallDifficulty":0.0,
                     "ApproachRate":0.0,
                     "SliderMultiplier":0.0,
                     "SliderTickRate":0.0
                     }



        with open(path,encoding='utf-8') as beatmap:

            keys = self.data.keys()
            counter = 0
            for line in beatmap:
                parse = line.split(":")
                try:
                    if str(parse[0]) in keys:
                        self.data[str(parse[0])] = parse[1].strip(' \n')
                except KeyError:
                    logging.warning(f"{parse[0]} is bad")
                    pass
                except IndexError:
                    logging.warning(f"{parse} is causing an index error to occur, this should not be anything to worry about")
                    pass

        #print(self.data)

            # the only
            
