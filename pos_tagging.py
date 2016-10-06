import sys
import codecs
from konlpy.tag import Komoran, Twitter, Mecab

DELIMITER = "\001"
DELIMITER2 = "\t"

if __name__ == "__main__":
	inputFilename = sys.argv[1]
	outputFilename = sys.argv[2]
	parser = sys.argv[3] if len(sys.argv) > 3 else "Mecab"
	columnIndicator = sys.argv[4] if len(sys.argv) > 4 else None

	selectedDelimiter = None

	p = None

	if parser == "Komoran":
		p = Komoran()
	elif parser == "Twitter":
		p = Twitter()
	elif parser == "Mecab":
		p = Mecab()

	f = codecs.open(inputFilename, "r", "utf-8")
	f2 = codecs.open(outputFilename, "w", "utf-8")

	for line in f:
		try:
			if line.strip() != "":
				if selectedDelimiter == None:
					selectedDelimiter = DELIMITER if DELIMITER in line else DELIMITER2

				tokens = line.strip().split(selectedDelimiter)
				tmpLine = ""

				for i, t in enumerate(tokens):
					t = t.strip()
					if columnIndicator == None or (len(columnIndicator) > i and columnIndicator[i] == "1"):
						if p != None:
							tmpLine += " ".join(["%s" % word for word in p.morphs(t)]) + "t"
						else:
							tmpLine += t + "\t"
					else:
						tmpLine += t + "\t"

				#print tmpLine.strip()
				f2.write(tmpLine.strip() + "\n")
		except Exception, e:
			print e

	f2.close()
	f.close()
