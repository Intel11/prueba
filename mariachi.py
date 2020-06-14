# -*- coding: utf-8 -*-

import codecs
from core import httptools
from core import tmdb
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
        episode = scrapertools.find_single_match(title, 'tulo (\w+)')
        itemlist.append(Item(action = "play",
                             channel = item.channel,
                             infoLabels = {"season": 1, "episode":episode},
                             contentSerieName = "El Mariachi",
                             title = "El Mariachi - " + title,
                             url = url
                            ))
    tmdb.set_infoLabels(itemlist)
    itemlist = servertools.get_servers_itemlist(itemlist)
    scrapertools.printMatches(itemlist)
    return itemlist
