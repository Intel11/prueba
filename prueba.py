# -*- coding: utf-8 -*-
# version 0.0.5
# https://mundovideoshd.com/el-mariachi-capitulos/
# https://notytech.com/2017/08/12/addons-kodi-alfa-vs-mitvspain-sucesor-pelisalacarta/

import base64

from core import httptools
from core import scrapertools
from core import scrapertoolsV2
from core import servertools
from core.item import Item
from lib.pyaes import openssl_aes
from lib import jsunpack
from platformcode import config,logger,platformtools

_useragent = "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3163.100 Safari/537.36"


def mainlist(item):
    logger.info()
    itemlist = list()
    itemlist.append(Item(channel=item.channel, title = "[COLOR green]Perú[/COLOR]", text_bold = True))
    itemlist.append(Item(channel=item.channel, action = "canal2",   title ="  Frecuencia Latina"))
    itemlist.append(Item(channel=item.channel, action = "canal4",   title ="  América TV"))
    itemlist.append(Item(channel=item.channel, action = "canal5",   title ="  Panamericana Televisión"))
    itemlist.append(Item(channel=item.channel, action = "canal5_2", title ="  Panamericana Televisión Op2"))
    itemlist.append(Item(channel=item.channel, action = "canal7_hd",title ="  TV Perú HD"))
    itemlist.append(Item(channel=item.channel, action = "canal7_73",title ="  TV Perú 7.3"))
    itemlist.append(Item(channel=item.channel, action = "canaln",   title ="  Canal N"))
    itemlist.append(Item(channel=item.channel, action = "canal9",   title ="  ATV"))
    itemlist.append(Item(channel=item.channel))
    itemlist.append(Item(channel=item.channel, title = "[COLOR green]Argentina[/COLOR]", text_bold = True))
    itemlist.append(Item(channel=item.channel, action = "canala1",      title ="  América TV"))
    itemlist.append(Item(channel=item.channel, action = "canala9",      title ="  Canal 9"))
    itemlist.append(Item(channel=item.channel, action = "canalatelefe", title ="  Telefe"))
    itemlist.append(Item(channel=item.channel, action = "canala26",     title ="  Canal 26"))
    itemlist.append(Item(channel=item.channel))
    itemlist.append(Item(channel=item.channel, title = "[COLOR green]Deportes[/COLOR]", text_bold = True))
    itemlist.append(Item(channel=item.channel, action = "canalespnmas",    title ="  ESPN+ HD"))
    itemlist.append(Item(channel=item.channel, action = "canalespn1",      title ="  ESPN 1 HD"))
    itemlist.append(Item(channel=item.channel, action = "canalespn2",      title ="  ESPN 2 HD"))
    itemlist.append(Item(channel=item.channel, action = "canalespn3",      title ="  ESPN 3 HD"))
    itemlist.append(Item(channel=item.channel, action = "canalfox_sport1", title ="  Fox Sport 1"))
    itemlist.append(Item(channel=item.channel, action = "canalfoxsporthd", title ="  Fox Sport 1 HD"))
    itemlist.append(Item(channel=item.channel, action = "canalfoxsport2",  title ="  Fox Sport 2 HD"))
    itemlist.append(Item(channel=item.channel, action = "canalfoxsport3",  title ="  Fox Sport 3 HD"))
    #itemlist.append(Item(channel=item.channel, action = "canalroja",       title ="  Roja directa"))
    itemlist.append(Item(channel=item.channel, action = "canalf1_1",       title ="  Formula 1"))
    itemlist.append(Item(channel=item.channel, action = "canalf1_2",       title ="  Formula 1 Op2"))
    itemlist.append(Item(channel=item.channel, action = "canaltoros",      title ="  Toros"))
    itemlist.append(Item(channel=item.channel, action = "canaltoros2",     title ="  Toros Op2"))
    itemlist.append(Item(channel=item.channel))
    itemlist.append(Item(channel=item.channel, title = "[COLOR green]Internacional[/COLOR]", text_bold = True))
    itemlist.append(Item(channel=item.channel, action = "canalantena3_1",   title = "  Antena 3"))
    itemlist.append(Item(channel=item.channel, action = "canalantena3_2",   title = "  Antena 3 Op2"))
    itemlist.append(Item(channel=item.channel, action = "canalhistory",     title = "  History Channel - Castellano"))
    itemlist.append(Item(channel=item.channel, action = "canalhistory2",    title = "  History Channel - Latino", HD=False))
    itemlist.append(Item(channel=item.channel, action = "canalhistory2",    title = "  History Channel HD- Latino", HD=True))
    itemlist.append(Item(channel=item.channel, action = "canaldiscovery",   title = "  Discovery Channel - Latino"))
    itemlist.append(Item(channel=item.channel, action = "canaldiscoveryhd", title = "  Discovery Channel - Latino HD"))
    itemlist.append(Item(channel=item.channel, action = "canalnatgeo",      title = "  National Geographic - HD"))
    itemlist.append(Item(channel=item.channel, action = "canalfox",         title = "  Fox - Latino", res = "832x468"))
    itemlist.append(Item(channel=item.channel, action = "canalfox",         title = "  Fox - Latino HD"))
    itemlist.append(Item(channel=item.channel, action = "canalhh",          title = "  H&H Discovery HD"))
    itemlist.append(Item(channel=item.channel, action = "canale",           title = "  E!"))
    itemlist.append(Item(channel=item.channel, action = "canalhbo",         title = "  HBO - HD"))
    itemlist.append(Item(channel=item.channel))
    itemlist.append(Item(channel=item.channel, title = "[COLOR green]Infantiles[/COLOR]", text_bold = True))
    itemlist.append(Item(channel=item.channel, action = "canalcartoon",    title = "  Cartoon Network - HD"))
    itemlist.append(Item(channel=item.channel, action = "canaldiscoveryk", title = "  Discovery Kids - HD"))
    itemlist.append(Item(channel=item.channel, action = "canaldisney",     title = "  Disney Channel - HD"))
    itemlist.append(Item(channel=item.channel, action = "canaldisneyxd",   title = "  Disney XD"))
    itemlist.append(Item(channel=item.channel, action = "canalnick",       title = "  Nick - HD"))
    itemlist.append(Item(channel=item.channel, action = "canalnicktoons",  title = "  Nicktoons"))
    itemlist.append(Item(channel=item.channel, action = "canaltooncast",   title = "  Tooncast"))
    return itemlist


def canalroja(item):
    logger.info()
    url_source = "http://www.tutv-gratis.com/2017/11/roja-directa-tv-en-vivo.html"
    item.url = server_telerium("http://tutv-gratishd.blogspot.com/2017/11/roja-directa.html")
    platformtools.play_video(item)


def canalhbo(item):
    logger.info()
    url_source = "http://latino-webtv.com/HBO-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/hbo.html", res = item.res)
    platformtools.play_video(item)


def canaltooncast(item):
    logger.info()
    url_source = "http://latino-webtv.com/Tooncast-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/tooncast.html", res = item.res)
    platformtools.play_video(item)


def canalnicktoons(item):
    logger.info()
    url_source = "http://latino-webtv.com/Nicktoons-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/nicktoons.html", res = item.res)
    platformtools.play_video(item)


def canaldisneyxd(item):
    logger.info()
    url_source = "http://latino-webtv.com/Disney-XD-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/disneyxd.html", res = item.res)
    platformtools.play_video(item)


def canalnick(item):
    logger.info()
    url_source = "http://latino-webtv.com/Nick-HD-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/nick.html", res = item.res)
    platformtools.play_video(item)


def canalcartoon(item):
    logger.info()
    url_source = "http://latino-webtv.com/Cartoon-Network-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/cartoon.html", res = item.res)
    platformtools.play_video(item)


def canalnatgeo(item):
    logger.info()
    url_source = "http://latino-webtv.com/Nat-Geo-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/natgeo.html", res = item.res)
    platformtools.play_video(item)


def canaldisney(item):
    logger.info()
    url_source = "http://www.fulltelevisionhd.net/2014/09/disney-channel-en-vivo-por-internet.html"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/disneych.html", res = item.res)
    platformtools.play_video(item)


def canaln(item):
    logger.info()
    url_source = "http://www.fulltelevisionhd.net/2013/02/canal-n-en-vivo-por-internet.html"
    item.url = server_playerfs("http://www.fulltvhd.fi/peru/canaln.php")
    platformtools.play_video(item)


def canalfoxsport2(item):
    logger.info()
    url_source = "http://latino-webtv.com/Fox-Sports-2-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/foxsports2.html", res = item.res)
    platformtools.play_video(item)


def canalfoxsport3(item):
    logger.info()
    url_source = "http://latino-webtv.com/Fox-Sports-3-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/Fox-Sports-3.html", res = item.res)
    platformtools.play_video(item)


def canalespn1(item):
    logger.info()
    url_source = "http://latino-webtv.com/ESPN-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/espn.html", res = item.res)
    platformtools.play_video(item)


def canalfoxsporthd(item):
    logger.info()
    url_source = "http://latino-webtv.com/Fox-Sports-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/foxsports.html", res = item.res)
    platformtools.play_video(item)


def canalespn2(item):
    logger.info()
    url_source = "http://latino-webtv.com/ESPN-2-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/espn2.html", res = item.res)
    platformtools.play_video(item)


def canalespn3(item):
    logger.info()
    url_source = "http://latino-webtv.com/ESPN-3-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/espn3.html", res = item.res)
    platformtools.play_video(item)


def canalespnmas(item):
    logger.info()
    url_source = "http://latino-webtv.com/ESPN-Plus-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/espn_plus.html", res = item.res)
    platformtools.play_video(item)


def canaltoros2(item):
    logger.info()
    url_source = "http://latelete.tv/canal-plus-toros-en-directo-gratis-por-internet/"
    url_channel = "http://verdirectotv.com/tv/digitales2/plustoros.html"
    data = httptools.downloadpage(url_channel).data
    url = scrapertools.find_single_match(data, '<iframe scrolling.*?src="([^"]+)')
    headers = [
    ["Referer", url_channel],
    ["host", scrapertoolsV2.get_domain_from_url(url)],
    ]
    data = httptools.downloadpage(url, headers = headers).data
    url = scrapertools.find_single_match(data, "source: '([^']+)")
    host = scrapertoolsV2.get_domain_from_url(url)
    item.url  = url + "|Referer=%s" %url
    item.url += "&Host=%s" %host
    item.url += "&User-Agent=%s" %_useragent
    platformtools.play_video(item)


def canaldiscoveryk(item):
    logger.info()
    url_source = "http://latino-webtv.com/Discovery-Kids-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/discoveryk.html", res = item.res)
    platformtools.play_video(item)


def canale(item):
    logger.info()
    url_source = "http://latino-webtv.com/E-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/e.html", res = item.res)
    platformtools.play_video(item)


def canalfox(item):
    logger.info()
    url_source = "http://latino-webtv.com/FOX-en-vivo/"
    item.url = provider_lw("http://embed.latino-webtv.com/channels/fox.html", res = item.res)
    platformtools.play_video(item)


def canaldiscoveryhd(item):
    logger.info()
    item.url = provider_lw("http://embed.latino-webtv.com/channels/discovery.html", res = item.res)
    platformtools.play_video(item)


def canaldiscovery(item):
    logger.info()
    item.url = server_playerfs("http://tvpor-internet.com/discovery-latino-en-vivo.html")
    platformtools.play_video(item)


def canalhh(item):
    logger.info()
    item.url = provider_lw("http://embed.latino-webtv.com/channels/homeandhealt.html", res = item.res)
    platformtools.play_video(item)


def canalhistory2(item):
    logger.info()
    url_source = "http://www.tutv-gratis.com"
    url_channel = "http://www.tv-en-vivo.org/history/"
    data = httptools.downloadpage(url_channel).data
    url = scrapertools.find_single_match(data, 'source: "([^"]+)"')
    host = scrapertoolsV2.get_domain_from_url(url)
    if item.HD==True:
        quality='05'
    else:
        quality='02'
    url = url.replace("index.m3u8","Stream(%s)/index.m3u8" % quality)
    item.url  = url + "|Referer=%s" %url
    item.url += "&Host=%s" %host
    item.url += "&User-Agent=%s" %_useragent
    headers = [
    ["Referer", url],
    ["Host", host]
    ]
    platformtools.play_video(item)


def canalantena3_2(item):
    logger.info()
    item.url = "http://a3live-lh.akamaihd.net/i/antena3_1@35248/index_2_av-b.m3u8?sd=10&rebase=on"
    platformtools.play_video(item)


def canalantena3_1(item):
    logger.info()
    item.url = provider_verplusonline("http://verplusonline.com/ver-antena-3-hd-en-directo-y-online-las-24h-en-vivo/")
    platformtools.play_video(item)


def canalfox_sport1(item):
    logger.info()
    item.url = provider_verplusonline("http://verplusonline.com/ver-fox-sport-online/")
    platformtools.play_video(item)


def canaltoros(item):
    logger.info()
    item.url = provider_verplusonline("http://verplusonline.com/toros-tv-online-24h/")
    platformtools.play_video(item)


def canalf1_1(item):
    logger.info()
    #item.url = provider_verplusonline("http://verplusonline.com/ver-movistar-f1-online/")
    item.url = provider_verplusonline("http://verbeinlaliga.com/movistar-formula-uno/")
    platformtools.play_video(item)
    

def canalf1_2(item):
    logger.info()
    #item.url = provider_vercanalestv("http://www.vercanalestv.com/ver-formula-1-en-directo-y-online-gratis/")
    item.url = server_telerium("http://vertelevision.tv/tv/deportes/formula1.php")
    platformtools.play_video(item)


def canalatelefe(item):
    logger.info()
    url_channel = "http://www.televisionparatodos.tv/telefe-reproductor/"
    data = httptools.downloadpage(url_channel).data
    item.url = scrapertools.find_single_match(data, '<source src="([^"]+)')
    platformtools.play_video(item)


def canala9(item):
    logger.info()
    url_channel = "http://www.televisionparatodos.tv/canal-9-player/"
    data = httptools.downloadpage(url_channel).data
    item.url = scrapertools.find_single_match(data, '<iframe id=.*?src="([^"]+)')
    data = httptools.downloadpage(item.url).data
    item.url = scrapertools.find_single_match(data, "file: '([^']+)")
    referer = item.url
    host = scrapertoolsV2.get_domain_from_url(item.url)
    item.url += "|Referer=%s" %referer
    item.url += "&Host=%s" %host
    platformtools.play_video(item)


def canala26(item):
    logger.info()
    url_channel = "http://television-internet.com.ar/canal-26.html"
    item.url = "http://live-edge01.telecentro.net.ar/live/smil:c26.smil/master.m3u8"
    platformtools.play_video(item)


def canala1(item):
    logger.info()
    url_channel = "http://television-internet.com.ar/america-tv.html"
    data = httptools.downloadpage(url_channel).data
    url_stream = scrapertools.find_single_match(data, '<iframe id.*?src="([^"]+)')
    data = httptools.downloadpage(url_stream).data
    url_stream = scrapertools.find_single_match(data, '<iframe src="([^"]+)')
    data = httptools.downloadpage(url_stream).data
    encode = scrapertools.find_single_match(data, 'atob\("([^"]+)"')
    decode = base64.b64decode(encode)
    item.url = scrapertools.find_single_match(decode, 'appPlaylist":"([^"]+)"')
    item.url += "|Referer=%s" %url_stream
    platformtools.play_video(item)

    
def canal2(item):
    logger.info()
    #url_source = "http://visionperuanatv.com/2013/03/frecuencia-latina-en-vivo.html"
    url_source = "http://www.fulltelevisionhd.net/2013/02/frecuencia-latina-en-vivo-por-internet.html"
    #item.url = server_pxstream("http://canalesenvivo.ucoz.com/Frecuencia_Latina.html")
    item.url = server_playerfs("http://fulltvhd.fi/peru/latina.php")
    platformtools.play_video(item)


def canal4(item):
    logger.info()
    #url_source = "http://visionperuanatv.com/2013/03/frecuencia-latina-en-vivo.html"
    # item.url = server_playerfs("http://tvenvivo.online/americatreve.php")
    # if not item.url:
        # item.url = server_pxstream("http://tvenvivo.online/americatreve.php")
    url_source = "http://www.fulltelevisionhd.li/america-television-en-vivo-por-internet/"
    item.url = server_playerfs("http://www.fulltvhd.fi/peru/america.php")
    platformtools.play_video(item)


def canal5(item):
    logger.info()
    data = httptools.downloadpage("https://panamericana.pe/tvenvivo/hd").data
    item.url = server_iblubs(scrapertools.find_single_match(data, '<iframe src="([^"]+)'))
    platformtools.play_video(item)

def canal5_2(item):
    logger.info()
    data = httptools.downloadpage("https://panamericana.pe/tvenvivo/sd").data
    item.url = scrapertools.find_single_match(data, '<iframe frameborder.*?src="([^"]+)')
    item.server = "dailymotion"
    platformtools.play_video(item)


def canal7_73(item):
    logger.info()
    item.url = server_iblubs("http://iblups.com/e_tvperu73")
    platformtools.play_video(item)


def canal7_hd(item):
    logger.info()
    item.url = server_iblubs("http://iblups.com/e_tvperuhd")
    platformtools.play_video(item)


def canal9(item):
    logger.info()
    url_channel = "http://tele-on.com/atv_en_vivo.html"
    data = httptools.downloadpage(url_channel).data
    item.url = scrapertools.find_single_match(data, '<video id="player".*?src="([^"]+)"')
    referer = scrapertools.find_single_match(data, '<iframe f.*?src="([^"]+)"')
    host = scrapertoolsV2.get_domain_from_url(item.url)
    item.url += "|Referer=%s" %referer
    item.url += "&Host=%s" %host
    platformtools.play_video(item)


def canalhistory(item):
    logger.info()
    item.url = provider_vercanalestv("http://www.vercanalestv.com/ver-canal-historia-en-directo-y-gratis-en-vivo/")
    platformtools.play_video(item)


### PROVEEDORES
def provider_lw(url_channel, res):
    # RESOLUCION POR DEFECTO: HD
    if not res:
        res = "1280x720"
    headers = [
    ["Referer", url_channel]
    ]
    uu1 = httptools.downloadpage(url_channel, follow_redirects=False, only_headers=True, headers=headers).headers.get("location", "")
    uu = httptools.downloadpage(uu1, headers = headers).data
    url = "http://" + scrapertoolsV2.get_domain_from_url(uu1) + "/" + scrapertools.find_single_match(uu, 'location = "([^"]+)')
    if url == "http://" or url == "http://tv.jaffmisshwedd.com/":
        data = httptools.downloadpage(url_channel, headers = headers).data
    else:
        data = httptools.downloadpage(url, headers = headers).data
    headers = {'Referer':url}
    data_c = httptools.downloadpage("http://tv.jaffmisshwedd.com/config-player.js", headers = headers).data
    key = scrapertools.find_single_match(data_c, "decode','slice','([^']+)")
    mm = scrapertools.find_single_match(data, 'MarioCSdecrypt.dec\("(.*?)"\)')
    if mm:
        OpenSSL_AES = openssl_aes.AESCipher()
        url1 = OpenSSL_AES.decrypt(mm, key)
        dd = httptools.downloadpage(url1, headers = headers).data
        url_f = scrapertools.find_single_match(dd, "(?s)%s.*?(http.*?)#" %res).strip()
        if url_f == "":
            url_f = url1
    else:
        id = scrapertools.find_single_match(data, "<script type='text/javascript'> width.*?id='([^']+)'")
        url = "https://player.limpi.tv/embed/%s" %id
        data1 = httptools.downloadpage(url, headers=headers).data
        loadbalance = httptools.downloadpage("https://www.limpi.tv/loadbalance").data
        loadbalance = loadbalance.replace("\n","")
        url_f = scrapertools.find_single_match(data1, '"file": "([^,]+)')
        url_f = url_f.replace('" + loadbalance + "',loadbalance).replace('"','')
    url_f += "|User-Agent=%s" %_useragent
    url_f += "&Referer=%s" %url
    return url_f


def provider_vercanalestv(url_channel):
    logger.info()
    data = httptools.downloadpage(url_channel).data
    urlx = scrapertools.find_single_match(data, '<iframe scrolling="no".*?src="([^"]+)"')
    if not urlx.startswith("http"):
        urlx = "http://www.vercanalestv.com" + urlx
    headers = [
    ["Referer", urlx]
    ]
    data = httptools.downloadpage(urlx, headers = headers).data
    url = scrapertools.find_single_match(data, '<a href="([^"]+)"')
    url1 = "http://" + scrapertoolsV2.get_domain_from_url(url_channel) + url
    headers1 = [
    ["Referer", url1],
    ["Host", scrapertoolsV2.get_domain_from_url(url_channel)]
    ]
    if "javascript" in url:
        url = scrapertools.find_single_match(data, '<iframe scrolling.*?src="([^"]+)"')
        if "vergol" in url:
            url1 = url
            headers1 = [
            ["Referer", urlx],
            ["Host", scrapertoolsV2.get_domain_from_url(url1)]
            ]
        else:
            data = httptools.downloadpage(url).data
            url1 = scrapertools.find_single_match(data, '<iframe scrolling.*?src="([^"]+)"')
            headers1 = []
    data = httptools.downloadpage(url1, headers = headers1).data
    patron = "source: '([^']+)'"
    url = scrapertools.find_single_match(data, "source: '([^']+)'")
    if url == "":
        url = scrapertools.find_single_match(data, '<iframe scrolling.*?src="([^"]+)"')
        headers2 = [
        ["Referer", url1],
        ["Host", scrapertoolsV2.get_domain_from_url(url)]
        ]
        data = httptools.downloadpage(url, headers = headers2).data
    url = scrapertools.find_single_match(data, patron)
    host = scrapertoolsV2.get_domain_from_url(url)
    url += "|Referer=%s" %url
    url += "&Host=%s" %host
    url += "&User-Agent=%s" %_useragent
    return url


def provider_verplusonline(url_channel):
    logger.info()
    data = httptools.downloadpage(url_channel).data
    urlx = scrapertools.find_single_match(data, '<iframe.*?src="([^"]+)"')
    headers = [
    ["Referer", url_channel]
    ]
    if not urlx.startswith("http"):
        urlx = "http:" + urlx
    data = httptools.downloadpage(urlx, headers = headers).data
    bloque = scrapertools.find_single_match(data, "<script type='text.*?src=.*?</script>")
    if bloque:
        url    = scrapertools.find_single_match(bloque, "src='([^']+)")
        file   = scrapertools.find_single_match(bloque, "file='([^']+)")
        height = scrapertools.find_single_match(bloque, "height='([^']+)")
        width  = scrapertools.find_single_match(bloque, "width='([^']+)")
        data = httptools.downloadpage(url).data
        url  = scrapertools.find_single_match(data, "src=(.*?)>")
        url = url.replace("'+file+'",file).replace("'+width+'",width).replace("'+height+'",height)
        data = httptools.downloadpage(url).data
    else:
        url = scrapertools.find_single_match(data, '<iframe scrolling.*?src="([^"]+)')
        headers = [
        ["Referer", urlx]
        ]
        data = httptools.downloadpage(url, headers = headers).data
    url = scrapertools.find_single_match(data, "source: '([^']+)'")
    url += "|User-Agent=%s "%_useragent
    return url


### SERVERS

def server_iblubs(url_channel):
    logger.info()
    url = url_channel
    headers = [
    ["Referer", url_channel]
    ]
    if "hls" not in url_channel:
        data = httptools.downloadpage(url_channel, headers = headers).data
        url = scrapertools.find_single_match(data, 'file: "(http[^"]+)"')
    url += "|User-Agent=%s" %_useragent
    return url


def server_pxstream(url_channel):
    logger.info()
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
    hh = scrapertoolsV2.get_domain_from_url(url)
    url = url + "|Referer=%s&Host=%s" %(url_stream, hh)
    url = url.replace("playlist","chunks")
    url += "&User-Agent=%s" %_useragent
    return url


def server_playerfs(url_channel):
    #playerfs / ucaster / janjuaplayer / zony
    logger.info()
    data    = httptools.downloadpage(url_channel).data
    bloque  = scrapertools.find_single_match(data,   "<script type='text.*?src='.*?'")
    width   = scrapertools.find_single_match(bloque, 'width=(\w+)')
    height  = scrapertools.find_single_match(bloque, 'height=(\w+)')
    channel = scrapertools.find_single_match(bloque, "channel='(\w+)'")
    g       = scrapertools.find_single_match(bloque, "g='(\w+)'")
    xserver = scrapertools.find_single_match(bloque, "src='([^']+)'")
    data    = httptools.downloadpage(xserver).data
    h_stream = scrapertools.find_single_match(data, "<iframe.*?src=(.*?height\+')")
    h_stream = h_stream.replace("'+embedded+'","membedplayer").replace("'+channel+'",channel).replace("'+g+'",g).replace("'+width+'",width).replace("'+height+'",height)
    headers = [
    ["Referer", url_channel]
    ]
    data = httptools.downloadpage(h_stream, headers=headers).data
    h_loadbalancer = scrapertools.find_single_match(data, 'url: "([^"]+)')
    try:
        ip_balancer = httptools.downloadpage(h_loadbalancer).data.split('=')[1]
    except:
        return ""
    url = scrapertools.find_single_match(data, '"src", "([^\)]+)')
    if "ucaster" in xserver:
        url1 = scrapertools.find_single_match(data, 'hlsUrl = "([^;]+)')
        pk = scrapertools.find_single_match(data, 'hlsUrl = hlsUrl \+ \("([^")]+)"')
        if pk != "":
            url = url1 + pk
    url = url.replace('" + ea + "', ip_balancer).replace('"',"")
    return url
    

def server_whostreams(url_channel):
    logger.info()
    data = httptools.downloadpage(url_channel).data
    url_stream = scrapertools.find_single_match(data, '<iframe src="([^"]+)"')
    headers = [
    ["Referer", url_channel],
    ["Host", "whostreams.net"]
    ]
    data = httptools.downloadpage(url_stream, headers=headers).data
    pack = scrapertools.find_single_match(data, "p,a,c,k,e,d\)(.*)</script")
    unpack = jsunpack.unpack(pack)
    url = scrapertools.find_single_match(unpack, 'file:"([^"]+)')
    url += "|User-Agent=%s" %_useragent
    return url


def server_telerium(url_channel):
    logger.info()
    data = httptools.downloadpage(url_channel).data
    logger.info("Intel55 %s" %data)
    url_stream = scrapertools.find_single_match(data, '<iframe.*?src="([^"]+)"')
    url_stream = "https://telerium.tv/embed/25812.html"
    headers = [
    ["Referer", url_stream],
    ["Host", "telerium.tv"]
    ]
    data = httptools.downloadpage(url_stream, headers=headers).data
    logger.info("Intel11 %s" %data)
    pack = scrapertools.find_single_match(data, "p,a,c,k,e,d\)(.*)</script")
    unpack = jsunpack.unpack(pack)
    logger.info("Intel22 %s" %pack)
    logger.info("Intel33 %s" %unpack)
    url = scrapertools.find_single_match(unpack, 'file:"([^"]+)')
    url += "|User-Agent=%s" %_useragent
    return url
