import eel
import twint
from collections import Counter

# Set web files folder
eel.init('web')

@eel.expose  
def item_item_cf(bookname):
    return "harry potter"

@eel.expose
def twitter_test():
    c = twint.Config()
    c.Search = "fiction"
    c.Limit = 5
    c.Pandas = True
    twint.run.Search(c)
    Tweets_df = twint.storage.panda.Tweets_df

    counts = Counter()
    for tweet in Tweets_df['tweet'].values:
        counts.update(word.strip('.,?!"\'@').lower() for word in tweet.split())
    dic_list=[]
    for key in counts:
        if counts[key]>1:
            tmp_dic={'word': key, 'size': counts[key]*8}
            dic_list.append(tmp_dic)
    print(dic_list)
    return dic_list

eel.start('welcome.html')  # Start