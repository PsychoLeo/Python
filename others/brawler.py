print("Nous allons te faire découvrir le brawler qui te correspond le mieux. A chaque question, plusieurs choix seront proposés, choisis celui qui te parait le plus adapté à toi et inscrit ta réponse comme indiqué, sans oublier de valider ton choix !")
a=int(input("1e question : Préfères-tu les brawlers attaquant de proche, d'une distance intermédiare ou de loin ? Ecris 1 pour la 1e réponse, 2 pour la 2e et 3 pour la 3e : "))
b=int(input("2e question : Préfères-tu les supers défensives, polyvalentes ou offensives ? Ecris 1 pour la première réponse, 2 pour la deuxième et 3 pour la troisième : "))
c=int(input("3e question : Préfères-tu les dégâts de zone ou les dégâts individuels ? Ecris 1 pour la première réponse ou 2 pour la deuxième : "))
if a==1:
    if b==1:
        if c==1:
            print("Tu es quelqu'un d'offensivement modéré, qui sait sasir la bonne occasion dans des combats rapprochés et lors de mélês, le brawler te correspondant est Rosa.")
        if c==2:
            print("Tu sais attaquer et reculer, cibler une personne et saisir ta chance face à lui lorsqu'elle se présente, ton brawler fétiche est Mortis.")
    if b==2:
        if c==1:
            print("Avec un caractère assez offensif, tu sais profiter des combats rapprochés en gardant cependant tes distances avec les adversaires, ton caractère correspond à Nita.")
        if c==2:
            print("Tu es un chasseur de prime, qui prend en chasse un brawler mais qui sait tout de même prendre la fuite, tu correspond à Darryl et Bull.")
    if b==3:
        if c==1:
            print("Tu es fort et aimes attaquer tes adversaires plusieurs à la fois, ton caractère correspond à Bibi, Franck et Primo.")
        if c==2:
            print("Meilleur de proche, tu peux cependant battre tes adversaires grâce à ton offensivité persuasive, le brawler te correspondant est Shelly.")
if a==2:
    if b==1:
        if c==1:
            print("Offensivement modéré, tu sais garder tes distances et te protéger grâce à ta super défensive, tu correspond donc à Poco.")
        if c==2:
            print("Très défensif, tu saurais sans problème gérer un problème au corps à corps et te sortir de situations délicates, ton brawler fétiche est Pam.")
    if b==2:
        if c==1:
            print("Assez polyvalent, tu aimes modérer ton caractère dans l'arène, et sais te défendre aussi bien qu'attaquer, tes brawlers correspondants sont Dynamike et Carl.")
        if c==2:
            print("Tu es rapide, furtif, polyvalent, redoutable en arène, chacun a peur de ta force de surprise, ton caractère correspond à Léon.")
    if b==3:
        if c==1:
            print("Les autres brawlers peuvent te redouter, tu es offensif et potentiellement dangereux à chaque distance et endroit, tu correspond à Barley et Tara.")
        if c==2:
            print("Tu es dangereux offensivement et chacun lors du combat peut avoir peur de toi et ta super, tes brawlers fétiches sont Crow, Gene et Max.")
if a==3:
    if b==1:
        if c==1:
            print("Les combats de loin sont tes point forts, ainsi que les mêlées, tu es polyvalent car tu sais te défendre, ton caractère correspond aux brawlers Bow et Tick.")
        if c==2:
            print("Tu peux faire des dégâts considérables aux adversaires qui t'approchent, et fuir pour pouvoir exprimer ta puissance aux autres, tu corresponds à Piper et Rico.")
    if b==2:
        if c==1:
            print("Ta super polyvalente te permet de t'exprimer dans l'arène, en plus d'être dangereux de loin, ton brawler correspondant est Penny.")
        if c==2:
            print("Tout le monde te considère comme les meilleurs brawlers du jeu, tu es polyvalent au combat et peut attaquer tes adversaires de loin, tu correspond à Jessie et Spike.")
    if b==3:
        if c==1:
            print("Tu gardes tes distances, mais malgré cela tu aimes le combat et l'action, qualité que tu renforces avec tes degâts groupés, ton brawler fétiche est Brock.")
        if c==2:
            print("Ton offensivité et tes armes font de toi un combattant agile et efficace, tu correspond le plus fortement à Colt et Bea.")
        
            
            
            
