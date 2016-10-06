import sys
import codecs
from operator import itemgetter

if __name__ == "__main__":
	inputFilename = sys.argv[1]
	outputFilename = sys.argv[2]
	convertFilename = sys.argv[3]
	columnIndice = map(int, sys.argv[4:]) if len(sys.argv) > 4 else [-1]

	columnIndice = sorted(columnIndice)

	cntMap = {}

	f = codecs.open(inputFilename, "r", "utf-8")
	f2 = codecs.open(convertFilename, "w", "utf-8")

	for line in f:
		if line.strip() != "":
			tokens = line.strip().split("\t")

			if len(tokens) > max(0, max(columnIndice)):
				toWrite = ""
				for columnIndex in columnIndice:
					words = tokens[columnIndex].strip().split(" ")

					for w in words:
						cntMap[w] = 1 if cntMap.get(w) == None else (cntMap[w] + 1)

					toWrite += tokens[columnIndex] + " "

				f2.write(toWrite.strip() + "\n")

	f2.close()
	f.close()

	print "Finish to count %d words..." % len(cntMap.keys())

	sortedItems = sorted(cntMap.items(), key = itemgetter(1), reverse = True)

	f = codecs.open(outputFilename, "w", "utf-8")

	for w, c in sortedItems:
		f.write("%s\t%d\n" % (w, c))

	f.close()
