import sys
import re
import codecs

if __name__ == "__main__":
	inputFilename = sys.argv[1]
	inputEncoding = sys.argv[2]
	outputFilename = sys.argv[3]
	outputEncoding = sys.argv[4]
	referenceFilename = sys.argv[5] if len(sys.argv) > 5 else None
	columnIndicator = sys.argv[6] if len(sys.argv) > 6 else None

	regexs = []

	if referenceFilename != None:
		f = codecs.open(referenceFilename, "r", "utf-8")

		for line in f:
			if line.strip() != "":
				if line[0] == u"#":
					continue
				if line[-2:] == u"\r\n":
					line = line[:-2]
				if line[-1] == u"\r" or line[-1] == u"\n":
					line = line[:-1]

				tokens = line.split("\t")
				print tokens

				regexs.append((tokens[0], tokens[1]))

		f.close()

	print "Start converting."

	f = codecs.open(inputFilename, "r", inputEncoding)
	f2 = codecs.open(outputFilename, "w", outputEncoding)

	for line in f:
		try:
			if line.strip() != "":
				tmpLine = ""
				tokens = line.strip().split("\t")

				for i, token in enumerate(tokens):
					if columnIndicator == None or (len(columnIndicator) > i and columnIndicator[i] == "1"):  
						for src, dest in regexs:
							token = re.sub(src, dest, token) + "\t"
					
					tmpLine = tmpLine + token + "\t"

				f2.write(tmpLine.strip() + "\n")
		except Exception, e:
			print e

	f2.close()
	f.close()