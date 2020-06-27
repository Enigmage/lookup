# pluck
A simple python command-line tool to fetch and display meaning, synonyms and antonyms of any word right in the terminal.

#### Usage: pluck [OPTION] [WORD] 

    List the synonym,antonym and meaning of a word in the terminal
    
    Options:
        -m                  Fetch meaning of a word
        -s                  Fetch synonyms of a word
        -a                  Fetch antonyms of a word
    
    Example:
        
        $ pluck -m scrupulous      (Fetches the meaning of Scrupulous)
        $ pluck -s scrupulous      (Fetches the synonyms of Scrupulous)
        $ pluck -a scrupulous      (Fetches the antonyms of Scrupulous)

#### Installation:

    Requirements:
        
        Make sure you have python3 and pip3 installed on your system.
        Rest of the dependencies will be installed automatically.
        Also if your local bin directory is not added the PATH by default, make sure to add it.
        
        To do that add the following line at the end of your ~/.profile or ~/.bash_profile:
        
             export PATH=$PATH:~/.local/bin/
            
        Save and exit then run:
            
            $ source .profile
                    or
            $ source .bash_profile
             

    Using pip:
        
        1. Clone this repository
        2. navigate to the directory:
            
            $ cd pluck

           then:

            $ pip3 install .

        3. You are good to go!
      
    Using install script:
        
        1. Script assumes you use .profile to set up PATH entries; if otherwise go ahead and
           change the source code of /install to whatever you use. 
        2. Clone the repo then navigate to the directory.
        3. Inside it run:
            
            $ chmod +x install

           To give executable permission to the install script.
           Then simply run:
            
            $ ./install
           
           This will take care of installing the tool and setting up the path variable.

#### Recommended
    
    The main purpose of this tool is to not have to open up another browser window to lookup simple things
    like synonyms or meanings of words. So, opening up another terminal window is still not efficient enough.
    Thus, it is recommended to use a drop-down terminal or scratchpads(like in dwm) to use this tool, which
    will make your workflow much more efficient.

