from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s
from google import search
#consumer key, consumer secret, access token, access secret.
ckey="w8wyoAKvlN9MEDR18HFzKyzUA"
csecret="W4R5i6VAkTgs6Tr6Ij3Jfk8x6k1rkqdPzb5R2JkFq2ccTQqdVr"
atoken="4157664553-PmCikHvFMBXmUf71TruTVi4hg8L4s2kdYaZgg5i"
asecret="Y4rxXI6s8TDmJD5YQZLRqHLPb7d9iTBFi40eoO7weE7Sw"

class listener(StreamListener):
    
    def on_data(self, data):
        pos_cnt=0
        neg_cnt=0
        
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            
            if sentiment_value == "pos":
                pos_cnt=pos_cnt+1
                print("\n heyyyyy POSITIVE------------------------------------" + pos_cnt)
            else:
                neg_cnt=neg_cnt+1
                print("\n heyyyyy NEGATIVE------------------------------------" + neg_cnt)
                
                
            if confidence*100 >= 80:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write('\n\n')
                output.close()
                print("POSITIVE COUNTER: " + pos_cnt)
                print("NEGATIVE COUNTER: " + neg_cnt)
            return True
        
        except:
            return True
        

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["narendramodi"])