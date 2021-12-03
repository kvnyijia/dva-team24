import eel
import twint
from collections import Counter
import re
import nltk
from numpy import number
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
nltk.download("stopwords")
nltk.download('punkt')

# Set web files folder
eel.init('web')

@eel.expose  
def item_item_cf(bookname):
    return "harry potter"

@eel.expose
def twitter_wordcnt(keyword):
    c = twint.Config()
    c.Search = keyword
    c.Lang = "en"
    c.Limit = 100
    c.Pandas = True

    twint.run.Search(c)
    Tweets_df = twint.storage.panda.Tweets_df

    common_words=['', 'all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']
    common_words.append(keyword)
    counts = Counter()
    for tweet in Tweets_df['tweet'].values:
        counts.update(word.strip('.,?!"\'@-').lower() for word in tweet.split())
    dic_list=[]
    for key in counts:
        if key.isalpha()== False:
            continue
        if key in common_words:
            continue
        if counts[key]>1:
            tmp_dic={'word': key, 'size': counts[key]*5}
            dic_list.append(tmp_dic)

    dic_list = sorted(dic_list, key=lambda d: d['size'], reverse=True) 
    recommend_str=""
    for dic in dic_list[:5]:
        recommend_str+=dic['word']
        recommend_str+=" "
    recommended_book=twitter_recommendation(recommend_str)
    return [recommended_book[0],recommended_book[1],recommended_book[2],dic_list]

@eel.expose
def twitter_recommendation(twitter_str):
    df = pd.read_csv('web/data/Preprocessed_data.csv')
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.drop(columns = ['Unnamed: 0','location',
                    'img_s','img_m','city','age',
                    'state','Language','country',
                    'year_of_publication'],axis=1,inplace = True)
    df.drop(index=df[df['Category'] == '9'].index, inplace=True)
    df.drop(index=df[df['rating'] == 0].index, inplace=True)
    df['Category'] = df['Category'].apply(lambda x: re.sub('[\W_]+',' ',x).strip())

    rating_counts = pd.DataFrame(df['book_title'].value_counts())
    rare_books = rating_counts[rating_counts['book_title'] <= 100].index

    common_books = df[~df['book_title'].isin(rare_books)]
    common_books = common_books.drop_duplicates(subset=['book_title'])
    common_books.reset_index(inplace= True)
    common_books['index'] = [i for i in range(common_books.shape[0])]
    common_books.dropna(inplace=True)

    target_cols = ['book_title','book_author','publisher','Category', 'Summary']
    common_books['combined_features'] = [' '.join(common_books[target_cols].iloc[i,].values) for i in range(common_books[target_cols].shape[0])]

    summary_filtered = []
    for i in common_books['combined_features']:
        i = re.sub("[^a-zA-Z]", " ", i).lower()
        i = nltk.word_tokenize(i)
        i = [word for word in i if not word in set(stopwords.words("english"))]
        i = " ".join(i)
        summary_filtered.append(i)
    common_books['combined_features'] = summary_filtered

    keywords = twitter_str
    common_books = common_books.append({'combined_features': keywords}, ignore_index=True)

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(common_books['combined_features'])

    cosine_sim = cosine_similarity(count_matrix)

    numberOfRelatedBook = 1
    sim_books = list(enumerate(cosine_sim[-1]))
    sorted_sim_books = sorted(sim_books, key=lambda x: x[1], reverse=True)[1:numberOfRelatedBook+1]

    books = []
    for i in range(len(sorted_sim_books)):
        books.append(common_books[common_books['index'] == sorted_sim_books[i][0]]['book_title'].item())
    
    df_tmp=df.loc[df['book_title'] == books[0]].iloc[0]
    result=[books[0],df_tmp['isbn'],df_tmp['img_l']]
    return result

eel.start('welcome.html')  # Start