
class BmCollection:



    def __init__(self, path):

        self.name = os.path.basename(path)
        diffs = []
        for beatmap in glob.glob(f'{path}\\*.osu'):

            diffs.append(BaseBeatmap(beatmap))


class BaseBeatmap:




    def __init__(self, path):

        self.data = {}



        with open(path) as beatmap:

            # the only
            
