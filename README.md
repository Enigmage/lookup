# pluck
A simple python command-line tool to fetch and display meaning, synonyms and antonyms of any word right in the terminal.

### Usage: pluck [OPTION] [WORD] 

List the synonym,antonym and meaning of a word in the terminal

Options:
    -m                  Fetch meaning of a word
    -s                  Fetch synonyms of a word
    -a                  Fetch antonyms of a word

Example:
    
    $ pluck -m scrupulous      (Fetches the meaning of Scrupulous)
    $ pluck -s scrupulous      (Fetches the synonyms of Scrupulous)
    $ pluck -a scrupulous      (Fetches the antonyms of Scrupulous)

Screenshot:

![example](.github/sc02.png)



### Installation:

#### Requirements:
    
Make sure you have python3 and pip3 installed on your system.
Rest of the dependencies will be installed automatically.
Also if your local bin directory is not added to the PATH variable
by default, make sure to add it.

To do that add the following line at the end of your ~/.profile or ~/.bash_profile:

     export PATH=$PATH:~/.local/bin/
    
Save and exit then run:
    
    $ source .profile
            or
    $ source .bash_profile
         

### Using pip:
    
1. Clone this repository
2. navigate to the directory:
    
        $ cd pluck

   then:

        $ pip3 install .

3. You are good to go!

### Recommended:
    
 This tool will work best with drop-down terminal or scratchpads, as you don't have to open any new
 window to lookup simple meanings/synonyms/antonyms of any word.

