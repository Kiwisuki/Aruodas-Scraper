from src.driver import SmartDriver

LIST_OF_URLS = [
    'https://www.aruodas.lt/butai-vilniuje-zirmunuose-verkiu-g-parduodamas-labai-sviesus-i-vidini-kiema-1-3365530/',
    'https://www.aruodas.lt/patalpos-kaune-zaliakalnyje-zemaiciu-g-specialus-pasiulymas-dabar-isigijus-verslo-3-327961/',
    'https://www.aruodas.lt/butai-vilniuje-zirmunuose-verkiu-g-parduodamas-labai-sviesus-i-vidini-kiema-1-3365530/',
    'https://www.aruodas.lt/patalpos-kaune-zaliakalnyje-zemaiciu-g-specialus-pasiulymas-dabar-isigijus-verslo-3-327961/',
    'https://www.aruodas.lt/butai-vilniuje-zirmunuose-verkiu-g-parduodamas-labai-sviesus-i-vidini-kiema-1-3365530/',
    'https://www.aruodas.lt/patalpos-kaune-zaliakalnyje-zemaiciu-g-specialus-pasiulymas-dabar-isigijus-verslo-3-327961/',
    'https://www.aruodas.lt/butai-vilniuje-zirmunuose-verkiu-g-parduodamas-labai-sviesus-i-vidini-kiema-1-3365530/',
    'https://www.aruodas.lt/patalpos-kaune-zaliakalnyje-zemaiciu-g-specialus-pasiulymas-dabar-isigijus-verslo-3-327961/',
    'https://www.aruodas.lt/butai-vilniuje-zirmunuose-verkiu-g-parduodamas-labai-sviesus-i-vidini-kiema-1-3365530/',
    'https://www.aruodas.lt/patalpos-kaune-zaliakalnyje-zemaiciu-g-specialus-pasiulymas-dabar-isigijus-verslo-3-327961/',
]
if __name__ == '__main__':
    driver = SmartDriver(refresh_rate=2)
    for url in LIST_OF_URLS:
        driver.get_html(url)
