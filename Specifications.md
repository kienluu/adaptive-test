# Adaptive Lab Tweets Test
===

## Specifications
===

### External Tweet Api:
===

There is an api at http://adaptive-test-api.herokuapp.com/tweets.json.
This will returns 10 random tweets with an id which I assume is unique.

### Tasks

A cron like scheduled job is needed to retrieve the external tweet api
and store these in our own database.


### Django
===

### Models
===
Model Tweet
	- id
		primary key
	- sentiment score
		float number
		range -1 to 1 inclusive
	- updated_at
		timestamp.
		datetime.
	- created_at
		timestamp.
		datetime.
	- followers
		integer
		number of followers
	- message
		string (There are no mentions of a max size of this field)
		a status message
	- user_handle
		foreignkey to TweetUser
		starts with @
		I'm guessing it can only contain the characters a-z 0-9 - _ after the @ sign
		
Model TweetUser
	- handle
		string (No mention of a max number)
		unique 
		
### Views
===

View tweet_list(keyword):
	Will return a list of Tweets that contains one or more of the
	keyword in the Tweet message field.
	
	Test actually wants views for 3 specific keywords:  ‘coke’, ‘coca-cola’ and ‘diet cola’
	
	Requirements:
	
	- Tweets will be ordered with sentiment (no mention of ascending or descending in description)
	- Show the message field of the Tweet results
	- Each Tweet need to have a link to the tweet view
	- Percentage of updates containing the keywords (This could be seperate view too)
	
View tweet(id):
	This view will display
	- the sentiment score
	- the number of people who have received the message (I assume this is the followers field)

