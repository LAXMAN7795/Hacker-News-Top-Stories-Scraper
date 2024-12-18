import requests
from bs4 import BeautifulSoup
import pprint

# Fetch content from Hacker News pages
req = requests.get('https://news.ycombinator.com/')
req2 = requests.get('https://news.ycombinator.com/?p=2')

# Parse the HTML content
soup1 = BeautifulSoup(req.text, 'html.parser')
soup2 = BeautifulSoup(req2.text, 'html.parser')

# Select the links and subtext (metadata) for news stories
links1 = soup1.select('.titleline')
subtext1 = soup1.select('.subtext')
links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')

# Combine the links and subtext from both pages
mega_links = links1 + links2
mega_subtext = subtext1 + subtext2

def sorted_stories_by_votes(hnlist):
    """
    Sorts the list of stories based on their vote count in descending order.
    Args:
        hnlist (list): List of dictionaries containing story details.

    Returns:
        list: Sorted list of stories.
    """
    return sorted(hnlist, key=lambda k: k['points'], reverse=True)

def create_custom_hn(links, subtext):
    """
    Creates a list of top stories with more than 99 votes from the Hacker News page.
    Args:
        links (list): List of story links.
        subtext (list): List of story metadata (e.g., votes).

    Returns:
        list: List of dictionaries containing story title, link, and vote count.
    """
    hn = []
    for idx, item in enumerate(links):
        # Extract the story title
        title = item.getText()

        # Extract all hyperlinks associated with the story
        href = item.find_all('a', href=True)
        href_links = [link['href'] for link in href]

        # Extract the vote count if available
        votes = subtext[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points > 99:
                # Append story details to the list
                hn.append({'title': title, 'link': href_links, 'points': points})
    return sorted_stories_by_votes(hn)

# Pretty print the top stories
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
