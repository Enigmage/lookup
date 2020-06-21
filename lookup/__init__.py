import sys
import requests 
from bs4 import BeautifulSoup as beSo
from colorama import Fore,Style

#query = input(f"{Fore.RED}{Style.BRIGHT}Enter Query: ")
try:
    if(sys.argv[1] == "-s"):

        loadPage = requests.get(f"https://www.thesaurus.com/browse/{sys.argv[2]}")
        src = loadPage.content
        soup = beSo(src, 'html.parser')
        myText = soup.find_all("a", {"class":"css-r5sw71-ItemAnchor etbu2a31"})
        print(f"{Fore.CYAN}{Style.BRIGHT}Synonyms of {sys.argv[2]}:-")
        for num, txt in enumerate(myText, 1):
            print(f"{Fore.GREEN}{Style.BRIGHT}{num}: {txt.text}")
    
    elif(sys.argv[1] == "-a"):
               
        loadPage = requests.get(f"https://www.thesaurus.com/browse/{sys.argv[2]}")
        src = loadPage.content
        soup = beSo(src, 'html.parser')
        myText = soup.find_all("a", {"class":"css-hobnle-ItemAnchor etbu2a31"})
        print(f"{Fore.CYAN}{Style.BRIGHT}Antonyms of {sys.argv[2]}:-")

        for num, txt in enumerate(myText, 1):
            print(f"{Fore.RED}{Style.BRIGHT}{num}: {txt.text}")

    elif(sys.argv[1] == "-m"): 

        loadPage = requests.get(f"https://www.merriam-webster.com/dictionary/{sys.argv[2]}")
# print(loadPage.status_code == 200) 
        src = loadPage.content 

        soup = beSo(src, 'html.parser')

        myText = soup.find_all("span", {"class" : "dtText"})
        
        print(f"{Fore.CYAN}{Style.BRIGHT}Meaning of {sys.argv[2]}:- ")
        for num, txt in enumerate(myText, 1):
            print(f"{Fore.YELLOW}{Style.BRIGHT}{num}{txt.text}")

    else:
        print("Usage lookup [OPTIONS] [WORD] \n Examples: \n $ lookup -m good  (Fetches meaning of good) \n $ lookup -s good  (Fetch synonyms of good) \n $ lookup -a good  (Fetch antonyms of good) ")

except IndexError:

    raise SystemExit("Usage lookup [OPTIONS] [WORD] \n Examples: \n $ lookup -m good  (Fetches meaning of good) \n $ lookup -s good  (Fetch synonyms of good) \n $ lookup -a good  (Fetch antonyms of good) ")


