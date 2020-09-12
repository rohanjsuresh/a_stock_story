# A Stock Story

Hi! Welcome to 'A Stock Story'. This is a personal research project looking into whether stock prices fluctuate with news about the company/product, and what data points are relevant in plotting this trend. 


## Data Sources

The project uses **Yahoo Finance** to get historical stock prices. 
For 'news' data I am using:
- Top 100 Tweets for that company per time interval around New York.
- A financial new Kaggle dataset: https://www.kaggle.com/notlucasp/financial-news-headlines.
	-  Currently only using the Guardan dataset but am planning to expand this.

## Method

### Tweets
For Twitter information I scrape the top 100 Tweets around the New York region relating to a given company over each time interval (default 1 month). I then use NLTK and score each tweet using semantic analysis based on how positive or negative the tweet is. I then normalize the data with the stock price (so that if there is a trend it can be seen better alongside the stock price), remove outliers, then graph the semantic analysis scores over the period specified.
### Financial News Headlines
I first scrape the financial news headlines CSV and create a dictionary where key is date in the form YYYY-MM and value is an array of headlines for that month. Then for each interval over the whole time period specified all the articles relating to the company are collected, similarly NLTK is used to score each headline based on how positive or negative the tweet is. The number of relevant headlines available during each time period is also collected. The semantic analysis score and number of relevant headlines are both normalized against the stock prices over the time period, and a heuristic score is created using both normalized semantic analysis scores and the normalized number of relevant headlines. This was done as I thought that both the positivity/negativity of the headlines AND the popularity of a given company, i.e. how often it was appearing in the news for a given time period, would both be relevant in scoring a time interval. This is then graphed. 
## Example Graphs Produced

### Twitter High and Low Prices + Twitter and Guardian Scores from 2018-01 -- 2019-12
![Image of Twitter Example Graph](https://github.com/rohanjsuresh/a_stock_story/blob/master/images/Twitter_from_2018-1_-_2019-12.png?raw=true)

### Netflix High and Low Prices + Twitter and Guardian Scores from 2018-01 -- 2019-12

![Image of Netflix Example Graph](https://github.com/rohanjsuresh/a_stock_story/blob/master/images/Netflix_from_2018-1_-_2019-12.png?raw=true)

### Facebook High and Low Prices + Twitter and Guardian Scores from 2018-01 -- 2019-12

![Image of Facebook Example Graph](https://github.com/rohanjsuresh/a_stock_story/blob/master/images/Facebook_from_2018-1_-_2019-12.png?raw=true)

### Apple High and Low Prices + Twitter and Guardian Scores from 2018-01 -- 2019-12

![Image of Apple Example Graph](https://github.com/rohanjsuresh/a_stock_story/blob/master/images/Apple_from_2018-1_-_2019-12.png?raw=true)
