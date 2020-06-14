# -*- coding: utf-8 -*-

import codecs
from core import httptools
from core import scrapertools
from core import servertools
from core.item import Item
from platformcode import config, logger

host = "https://raw.githubusercontent.com/Intel11/prueba/master/mariachi.html"

def mainlist(item):
    logger.info()
    itemlist = []
    data = httptools.downloadpage(host).data
    logger.info("Intel11 %s" %data)
    patron  = '(?is)<span>([^<]+)'
    patron += '.*?<a href="([^"]+)'
    matches = scrapertools.find_multiple_matches(data, patron)
    for title, url in matches:
        itemlist.append(Item(action = "play",
                             channel = item.channel,
                             title = "El Mariachi - " + title,
                             url = url
                            ))
    itemlist = servertools.get_servers_itemlist(itemlist)
    return itemlist
