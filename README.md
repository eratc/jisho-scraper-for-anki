# jisho-scraper-for-anki

Jisho Scraper For Anki is a web scraper to create [Anki](https://apps.ankiweb.net/) notes for Japanese vocabulary 
and kanji from [Jisho](http://jisho.org) links. It reads Jisho links line by line from a ```.txt``` file and outputs
a bundle of notes as a ```.csv``` file to be imported to Anki. Fields include html scraped from Jisho, used with 
styling of Jisho to create notes which look like Jisho pages with some custom changes.

## Requirements

 - **Python 3.8** or above
 - Python modules **requests** and **Beautiful Soup 4**

## Usage 

 1. Create a note type in Anki with following fields: {Word, Furigana, Sound, Jisho Tags, Meanings, 
    Kanji In Word}
    
 2. Use the html from [this gist](https://gist.github.com/eratc/9c86aaec62af0126507bd0807f40dcab) for the back template of cards.

 3. Use the CSS from [this gist](https://gist.github.com/eratc/dfb153f18dabcfca519c1eb765a52b41) to make back of the 
    cards look like Jisho pages.

 4. Download the project
    
 5. Set ```ANKI_MEDIA_PATH``` to Anki ```collection.media``` folder path as an environment variable. Refer to 
[related Anki docs page](https://docs.ankiweb.net/#/files) where this folder might be according to your operating 
    system.
    
 6. Create a ```.txt``` file. Write Jisho links you want to make into notes line by line.

        https://jisho.org/word/%E7%9C%BC%E9%8F%A1
        https://jisho.org/word/%E6%9C%AC%E6%A3%9A
        https://jisho.org/word/%E5%A4%A7%E4%B8%88%E5%A4%AB
    
 7. Run ```main.py``` from command line with parameters 
    **-I \YOUR\INPUT\PATH\input.txt -O \YOUR\OUTPUT\PATH\output.csv**
    
        python main.py -I C:\Users\Dumile\Desktop\jisho_links.txt -O C:\Users\Dumile\Desktop\anki_notes.csv
    
 8. Import ```.csv``` file into Anki with these settings:
 - Fields seperated by: Comma
 - Uncheck **'Allow HTML in fields'**
 - Make sure all 6 fields are mapped correctly