import json
import sys

unknownScoreMap = {}

def populateKnownScoresMap(afinnfile):
    scores = {}
    for line in afinnfile:
	term, score = line.split("\t")
	scores[term] = int(score)
    return scores

def process_tweet_text(text, word_scores):
    words = text.split()
    whole_sentiment = sum(word_scores.get(word, 0) for word in words)
    unknown_words = [w for w in words if w not in word_scores]
    for uw in unknown_words:
	current = unknownScoreMap.setdefault(uw, 0)
	unknownScoreMap[uw] = current + whole_sentiment

def main():
    word_scores = populateKnownScoresMap(open(sys.argv[1]))
    tweet_file = open(sys.argv[2])
    whole_tweets = [json.loads(line) for line in tweet_file]
    for wt in whole_tweets:
	if 'text' in wt.keys():
	    process_tweet_text(wt['text'], word_scores)
	    for term, score in unknownScoreMap.iteritems():
		print term, float(score)

if __name__ == '__main__':
    main()
