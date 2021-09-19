from bs4 import BeautifulSoup
from collections import deque
from urllib.request import Request, urlopen
import re



def createTree(source, target = None, limite=100000):
    """
    Create the tree of the links
    @param source: site source
    @param target: site vers lequel on veut aller
    @param profondeur: profondeur de l'arbre
    @return: on renvoie un chemin vers le lien
    On effectue donc un BFS pour trouver le chemin le plus rapide 
    (on considère que passer d'un lien à un autre prend un temps constant)
    """

    afaire = deque()
    afaire.appendleft(source) # On insère la source

    vues = set() # Conserve les site vus
    vues.add(source)

    pred = dict() # Permet de reconstituer le chemin à l'aide des prédecesseurs
    pred[source] = None

    found = False


    while afaire and not found:
        page = afaire.pop()
        # On a récupéré la page
        print(page, len(vues))

        if len(vues) > limite:
            break
        
        for link in getLinksOfWikiPage(page): # On récupère les autres pages
            if link not in vues: # Si l'on a jamais vu le lien
                afaire.appendleft(link)
                pred[link] = page
                vues.add(link)
                if link == target:
                    found = True
                    break

    # On extraie le chemin
    if found :
        path = []
        page = target
        while page is not None:
            path.append(page)
            page = pred[page]
        return path[::-1]
    return None



def getLinksOfWikiPage(page):
    req = Request(page)
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")
    links = []
    prefix = "https://en.wikipedia.org"

    for link in soup.findAll("a"):
        href = link.get("href")
        if isinstance(href, str): # Chaîne de cara
            if re.match(r'/wiki', href) and href.count(":") == 0: # Commence par wiki
                links.append(prefix + href)
    return links

if __name__ == "__main__":
    src = "https://en.wikipedia.org/wiki/Groucho_Marx"
    trg = "https://en.wikipedia.org/wiki/Entergy"
    # print(getLinksOfWikiPage(page1))
    print()
    for i,page in enumerate(createTree(src, trg)) :
        print(f"{i}\t{page.split('/')[-1]}")
