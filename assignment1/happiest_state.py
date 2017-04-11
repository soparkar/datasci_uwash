import json
import sys

def isState(location):
    states = ['WA', 'WI', 'WV', 'FL', 'WY', 'NH', 'NJ', 'NM', 'NA', 
              'NC', 'ND', 'NE', 'NY', 'RI', 'NV', 'GU', 'CO', 'CA', 
              'GA', 'CT', 'OK', 'OH', 'KS', 'SC', 'KY', 'OR', 'SD', 
              'DE', 'DC', 'HI', 'PR', 'TX', 'LA', 'TN', 'PA', 'VA', 
              'VI', 'AK', 'AL', 'AS', 'AR', 'VT', 'IL', 'IN', 'IA', 
              'AZ', 'ID', 'ME', 'MD', 'MA', 'UT', 'MO', 'MN', 'MI', 
              'MT', 'MP', 'MS']
    return location in states
    
def populateScoreMap(sentimentScoreFile):
    scores = {}
    for line in sentimentScoreFile:
        term, score  = line.split("\t")
        scores[term] = int(score)
    return scores

def location(tweetJosn):
    try:
        if tweetJosn is None:
            return 
            
        # extract location from tweet
        loc = (tweetJosn.get('place') or {}).get('full_name')
        if loc:
            return loc.strip().split()[-1].upper()
        
        # if tweet has no location, extract it from user info
        loc = (tweetJosn.get('user') or {}).get('location')
        if loc:
            return loc.strip().split()[-1].upper()
    except:
        pass
        
def main():
    tweet_file   = open(sys.argv[2])
#    allTweets = []
    word_scores  = populateScoreMap(open(sys.argv[1]))
    allTweets = [json.loads(line) for line in tweet_file]
    locationScoreMap = {}
    
    for eachTweet in allTweets:
        if 'text' in eachTweet.keys():
            loc = location(eachTweet)
            if isState(loc):
                words = eachTweet['text'].split()
                tweet_score = sum(word_scores.get(word.lower(), 0) for word in words)
                scoreArray = locationScoreMap.get(loc) or []
                scoreArray.append(tweet_score)
                locationScoreMap[loc] = scoreArray
        
    averages = [(t, float(sum(locationScoreMap[t])) / len(locationScoreMap[t])) for t in locationScoreMap]

    happiestState = averages[0][0]
    maxScore = averages[0][1]
    for s, v in averages:
        if v > maxScore:
            happiestState = s
            maxScore = v
            
    print happiestState

if __name__ == '__main__':
    main()
