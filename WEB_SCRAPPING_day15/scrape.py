

# # step 1 Import 

# import html
# import requests
# from bs4 import BeautifulSoup
# import csv
# import json

# # URL of the web page you want to scrape
# url = 'https://example.com'


# # step 3 parse the html using beautiful soup

# soup = BeautifulSoup(html_content, 'html.parser')

# # step4 find the specified data

# data = [
#     for item in soup.find_all('a'):
#         title = item.text.strp()
#         link = item.get('href')
#         data.append({'title': title, 'link': link}) 
# ]


# # Step 5 save the data to the csv file


# csv


# scrape.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# URL of the web page to scrape
url = 'https://example.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Let's assume we want to scrape titles and links from articles
    # This is a placeholder and should be adjusted based on the actual structure of the website
    titles = []
    links = []
    
    # Find all article elements (update the selector based on actual website structure)
    articles = soup.find_all('article')
    
    for article in articles:
        title = article.find('h2').get_text()
        link = article.find('a').get('href')
        titles.append(title)
        links.append(link)
    
    # Create a DataFrame from the scraped data
    data = pd.DataFrame({
        'Title': titles,
        'Link': links
    })
    
    # Save the DataFrame to a CSV file
    data.to_csv('scraped_data.csv', index=False)
    print("Data saved to scraped_data.csv")
    
    # Save the DataFrame to a JSON file
    data.to_json('scraped_data.json', orient='records', lines=True)
    print("Data saved to scraped_data.json")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")


# Do testing 
