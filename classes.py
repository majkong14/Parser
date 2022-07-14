import functions


#some constants to set the parsing parameters
ENTITIES_PER_PAGE = 100



class Posts:

    """ 
        Fields:
        They contain entities of the "id - element" type 
    
        Methods:
        get() - gets the posts using 'GET' request from the website, adds them to the posts_dict

        to_dataframe() - conversion of posts_dict into the pandas.dataframe

        change_cats() - changes id's of the categories for their names in posts_dict

        change_tags() - changes id's of the tags for their names in posts_dict

        change_media() - changes id's of the media elements for the links to them in posts_dict
    """

    posts_dict = dict()

    def __init__(self):
        pass

    def get(self, url):
        page = 1

        while True:
            r = functions.get_connection(f"{url}/posts/?per_page={ENTITIES_PER_PAGE}&page={page}")
            json_list = r.json()

            if json_list and r.status_code == 200:
                for elem in json_list:
                    temp = dict([(elem['id'], elem)])
                    self.posts_dict.update(temp)
            else:
                break
            page+=1

    def to_dataframe(self):
        df = functions.pd.DataFrame.from_dict(self.posts_dict, orient="index")
        return df

    def change_cats(self, cats_dict):
        for elem in self.posts_dict.values():
            for i in range(len(elem['categories'])):
                if (temp := elem['categories'][i]) in cats_dict.keys():
                    elem['categories'][i] = cats_dict[temp]

    def change_tags(self, tags_dict):
        for elem in self.posts_dict.values():
            for i in range(len(elem['tags'])):
                if (temp := elem['tags'][i]) in tags_dict.keys():
                    elem['tags'][i] = tags_dict[temp]

    def change_media(self, media_dict):
        for elem in self.posts_dict.values():
            if (temp := elem['featured_media']) in media_dict.keys():
                    elem['featured_media'] = media_dict[temp]


                
class Categories:

    """
        Fields:
        cats_dict() - dict with "category id - category name" pairs

        order_dict() -  dict with "current category id - id of its parent category" pairs

        Methods:
        get() - gets the categories using 'GET' request from the website, adds them to the саts_dict

        get_order() - gets the dict with "current category id - id of its parent category" pairs
    """
    
    cats_dict = dict()
    order_dict = dict()

    def __init__(self):
        pass

    def get(self, url):
        page = 1

        while True:
            r = functions.get_connection(f"{url}/categories/?per_page={ENTITIES_PER_PAGE}&page={page}")
            json_list = r.json()

            if json_list and r.status_code == 200:
                for elem in json_list:
                    temp = dict([(elem['id'], elem['name'])])
                    self.cats_dict.update(temp)
            else:
                break
            page+=1

    def get_order(self, url):
        page = 1
        
        while True:
            r = functions.get_connection(f"{url}/categories/?per_page={ENTITIES_PER_PAGE}&page={page}")
            json_list = r.json()
            if r.status_code == 200 and json_list:
                for item in json_list:
                    self.order_dict.update({item['id']:item['parent']})
                page +=1
            else:
                break

    def get_parents(self):
        result = dict()

        for node in self.order_dict:
            hierarchy = list()
            hierarchy.append(node)
            node_parent = self.order_dict[node]
            while node_parent != 0:
                hierarchy.append(node_parent)
                if node_parent in self.order_dict.keys():
                    node_parent = self.order_dict[node_parent]

            result.update([(node, hierarchy)])
                    
            print(str(result))
        


class Tags:

    """ 
        Fields:
        tags_dict() - dict with "tag id - name of the tag" pairs

        Methods:
        get() - gets the tags using 'GET' request from the website, adds them to the tags_dict
    """

    tags_dict = dict()

    def __init__(self):
        pass

    def get(self, url):
        page = 1

        while True:
            r = functions.get_connection(f"{url}/tags/?per_page={ENTITIES_PER_PAGE}&page={page}")
            json_list = r.json()

            if json_list and r.status_code == 200:
                for elem in json_list:
                    temp = dict([(elem['id'], elem['name'])])
                    self.tags_dict.update(temp)
            else:
                break
            page+=1


class Media:

    """ 
        Fields:
        media_dict() - dict with "id медиа сущности - название этой сущности" pairs

        Мethods:
        get() - gets the media using 'GET' request from the website, adds them to the media_dict
    """

    media_dict = dict()

    def __init__(self):
        pass

    def get(self, url):
        page = 1

        while True:
            r = functions.get_connection(f"{url}/media/?per_page={ENTITIES_PER_PAGE}&page={page}")
            json_list = r.json()

            if json_list and r.status_code == 200:
                for elem in json_list:
                    temp = dict([(elem['id'], elem['guid']['rendered'])])
                    self.media_dict.update(temp)
            else:
                break
            page+=1
