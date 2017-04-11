import sys
import json

dictMap = {}

def hw():
    print 'Hello, world!'

def createDictionary(dict_file):
    for line in dict_file.readlines():
	term, score = line.split("\t")
	dictMap[term] = int (score)
	
def calculateSentiment(input_file):
    for line in input_file.readlines():
	jsonObj = json.loads(line)
	sentimentSum = 0.0
	if 'text' in jsonObj:
	    words = jsonObj['text'].split()	    
	    for word in words:
		if word in dictMap:
		    sentimentSum += dictMap[word]
	    print sentimentSum

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
#    hw()
    createDictionary(sent_file)
    calculateSentiment(tweet_file)
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
