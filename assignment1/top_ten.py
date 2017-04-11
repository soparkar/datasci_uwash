import sys
import re
#import urllib
import json
import operator

hashtagsMap = {}

def populateHashtagsMap(fp):
    for line in fp.readlines(): 
        tweetObj = json.loads(line)
        if "entities" in tweetObj:
            entity = tweetObj["entities"]
            if "hashtags" in entity:
                hashtags = entity["hashtags"]
                for hashtag in hashtags:
                    htag = hashtag["text"]
                    if htag not in hashtagsMap:
                        hashtagsMap[htag] = 0
                    hashtagsMap[htag] += 1

def main():
    tweet_file = open(sys.argv[1])
    populateHashtagsMap(tweet_file)
    sortedMap = sorted(hashtagsMap.iteritems(), key=operator.itemgetter(1), reverse=True)
    for i in range(0, 10):
        print "%s %i" % (sortedMap[i][0].encode("utf-8"), sortedMap[i][1])

if __name__ == '__main__':
    main()

