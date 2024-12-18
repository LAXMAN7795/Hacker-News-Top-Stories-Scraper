Hacker-News-Top-Stories-Scraper:
A Python-based web scraping tool to fetch and display the top trending stories on Hacker News with more than 99 votes.

Introduction:
Hacker News is a popular platform for tech enthusiasts to share and discuss the latest news and articles. However, manually identifying the top stories can be time-consuming. This script automates the process by:

Scraping data from Hacker News' first two pages.
Filtering stories with more than 99 votes.
Sorting them in descending order of popularity.
Whether you're conducting research, staying updated on trends, or just exploring tech news, this tool simplifies it all.

Key Features:
Efficient Scraping: Fetches data from Hacker News' multiple pages.
Custom Filtering: Displays only the most popular stories with more than 99 votes.
Data Sorting: Outputs stories ranked by vote count in descending order.
Readable Output: Uses Python's pprint module for easy reading.

Technologies Used:
Python: Core programming language.
Requests: For sending HTTP requests to fetch web page data.
BeautifulSoup: For parsing HTML and extracting content.
pprint: For formatting the output.

Setup Instructions
Follow these steps to get started with the project:

Prerequisites:
Python 3.x installed.
Familiarity with Python and web scraping concepts.

Steps
Clone the repository:
git clone https://github.com/yourusername/Hacker-News-Top-Stories-Scraper.git

Navigate to the project directory:
cd Hacker-News-Top-Stories-Scraper

Install the required libraries:
pip install requests beautifulsoup4

Run the script:
python scraper.py

Usage
Run the Script: The script fetches data from Hacker News' first two pages.
Filter Stories: It filters stories with more than 99 votes.
View Results: Outputs a list of popular stories in a structured format.

Code Overview
Key Functions
sorted_stories_by_votes(hnlist):

Sorts the list of stories by vote count in descending order.
Input: A list of dictionaries containing story details.
Output: A sorted list.

create_custom_hn(links, subtext):

Combines data from links and metadata to create a list of popular stories.
Filters out stories with fewer than 99 votes.
Input: Parsed HTML elements for links and subtext.
Output: A sorted list of story dictionaries.

Core Logic:
Fetch HTML using requests.
Parse HTML using BeautifulSoup to extract story titles, links, and vote counts.
Combine and filter data, then sort based on popularity.

Sample Output:
The script produces output in the following format:
[
  {
    "title": "Moon",
    "points": 1725,
    "link": "https://ciechanow.ski/moon/"
  },
  {
    "title": "Getting to 2M users as a one woman dev team [video]",
    "points": 642,
    "link": "https://brightonruby.com/2024/getting-to-2-million-users-as-a-one-woman-dev-team/"
  },
  {
    "title": "Always go to the funeral (2005)",
    "points": 486,
    "link": "https://www.npr.org/2005/08/08/4785079/always-go-to-the-funeral"
  },
  {
    "title": "New LLM optimization technique slashes memory costs",
    "points": 437,
    "link": "https://venturebeat.com/ai/new-llm-optimization-technique-slashes-memory-costs-up-to-75/"
  },
  {
    "title": "FTC bans hidden junk fees in hotel, event ticket prices",
    "points": 365,
    "link": "https://www.cnbc.com/2024/12/17/ftc-bans-hidden-junk-fees-in-hotel-event-ticket-prices-.html"
  },
  {
    "title": "MIT study explains why laws are written in an incomprehensible style",
    "points": 291,
    "link": "https://news.mit.edu/2024/mit-study-explains-laws-incomprehensible-writing-style-0819"
  },
  {
    "title": "How I used linear algebra to build an interactive diagramming editor",
    "points": 242,
    "link": "https://medium.com/@ivan.ishubin/how-i-used-linear-algebra-to-build-an-interactive-diagramming-editor-and-why-matrix-math-is-d5bd552f2e8d"
  },
  {
    "title": "3D-Printed Dune Chess Set",
    "points": 201,
    "link": "https://parametric-architecture.com/3d-printed-dune-chess-set-by-rory-noble-turner/"
  },
  {
    "title": "After 3 Years, I Failed. Here's All My Startup's Code",
    "points": 193,
    "link": "https://dylanhuang.com/blog/closing-my-startup/"
  },
  {
    "title": "Microsoft Confirms Password Deletion for 1B Users",
    "points": 193,
    "link": "https://www.forbes.com/sites/zakdoffman/2024/12/13/microsoft-confirms-password-deletion-for-1-billion-users-attacks-up-200/"
  },
  {
    "title": "Advent of Code on the Nintendo DS",
    "points": 184,
    "link": "https://sailor.li/aocnds.html"
  },
  {
    "title": "Crunch – a Scheme compiler with a minimal runtime",
    "points": 173,
    "link": "https://www.more-magic.net/posts/crunch.html"
  },
  {
    "title": "Launch HN: Langfuse (YC W23) – OSS Tracing and Workflows to Improve LLM Apps",
    "points": 171,
    "link": "https://github.com/langfuse/langfuse"
  },
  {
    "title": "Droste’s Lair",
    "points": 152,
    "link": "https://vezwork.github.io/drostes-lair-post/"
  },
  {
    "title": "Natural Number Game: build the basic theory of the natural numbers from scratch",
    "points": 148,
    "link": "https://adam.math.hhu.de/#/g/leanprover-community/NNG4"
  },
  {
    "title": "Show HN: I built an open-source data pipeline tool in Go",
    "points": 143,
    "link": "https://github.com/bruin-data/bruin"
  },
  {
    "title": "Voxon: Real time interactive volumetric holograms",
    "points": 125,
    "link": "https://www.voxon.co"
  },
  {
    "title": "A quick look at OS/2's builtin virtualization",
    "points": 104,
    "link": "https://www.uninformativ.de/blog/postings/2024-12-13/0/POSTING-en.html"
  },
  {
    "title": "Surfer: Open-Source Personal Data Warehouse",
    "points": 102,
    "link": "https://github.com/Surfer-Org/Protocol"
  },
  {
    "title": "A pilot crashed a full passenger jet into the bay, didn't lose his job (2021)",
    "points": 100,
    "link": "https://www.sfgate.com/sfhistory/article/san-francisco-historic-plane-crash-asoh-defense-16319360.php"
  }
]

Future Enhancements:
Planned improvements for the project:

Pagination Support: Automatically scrape more than two pages.
CSV Export: Save the scraped data in CSV format.
GUI: Create a graphical interface for better usability.
APIs: Use Hacker News APIs for more structured data fetching.
Email Notifications: Send top stories via email.




