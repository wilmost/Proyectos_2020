import json 
from operator import itemgetter, attrgetter

sets =[]

class Data(): 
    def __init__(self,hits,visitors,bytes,data):
        self.hits = hits  
        self.visitors = visitors 
        self.bytes = bytes
        self.data = data 
    
    def __repr__(self):
        return repr((self.hits,self.visitors,self.bytes,self.data))



file = "goaccess-1601553965072.json"
with open (file, encoding="utf8") as read_file: 
    data =json.load(read_file) 


#la funcion acepta dos argumentos. data y sort parameter (hits,visitors,bytes, data)
def hots_query(data,sort = "visitors"): #agregar opcion sort by
    vistiors_raw =  data["hosts"]["data"]
    count= 0
    for i in vistiors_raw: 
        elements = Data((i["hits"]["count"],i["hits"]["percent"]),(i["visitors"]["count"],i["visitors"]["percent"]),(i["bytes"]["count"],i["bytes"]["percent"]),i["data"]) 
        sets.append(elements) 
    if sort == "visitors":
        return sorted(sets, key = attrgetter("visitors"),reverse=True) 
    elif sort == "hits":
        return sorted(sets, key = attrgetter("hits"),reverse=True) 
    elif sort == "bytes" :
        return sorted(sets, key = attrgetter("bytes"),reverse=True)  
    elif sort =="data":
        return sorted(sets, key = attrgetter("data"),reverse=True) 
    


def visiTime_query(data,sort = "visitors"): #agregar opcion sort by
    vistiors_raw =  data["hosts"]["data"]
    count= 0
    for i in vistiors_raw: 
        elements = Data((i["hits"]["count"],i["hits"]["percent"]),(i["visitors"]["count"],i["visitors"]["percent"]),(i["bytes"]["count"],i["bytes"]["percent"]),i["data"]) 
        sets.append(elements) 
    if sort == "visitors":
        return sorted(sets, key = attrgetter("visitors"),reverse=True) 
    elif sort == "hits":
        return sorted(sets, key = attrgetter("hits"),reverse=True) 
    elif sort == "bytes" :
        return sorted(sets, key = attrgetter("bytes"),reverse=True)  
    elif sort =="data":
        return sorted(sets, key = attrgetter("data"),reverse=True) 
    


def refering_site_query(data,sort = "visitors"): #agregar opcion sort by
    vistiors_raw =  data["referring_sites"]["data"]
    count= 0
    for i in vistiors_raw: 
        elements = Data((i["hits"]["count"],i["hits"]["percent"]),(i["visitors"]["count"],i["visitors"]["percent"]),(i["bytes"]["count"],i["bytes"]["percent"]),i["data"]) 
        sets.append(elements) 
    if sort == "visitors":
        return sorted(sets, key = attrgetter("visitors"),reverse=True) 
    elif sort == "hits":
        return sorted(sets, key = attrgetter("hits"),reverse=True) 
    elif sort == "bytes" :
        return sorted(sets, key = attrgetter("bytes"),reverse=True)  
    elif sort =="data":
        return sorted(sets, key = attrgetter("data"),reverse=False) 
