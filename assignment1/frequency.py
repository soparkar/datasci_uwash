import collections
import json
import sys

def main():
	tweet_file = open(sys.argv[1])
	termsCountMap = {}
	allTweets = [json.loads(line) for line in tweet_file]
	for eachTweet in allTweets:
		if 'text' in eachTweet.keys():
			words = eachTweet['text'].split()
			for word in words:
				count = termsCountMap.setdefault(word, 0)
				termsCountMap[word] = count + 1

	totalTerms = sum(termsCountMap.values())
	for k, v in termsCountMap.iteritems():
		print k, float(v)/totalTerms

if __name__ == '__main__':
    main()
