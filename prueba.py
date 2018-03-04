# -*- coding: utf-8 -*-
# version 0.0.2

import base64

from core import httptools
from core import scrapertools
from core import servertools
from core.item import Item
from platformcode import config,logger,platformtools


def mainlist(item):
    logger.info()
    itemlist = list()
    itemlist.append(Item(channel=item.channel, title = "Perú", text_bold = True))
    itemlist.append(Item(channel=item.channel, action = "canal2", title ="  Frecuencia Latina"))
    itemlist.append(Item(channel=item.channel, action = "canal4", title ="  América TV"))
    itemlist.append(Item(channel=item.channel, action = "canal5", title ="  Panamericana Televisión"))
    itemlist.append(Item(channel=item.channel, action = "canal7", title ="  TV Perú"))
    itemlist.append(Item(channel=item.channel, action = "canal9", title ="  ATV"))
    itemlist.append(Item(channel=item.channel))
    itemlist.append(Item(channel=item.channel, title = "Argentina", text_bold = True))
    itemlist.append(Item(channel=item.channel, action = "canala1", title ="  América TV"))
    itemlist.append(Item(channel=item.channel, action = "canala26", title ="  Canal 26"))
    itemlist.append(Item(channel=item.channel, action = "canala9", title ="  Canal 9"))
    itemlist.append(Item(channel=item.channel, action = "canalatelefe", title ="  Telefe"))
    return itemlist


def canalatelefe(item):
    logger.info()
    itemlist = []
    url_channel = "http://www.televisionparatodos.tv/telefe-reproductor/"
    data = httptools.downloadpage(url_channel).data
    item.url = scrapertools.find_single_match(data, '<source src="([^"]+)')
    platformtools.play_video(item)


def canala9(item):
    logger.info()
    itemlist = []
    url_channel = "http://www.televisionparatodos.tv/canal-9-player/"
    data = httptools.downloadpage(url_channel).data
    item.url = scrapertools.find_single_match(data, '<iframe id=.*?src="([^"]+)')
    data = httptools.downloadpage(item.url).data
    item.url = scrapertools.find_single_match(data, "file: '([^']+)")
    platformtools.play_video(item)


def canala26(item):
    logger.info()
    itemlist = []
    url_channel = "http://television-internet.com.ar/canal-26.html"
    item.url = "http://live-edge01.telecentro.net.ar/live/smil:c26.smil/master.m3u8"
    platformtools.play_video(item)


def canala1(item):
    logger.info()
    itemlist = []
    url_channel = "http://television-internet.com.ar/america-tv.html"
    data = httptools.downloadpage(url_channel).data
    url_stream = scrapertools.find_single_match(data, '<iframe id.*?src="([^"]+)')
    data = httptools.downloadpage(url_stream).data
    url_stream = scrapertools.find_single_match(data, '<iframe src="([^"]+)')
    data = httptools.downloadpage(url_stream).data
    encode = scrapertools.find_single_match(data, 'atob\("([^"]+)"')
    decode = base64.b64decode(encode)
    item.url = scrapertools.find_single_match(decode, 'appPlaylist":"([^"]+)"')
    item.url += "|Referer=%s" %url_stream #http://vmf.edge-apps.net/embed/live.php?streamname=americahls-100056&autoplay=true"
    platformtools.play_video(item)

    
def canal2(item):
    logger.info()
    itemlist = []
    url_channel = "http://canalesenvivo.ucoz.com/Frecuencia_Latina.html"
    data = httptools.downloadpage(url_channel).data
    url_stream = scrapertools.find_single_match(data, '<iframe src="([^"]+)"')
    headers = [
    ["Referer", url_channel]
    ]
    headers1 = [
    ["Referer", url_stream]
    ]
    data = httptools.downloadpage(url_stream, headers=headers).data
    url = scrapertools.find_single_match(data, 'var urlchannel = "([^"]+)"')
    url = httptools.downloadpage(url, follow_redirects=False, only_headers=True, headers=headers1).headers.get("location", "")
    hh = scrapertools.find_single_match(url, "http://(.*?)/load")
    item.url = url + "|Referer=%s&Host=%s" %(url_stream, hh)
    item.url = item.url.replace("playlist","chunks")
    platformtools.play_video(item)


def canal4(item):
    logger.info()
    itemlist = []
    url_channel = "http://tvenvivo.online/americatreve.php"
    data = httptools.downloadpage(url_channel).data
    bloque = scrapertools.find_single_match(data, "<script type='text.*?\</script>")
    width = scrapertools.find_single_match(bloque, 'width=(\w+)')
    height = scrapertools.find_single_match(bloque, 'height=(\w+)')
    channel = scrapertools.find_single_match(bloque, "channel='(\w+)'")
    g = scrapertools.find_single_match(bloque, "g='(\w+)'")
    headers = [
    ["Referer", url_channel]
    ]
    data = httptools.downloadpage("http://www.playerfs.com/membedplayer/%s/%s/%s/%s" %(channel, g, width, height), headers=headers).data
    ip_balancer = httptools.downloadpage("http://www.pubfstream.com:1935/loadbalancer").data.split('=')[1]
    url = scrapertools.find_single_match(data, '"src", "([^\)]+)')
    item.url = url.replace('" + ea + "', ip_balancer).replace('"',"")
    platformtools.play_video(item)


def canal5(item):
    logger.info()
    itemlist = []
    item.url = "http://cdnh4.iblups.com/hls/ptv2.m3u8"
    platformtools.play_video(item)


def canal7(item):
    logger.info()
    itemlist = []
    url_channel = "http://p.iblups.com/tvperu/embed.php"
    data = httptools.downloadpage(url_channel).data
    item.url = scrapertools.find_single_match(data, 'file: "(http[^"]+)"')
    platformtools.play_video(item)


def canal9(item):
    logger.info()
    itemlist = []
    url_channel = "http://tele-on.com/atv_en_vivo.html"
    data = httptools.downloadpage(url_channel).data
    item.url = scrapertools.find_single_match(data, '<video id="player".*?src="([^"]+)"')
    platformtools.play_video(item)
