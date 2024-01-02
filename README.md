# jisho-scraper-for-anki

Jisho Scraper For Anki is a web scraper to create [Anki](https://apps.ankiweb.net/) notes for Japanese vocabulary 
and kanji from [Jisho](http://jisho.org) links. It reads Jisho links line by line from a ```.txt``` file and outputs
a bundle of notes as a ```.csv``` file to be imported to Anki. Fields include html scraped from Jisho, used with 
styling of Jisho to create notes which look like Jisho pages with some custom changes. Check 

## Requirements

 - **Python 3.8** or above
 - Python modules **requests** and **Beautiful Soup 4**

## Create Vocab Cards

 1. Create a note type in Anki with following fields: {Word, Furigana, Sound, Jisho Tags, Meanings, 
    Kanji In Word}
    
 2. Use the html from [this gist](https://gist.github.com/eratc/9c86aaec62af0126507bd0807f40dcab) for the back template of cards.

 3. Use the CSS from [this gist](https://gist.github.com/eratc/dfb153f18dabcfca519c1eb765a52b41) to make back of the 
    cards look like Jisho pages.

 4. Set ```ANKI_MEDIA_PATH``` to Anki ```collection.media``` folder path as an environment variable. Refer to 
[related Anki docs page](https://docs.ankiweb.net/#/files) where this folder might be according to your operating 
    system.
    
 5. Create a ```.txt``` file. Write Jisho links you want to make into notes line by line.

        https://jisho.org/word/%E7%9C%BC%E9%8F%A1
        https://jisho.org/word/%E6%9C%AC%E6%A3%9A
        https://jisho.org/word/%E5%A4%A7%E4%B8%88%E5%A4%AB
    
 6. Run ```main.py``` with your input/output path 
    
        python main.py -I YOUR/PATH/jisho_links.txt -O YOUR/PATH/anki_notes.csv --to_card vocab
    
 7. Import ```.csv``` file into Anki with these settings:
 - Fields seperated by: Comma
 - Uncheck **'Allow HTML in fields'**
 - Make sure all 6 fields are mapped correctly

## Create Kanji Cards

 1. Create a note type in Anki with following fields: {Kanji, Description, Kun, On, Level, Link}
 2. Use html from [this gist](https://gist.github.com/eratc/6acf28534a8561a6d1f947f79cc12e6f) for the back template of cards.
 3. Use the CSS from [this gist](https://gist.github.com/eratc/384562145d1c62c5dd6d663e1db3fe3c).
 4. Create a ```.txt``` file that contains Jisho links like as before.
 5. Run ```main.py``` with ```--to_card kanji``` flag instead.
 6. Import ```.csv``` file the same way.

## Download All Kanji From Search Link

Outputs a ```.txt``` file that contains links from all kanji search results from the link. You can later use it to create kanji cards for Anki. 

 1. Run ```main.py``` with your output path and kanji search link
    
        python main.py -O /YOUR/PATH/kanjilist.txt --list kanji -u "https://jisho.org/search/%23kanji%20%23jinmei"
    
## Get Verb Inflections From Search Link

 1. Run ```main.py``` with your output path and verb search link
    
        python main.py -O /YOUR/PATH/verbinf_notes.csv --verb_inflections