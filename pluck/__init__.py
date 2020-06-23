import requests 
from bs4 import BeautifulSoup as beSo
from colorama import Fore,Style

def scrape(option, word):
    try:
        if( option == "-s"):
            loadPage = requests.get(f"https://www.thesaurus.com/browse/{word}")
            src = loadPage.content
            soup = beSo(src, 'html.parser')
            myText = soup.find_all("a", {"class":"css-r5sw71-ItemAnchor etbu2a31"})
            print(f"{Fore.CYAN}{Style.BRIGHT}Synonyms of {word}:")
            
            for num, txt in enumerate(myText, 1):
                print(f"{Fore.GREEN}{Style.BRIGHT}{num}: {txt.text}")
        
        elif( option == "-a"):            
            loadPage = requests.get(f"https://www.thesaurus.com/browse/{word}")
            src = loadPage.content
            soup = beSo(src, 'html.parser')
            myText = soup.find_all("a", {"class":"css-hobnle-ItemAnchor etbu2a31"})
            print(f"{Fore.CYAN}{Style.BRIGHT}Antonyms of {word}:")

            for num, txt in enumerate(myText, 1):
                print(f"{Fore.RED}{Style.BRIGHT}{num}: {txt.text}")

        elif( option == "-m"): 
            loadPage = requests.get(f"https://www.merriam-webster.com/dictionary/{word}")
            src = loadPage.content 
            soup = beSo(src, 'html.parser')
            myText = soup.find_all("span", {"class" : "dtText"})      
            print(f"{Fore.CYAN}{Style.BRIGHT}Meaning of {word}: ")
            
            for num, txt in enumerate(myText, 1):
                print(f"{Fore.YELLOW}{Style.BRIGHT}{num}{txt.text}")

        else:
            print("Usage pluck [OPTIONS] [WORD] \n Examples: \n $ pluck -m good  (Fetches meaning of good) \n $ pluck -s good  (Fetch synonyms of good) \n $ pluck -a good  (Fetch antonyms of good) ")

    except IndexError:
        raise SystemExit("Usage pluck [OPTIONS] [WORD] \n Examples: \n $ pluck -m good  (Fetches meaning of good) \n $ pluck -s good  (Fetch synonyms of good) \n $ pluck -a good  (Fetch antonyms of good) ")


