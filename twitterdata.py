import tweepy
import configparser


# configparser  for read files
config = configparser.ConfigParser()
config.read('config.ini')

# twitter app details
app_key = 'BGpC3UyTuajGOB7KJqikJZqpq'
app_secret = 'qYHfOXpKTIlWlrNUePtTRtn9xgJJwlgX4NUpSUShpuZPDb5mET'
access_token = '1502851009994919938-H455qJzUD8Y45NTG33SOdYVpxipz9a'
access_token_key = 'yVWfsHmfJOfV6ddHniBxFH3mFIVGfrGNmgKrHm20o4Di6'

# authorization and accessing keys
authority = tweepy.OAuthHandler(app_key, app_secret)
authority.set_access_token(access_token, access_token_key)

# calling the api
api = tweepy.API(authority)

#targeted user
user = 'Calendly'
limit = 20000
followers = tweepy.Cursor(api.get_followers,screen_name = user,count = 200).items(limit)

#for converting to file type

#columns = ['Name','Screen_name','Location','Time','Followers_count','Url','Description']

#row = []
for followers in followers:
      print([followers.name])

'''df = pd.DataFrame(row, columns = columns)
print(df)
#to csv file
df.to_csv('Twitter followers data.csv')'''
