
import classes


URL = 'PASTE THE URL OF THE WEBSITE TO PARSE HERE'
FILENAME = 'NAME OF THE OUTPUT FILE'

#Driver
def parse(url, file):
    posts = classes.Posts()
    posts.get(URL)

    cats = classes.Categories()
    cats.get(URL)
    
    #functionality example for 'cats' class
    cats.get_order(URL)
    cats.get_parents()
    
    tags = classes.Tags()
    tags.get(URL)

    media = classes.Media()
    media.get(URL)

    #functionality example 'posts' class
    posts.change_cats(cats.cats_dict)
    posts.change_tags(tags.tags_dict)
    posts.change_media(media.media_dict)

    df = posts.to_dataframe()
    df.to_excel(file)


#Driver call
parse(URL, FILENAME)
