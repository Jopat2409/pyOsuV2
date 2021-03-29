
import math




def blitCenter(toBlit, blittedTo):

	w, h = toBlit.get_size()
	w2, h2 = blittedTo.get_size()


	xCoord = math.ceil((w2 - w) / 2)
	yCoord = math.ceil((h2 - h) / 2)

	blittedTo.blit(toBlit, (xCoord, yCoord))