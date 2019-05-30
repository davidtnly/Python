#! python3
# 12-parse-movies.py - Webscrape IMDB website for top movies per year

"""
https://www.dataquest.io/blog/web-scraping-beautifulsoup/


To source data for data science projects, you’ll often rely on SQL and NoSQL databases, APIs, or
ready-made CSV data sets.

The problem is that you can’t always find a data set on your topic, databases are not kept current
and APIs are either expensive or have usage limits.

If the data you’re looking for is on an web page, however, then the solution to all these problems is web scraping.

In this tutorial we’ll learn to scrape multiple web pages with Python using BeautifulSoup and requests.
We’ll then perform some simple analysis using pandas, and matplotlib.

You should already have some basic understanding of HTML, a good grasp of Python’s basics, and a rough
idea about what web scraping is. If you are not comfortable with these, I recommend this beginner web scraping tutorial
"""

"""
High level outline on the current code structure
- Figure out what elements you are trying to extract
- Explore the HTML structure of the website
- Begin to parse out the links using BeautifulSoup
- Find the elements needed to extract each information piece
- Create a for loop with warnings, error handling, sleep,and show requests; extract requests to a txt file
    - Loop includes gathering of all the pages and years of information needed then add it to a dataframe
- Explore the dataframe - describe(), head(), .loc[['min', 'max'], ['col1', col2']]
- Save the file to the folder
- (Extra): Save the data to a database and then using the db, create a functional webpage with statistics
"""

import os
from requests import get
import bs4
import time
import pandas as pd
from IPython.core.display import clear_output
from warnings import warn

"""
Identify the URL structure and the correct directory needed
"""
d = 'C:\\Users\\' + os.getlogin() + '\\Documents\\Programming\\Python\\Review\\12-files'
os.chdir(d)
os.getcwd() # Confirm that I am in the correct dir

"""
Get URL using bs4 and assign the URL to a variable - print out the first 500 text
"""
url = 'http://www.imdb.com/search/title?release_date=2019&sort=num_votes,desc&page=1'

# Get the response object and print
res = get(url)
print(res.text[:500])

"""
Now we want to parse out the request object into a bs4.element object.
Add in a 'html.parser' argument into the function to use the internal parser from Python
"""
soup = bs4.BeautifulSoup(res.text, 'html.parser')
type(soup)

"""
After figuring out what HTML element we want to use, extract each element one by one before adding them altogether
"""
# This is the main div (container) using .findAll()
movie_containers = soup.findAll('div', class_='lister-item mode-advanced')  # Main element holding all the info

# Access the first container by adding an index [0]
print(movie_containers[0])

# Get the first name element
print(movie_containers[0].h3.a.text)  # Name is nested within the h3 tag in an anchor tag of the third div tag
first_name = movie_containers[0].h3.a.text

# Get year - Using the .find() method vs. .findAll(); .find() returns only the first match == find_all(limit = 1)
first_year = movie_containers[0].h3.find('span', class_='lister-item-year text-muted unbold')  # Within h3 tag
first_year = first_year.text  # Get text within the span tag

# Get IMDB Rating - notice there is a strong tag so we can try the dot notation but first try .find() method
print(movie_containers[0].find('div', class_='inline-block ratings-imdb-rating'))
# The above does show the rating but we can access the strong element using a dot notation
print(movie_containers[0].strong)
first_imdb = movie_containers[0].strong.text
first_imdb = float(first_imdb)  # float data types return decimal values
print(first_imdb)

# Get the Metascore - found a span tag with a class "metascore favorable"; try .find() method
first_mscore = movie_containers[0].find('span', class_='metascore favorable')
print(first_mscore)
# Use the dot notation and use .text then transform the value to an int
first_mscore = int(first_mscore.text)
print(first_mscore)

# Number of votes - this is a different way using attrs parameter within .find() method
# There is a distinctive mark that is a name attribute with the value nv holding a datatype value
# Using attrs parameter, pass the attributes and values as a dictionary
first_votes = movie_containers[0].find('span', attrs={'name':'nv'})  # Using {}
print(first_votes)
print(first_votes.text)  # It looks like you can pull the text value with a comma
type(first_votes)
# Instead of having the need to strip the comma, we can get the data-type attribute within the span
first_votes = first_votes['data-value']
first_votes = int(first_votes)
print(first_votes)  # 555555 vs 555,555

"""
Test to see if we can create an initial loop around the first container before adding all
"""
# Create empty lists to store the scraped data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

# Extract the data from an individual movie container
for container in movie_containers:
    # If the movie has no metascore then don't extract
    if container.find('div', class_='ratings-metascore') is not None:
        # Get Name
        name = container.h3.a.text
        names.append(name)
        # Get Year
        year = container.find('span', class_='lister-item-year').text
        years.append(year)
        # Get IMDB Rating
        imdb = container.strong.text
        imdb_ratings.append(imdb)
        # Get Metascore
        m_score = container.find('span', class_='metascore').text
        metascores.append(m_score)
        # Get Votes
        vote = container.find('span', attrs = {'name','nv'})['data-value']
        votes.append(vote)

"""
Now we have all the elements needed and we have to create a loop for every container now.
Using pandas, we can create an empty DataFrame to score the values
"""
first_df = pd.DataFrame({'movies':names,
                         'years':years,
                         'imdb':imdb_ratings,
                         'metascore':metascores,
                         'votes':votes})
print(first_df.info())
print(first_df.head())

"""
If you run code from a country where English is not a main language, it's very likely that you'll get some movie
names translated into the country's main language. This happens because the server infers your location based on IP.

If this issue happens, pass the following values to the headers parameter of the get() function, which will
communicate to the server to want American English (en-us) language. The q argument indicates the degree to 
which we prefer a certain language.
"""
headers = {'Accept-Language':'en-US, en; q=0.5'}

"""
Begin the looping process with warnings, sleep, requests monitoring messages
"""
# Begin with warning message if needed instead of break and stopping the entire loop
warn('Warning simulation')

# Create lists of pages and years that will be looped
pages = [str(i) for i in range(5)]
years_url = [str(i) for i in range(2015, 2020)]

# Redeclare the lists to store the data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

# Prepare the monitoring of the loop
start_time = time.time()
requests = 0
store_requests = []

# Create a loop for every year, every page, if metascore is not None, requests
# For every year, every page, request URL
for year_url in years_url:
    for page in pages:
        res = get('http://www.imdb.com/search/title?release_date=' + year_url + '&sort=num_votes,desc&page=' + page, \
                  headers = headers)
        # Pause the loop
        sleep(random.randint(8, 15))
        # Monitor the requests
        requests+=1
        elapsed_time = time.time() - start_time
        txt = 'Requests: {}, Frequency: {} requests/s'.format(requests, requests/elapsed_time)  # format notation
        print(txt)
        # Store the requests since we are going to clear the output view
        store_requests.append(txt)
        # Clear the output view
        clear_output(wait=True)
        # Throw a warning for non-200 status codes
        if res.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, res.status_code))
        if requests > 72:
            warn('Number of requests were greater than expected.')
            break
        # Parse the content of the request with BeautifulSoup
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        # Get the main container
        mv_containers = soup.find_all('div', class_='lister-item mode-advanced')
        # For every movie per year per page
        for containers in mv_containers:
            # Check metascore
            if containers.find('div', class_='ratings-metascore') is not None:
                # Name - within h3 element within anchor tag
                name = container.h3.a.text
                names.append(name)
                # Year - within h3 element within span
                year = container.h3.find('span', class_='lister-item-year').text
                years.append(year)
                # IMDB Rating - within the strong element
                imdb = float(container.strong.text)
                imdb_ratings.append(imdb)
                # Metascore
                m_score = container.find('span', class_='metascore').text
                metascores.append(int(m_score))
                # Votes - within attributes; use attrs dictionary values
                vote = container.find('span', attrs = {'name':'nv'})['data-type']
                votes.append(vote)

# Create a new df to store the looped values
movie_df = pd.DataFrame({'movie':names,
                         'years':years,
                         'imdb':imdb_ratings,
                         'metascore':metascores,
                         'votes':votes})

# Print df info
print(movie_df.info())
print(movie_df.head())

"""
Now we can start to do some minor cleaning and extract the data to a CSV file
"""
# Let's reorder the columns; to do that just list out the column names differently
movie_df = movie_df[['movie', 'years', 'imdb', 'metascore', 'votes']]  # [[]]
print(movie_df.head())

# Clean the years column - check for unique values
print(movie_df['years'].unique())  # find string pattern which is the fifth character to the second with .str() method

# Extract the year using .str() method and .loc() method which takes index labels and returns rows and convert
movie_df.loc[:, 'years'] = movie_df['year'].str[-5:-1].astype(int)
print(movie_df['years'].head())

# Describe method to get min/max values
print(movie_df.describe())

# Using pandas describe() method and .loc() method, get the min/max columns
print(movie_df.describe())  # first describe
print(movie_df.describe().loc[['min', 'max', 'mean']])  # second locate the rows
print(movie_df.describe().loc[['min', 'max', 'mean'], ['imdb', 'metascore']])  # third add in column names

# Normalize the imdb variable to be on the same scale as metascore
movie_df['n_imdb'] = movie_df['imdb']*10  # Create a new column by just adding a new name within []
print(movie_df.head())

"""
Create a new CSV file by using .to_csv() method
"""
movie_df.to_csv('movie_ratings_2.csv')

"""
Using matplotlib to plot and analyze the distributions
"""
import matplotlib.pyplot as plt

# Create a figure object with 3 axes (use plt.subplots())
fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (16,4))
ax1, ax2, ax3 = fig.axes

# Plot the distribution of each unnormalized rating on an individual axis
ax1.hist(movie_df['imdb'], bins = 10, range = (0,10))
ax1.set_title('IMDB Rating')

ax2.hist(movie_df['metascore'], bins = 10, range = (0,100))
ax2.set_title('Metascore')

# Plot the normalized distributions of the two ratings on the same axis
ax3.hist(movie_df['n_imdb'], bins = 10, range = (0,100), histtype = 'step')
ax3.hist(movie_df['metascore'], bins = 10, range = (0,100), histtype = 'step')
ax3.legend(loc = 'upper left')
ax3.set_title('The Two Normalized Distributions')

# Hide the top and right spines of all the three axes
for ax in fig.axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.show()
    plt.pause(5) # show it for 5 seconds - crashing with pause()

"""
Starting with the IMDB histogram, we can see that most ratings are between 6 and 8. There are few movies with a 
rating greater than 8, and even fewer with a rating smaller than 4. This indicates that both very good movies and 
very bad movies are rarer.

The distribution of Metascore ratings resembles a normal distribution – most ratings are average, peaking at the 
value of approximately 50. From this peak, the frequencies gradually decrease toward extreme rating values. According 
to this distribution, there are indeed fewer very good and very bad movies, but not that few as the IMDB ratings 
indicate.

On the comparative graph, it’s clearer that the IMDB distribution is highly skewed toward the higher part of the 
average ratings, while the Metascore ratings seem to have a much more balanced distribution.

What might be the reason for that skew in the IMDB distribution? One hypothesis is that many users tend to have a 
binary method of assessing movies. If they like the movie, they give it a 10. If they don’t like the movie, they 
give it a very small rating, or they don’t bother to rate the movie. This an interesting problem that’s worth being 
explored in more detail.
"""