import discord 
from datetime import datetime
from random import randint
from discord.ext import commands 
client = commands.Bot(command_prefix="$")

class Node :
    def __init__(self,question,keyword,list_child_node):
        self.question = question
        self.keyword = keyword
        self.list_child_node = list_child_node

    def user_response(self):
        print(self.question)
        txt = input()
        for child in self.list_child_node:
            if child.keyword in txt:
                child.user_response()

docu = [
    Node("Tu peut accéder à la convention de stage 2021/2022 ici : https://assets.jobteaser.com/upload_file/uploads/Convention_de_Stage_2022_-_fran%C3%A7ais.3417430645.pdf", "convention", []),
    Node("Ton emploi du temps se trouve sur l'hyperplanning : https://hetic-planning.oxymis.fr/hp/etudiant\n Si tu as oublié tes codes envoie un MP à Brontis (@ErwinTheCat#8778)", "emploi du temps", []),
]
administration = [
    Node("Frais de scolarité ! Que souhaite tu savoir?", "frais", [Node("Les frais de scolarités pour cette année s'élèvent à 7 500€, les deux prochaines années seront payé par votre entreprise où vous serez en alternance.", "montant", []), Node("Les modalitées de paiment sont indiquées sur ton contrat d'inscription, si tu souhaite plus d'information je t'invite à te raprocher au près de la compta : compta@hetic.com", "modalité", []), ]),
    Node("De quel document as-tu besoin ?", "document", docu)
]
stage = [
    Node("Du 4 juillet au 30 septembre 2022","date",[]),
    Node("Envoi un mp à Brontis (@ErwinTheCat) ou utilise $modo @ErwinTheCat, il saura comment t'aider.", "offre", []),
    Node("Envoi un mp à Giuseppe (@Giuseppe#) ou utilise $modo @Giuseppe, il saura comment t'aider.", "CV", []),
    Node("Bravo ! Envoi tout de suite un mp à Brontis (@ErwinTheCat) ou utilise $modo @ErwinTheCat pour lui annoncer la bonne nouvelle, il te dira comment s'y prendre pour la suite.","trouvé",[]),
    docu[0]
]
alternance = [
    Node("En 1ère année : 2 semaines entreprise / 1 semaine cours,\n 2eme année : 3 semaines entreprise / 1 semaine cours.","rythme",[]),
    Node("Début octobre 2022","date",[]),
    Node("Envoi un mp à Brontis (@ErwinTheCat) ou utilise $modo @ErwinTheCat , il saura comment t'aider","offre",[]),
    Node("Envoi un mp à Giuseppe (@Giuseppe) ou utilise $modo @Giuseppe, il saura comment t'aider","CV",[]),
    Node("Bravo ! Envoi tout de suite un mp à Brontis (@ErwinTheCat) ou utilise $modo @ErwinTheCat pour lui annoncer la bonne nouvelle, il te dira comment s'y prendre pour la suite.","trouvé",[]),
    docu[0]
]
programation = [
    Node("Je pense que tu parle de la création des bots ! Voici un tuto pour bien comprendre comment créer un bot sur discord : https://www.docstring.fr/blog/creer-un-bot-discord-avec-python/", "discord",[]),
    Node("Ah les boucles ! Je te conseille de regarder cette courte vidéo qui explique bien le fonctionnement des boucles : https://www.youtube.com/watch?v=Vg4ddGHznv0","boucles",[]),
    Node("Ah les fonctions ! C'est vrai que c'est un peu dure mais c'est une des bases à apprendre en python et sur n'importe quel langage!\n Regarde cette vidéo qui va te permettre de mieux comprendre les fonctions : https://www.youtube.com/watch?v=uFWYSSsJ_JE","fonction",[]),
    Node("Les classes ? Bien sûr je vais t'aider! Voici un tuto pour mieux comprendre le fonctionnement des classes : https://www.youtube.com/watch?v=91dPooHyNIo","classe",[]),
    Node("Ah le bon dico en python ! Consulte le lien suivant pour mieux comprendre le fonctionnement des dictionnaires en python : https://courspython.com/dictionnaire.html","dictionnaire",[]),
    Node("Les arbres ! C'est le dernier chapitre que vous avez vu en python, je peux comprendre que tu as certaines difficultés.\n Regarde ce lien pour mieux comprendre le fonctionnement des arbres : https://pixees.fr/informatiquelycee/n_site/nsi_term_projet_4.html","arbre",[])

]
php = [
    Node("Ah les boucles ! Ce site t'explique bien le fonctionnement des boucles : https://www.phpfacile.com/apprendre_le_php/boucles_for_while_en_php ","boucle",[]),
    Node("Ah les fonctions ! C'est vrai que c'est un peu dure mais c'est une des bases à apprendre sur n'importe quel langage!\n Regarde cette vidéo qui va te permettre de mieux comprendre les fonctions : https://www.youtube.com/watch?v=UXdvpKRQsx8","fonction",[]),
    Node("Les variables ! Voici comment s'y prendre avec les variables en php : https://www.youtube.com/watch?v=UnqJwiIPbag","variable",[]),
    Node("Session ! Regarde cette courte vidéo sur comment s'y prendre avec les sessions en php : https://www.youtube.com/watch?v=j0a1kQpELRo","session",[])
]
sql = [
    Node("PDO ! Voici  comment fonctionne la fonction PDO : https://www.commentcamarche.net/faq/27489-pdo-une-autre-facon-d-acceder-a-vos-bases-de-donnees", "pdo",[]),
    Node("Tu parle bien de l'insertion d'un élement dans la base de donnée ? Alors voici comment s'y prendre : https://sql.sh/cours/insert-into ", "insert",[]),
    Node("Sélectionner un élement dans la base de donnée c'est simple! Voici comment s'y prendre : https://sql.sh/cours/select ", "select",[]),
    Node("Mettre à jour la base de donnée c'est rapide et simple! Voici comment s'y prendre : https://sql.sh/cours/update", "update",[]),
    Node("Supprimer un élement de la base donnée c'est rapide ! Voici comment s'y prendre : https://sql.sh/cours/delete ", "delete",[]),
    Node("Les jointures en SQL ! Voici comment s'y prendre : https://sql.sh/cours/jointures ", "jointure",[]),
    Node("La condition having en SQL ! Voici comment s'y prendre : https://sql.sh/cours/having", "having",[]),
    Node("La commande where en SQL ! Voici comment s'y prendre : https://sql.sh/cours/where", "where",[])
]
back = [
    Node("PHP ! Qu'est-ce qui te pose problème plus précisément ?", "php", php),
    Node("PYTHON ! Qu'est-ce qui te pose problème plus précisément ?", "python", programation),
    Node("SQL ! Qu'est ce qui vous te problème plus précisément ?", "sql", sql)
]
html = [
    Node("Si tu veux comprendre les bases du HTML, consulte ce lien : https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/HTML_basics ","base",[]),
    Node("LES BALISES ! Regarde cette vidéo qui explique bien le fonctionnement des balises en HTML : https://www.youtube.com/watch?v=NwlCc-5RPqY","balises",[]),
    Node("LES HEADERS ! Voici un tuto pour mieux comprendre le fonctionnement du header : https://developer.mozilla.org/fr/docs/Web/HTML/Element/header ","header",[]),
    Node("LE BODY ! Voici un tuto pour mieux comprendre le fonctionnement du body de la page : https://developer.mozilla.org/fr/docs/Web/HTML/Element/body","body",[]),
    Node("LES FOOTERS ! Voici un tuto pour mieux comprendre le fonctionnement du footer : https://developer.mozilla.org/fr/docs/Web/HTML/Element/footer","footer",[]),
    Node("Les images en HTML ! Pour insérer une image dans une page c'est simple regarde cette vidéo pour comprendre : https://www.youtube.com/watch?v=7T9H-P45REg&list=PLjwdMgw5TTLUeixVGPNl1uZNeJy4UY6qX&index=10","image",[]),
    Node("Les div & span en HTML ! Regarde cette vidéo pour comprendre : https://www.youtube.com/watch?v=M34IhS0Pfj8&list=PLjwdMgw5TTLUeixVGPNl1uZNeJy4UY6qX&index=13","div",[]),
    Node("Les tables en HTML ! Regarde cette vidéo pour comprendre : https://www.youtube.com/watch?v=g_u3U2BtK88&list=PLjwdMgw5TTLUeixVGPNl1uZNeJy4UY6qX&index=11","table",[]),
    Node("Les formulaires en HTML ! Regarde cette vidéo pour comprendre : https://www.youtube.com/watch?v=r-X7DutXeIY&list=PLjwdMgw5TTLUeixVGPNl1uZNeJy4UY6qX&index=16","formulaire",[]),
    Node("Les liens hypertextes en HTML ! Regarde cette vidéo pour comprendre : https://www.youtube.com/watch?v=gJ_G-gxQRRk&list=PLjwdMgw5TTLUeixVGPNl1uZNeJy4UY6qX&index=9","lien",[])
]
css = [
    Node("Si tu veux comprendre les bases du CSS, regarde cette vidéo : https://www.youtube.com/watch?v=_-KEFeWLVtY","base",[]),
    Node("Les sélécteurs sont importants en CSS, regarde cette vidéo pour comprendre : hhttps://www.youtube.com/watch?v=EM8UlPeBfuk&list=PLjwdMgw5TTLVjTZQocrMwKicV5wsZlRpj&index=2","sélecteur",[]),
    Node("Rendre son site responsive ! Si t'a pas bien compris le cours, voici un petit tuto qui le résume : https://www.youtube.com/watch?v=BdzKNrxLiSs","responsive",[]),
    Node("Les grids ! Pas encore famillier avec cette propriété ? Regarde cette vidéo elle va surement t'aider : https://www.youtube.com/watch?v=vAs00R8aXUA", "grid",[]),
    Node("La position en CSS ! Pas encore famillier avec cette propriété ? Regarde cette vidéo elle va surement t'aider : https://www.youtube.com/watch?v=uo13gKY6q5k&t=210s","position",[]),
    Node("Le style du texte ! Tu veut savoir comment bien maitriser le style de tes textes  ? Viens voir par là : https://www.youtube.com/watch?v=n4H0nod_gHY","texte",[]),
    Node("Tu n'as pas bien compris la propriété flex ? Regarde cette vidéo, tu verras comment c'est cool : https://www.youtube.com/watch?v=Pl7LbpGr2uU", "flex",[])
]
javascript = [
    Node("Si tu veux comprendre les bases du JS, regarde cette vidéo : https://www.youtube.com/watch?v=XkvrHQNmigs", "base",[]),
    Node("Les boucles ! Voici un tuto qui explique bien le fonctionnement des boucles : https://www.youtube.com/watch?v=jgt_VqnGPHg", "boucle",[]),
    Node("Les fonctions ? C'est très important, regarde cette vidéo pour mieux comprendre les fonctions en JS : https://www.youtube.com/watch?v=pggJ5s6sTpk ", "fonction",[]),
    Node("Les variables ! Voici comment s'y prendre avec les variables en JS : https://www.youtube.com/watch?v=L8yNc1xqAw8", "variable",[]),
    Node("Les conditions ! Voici comment s'y prendre avec les conditions en JS : https://www.youtube.com/watch?v=DmHuw9dGYRw", "condition",[]),
    Node("Le DOM ! Voici comment s'y prendre avec le DOM en JS : https://www.youtube.com/watch?v=UBIfdObb9cY", "dom",[]),
    Node("Les évènements ! Visionne cette vidéo pour comprendre les évènements en JS : https://www.youtube.com/watch?v=KnBEDuzvRCA", "évènement",[]),
]
front = [
    Node("HTML ! Qu'est-ce qui te pose problème plus précisément ?", "html", html),
    Node("CSS ! Qu'est-ce qui te pose problème plus précisément ?", "css", css),
    Node("JAVASCRIPT ! Qu'est ce qui te pose problème plus précisément ?", "javascript", javascript)
]
scrum = [
    Node("Tu trouveras tout les informations possible sur le Scrum Product Owner via le lien suivant : https://www.qrpinternational.fr/blog/glossaire/scrum-product-owner-definition-role-responsabilites-et-competences/","owner",[]),
    Node("Tu trouveras tout les informations possible sur le Scrum Master via le lien suivant : https://www.qrpinternational.fr/blog/glossaire/scrum-master-definition-role-responsabilites-et-competences/","master",[]),
    Node("Tu trouveras tout les informations possible sur le Scrum Developer via le lien suivant : https://www.qrpinternational.fr/blog/glossaire/scrum-developer-definition-role-responsabilites-et-competences/","developer",[]),
    Node("Tu trouveras tout les informations possible sur le Scrum Team via le lien suivant : https://www.atlassian.com/fr/agile/scrum/roles#:~:text=Scrum%20pr%C3%A9sente%20trois%20r%C3%B4les%20%3A%20Product,intitul%C3%A9s%20lorsqu'elles%20adoptent%20Scrum","team",[]),
    Node("Tu trouveras tout les informations possible sur le sprint via le lien suivant : https://www.journaldunet.fr/web-tech/guide-de-l-entreprise-digitale/1443836-sprint-definition-planning-review-retrospective-backlog/","sprint",[])
]
graphism=[
    Node("Apprend les bases du logiciel InDesign avec cette video disponible sur Youtube : https://www.youtube.com/watch?v=FK5GEEEOZyo","indesign",[]),
    Node("Apprend les bases du logiciel Photoshop avec cette video disponible sur Youtube : https://www.youtube.com/watch?v=SvFFh5_HUA8","photoshop",[]),
    Node("Apprend les bases du logiciel Illustrator avec cette video disponible sur Youtube : https://www.youtube.com/watch?v=gMSwSjD67H8","illustrator",[])
]
design=[
    Node("Suivez ce cours afin de mieux comprendre l'UI design : https://www.mailabs.fr/tout-comprendre-de-lui-design/","ui",[]),
    Node("Suivez ce cours afin de mieux comprendre l'UX design : https://lagrandeourse.design/blog/ux-design/quest-ce-que-l-ux-design/","ux",[]),
    Node("Suivez ce cours complet disponible sur OpenClassRooms pour comprendre comment utiliser Figma : https://openclassrooms.com/fr/courses/7342806-creez-une-maquette-pour-le-developpement-web/7458079-prenez-en-main-figma","figma",[])
]
cours = [
    Node("Back-end ! Quel language ?", "back", back),
    Node("Front-end ! Quel language ?", "front", front),
    Node("Programmation ! En première année tu aborde que python, dit-moi qu'est-ce qui ne va pas avec ce language ?", "programation", programation),
    Node("Design ! Tu veut en savoir plus sur le logiciel Figma ou la théorie UI/UX", "design", design),
    Node("Outils graphique ! Quel logiciel (InDesign, Photoshop, Illustrator)", "graphique", graphism),
    Node("SCRUM ! Quel rôle t'interesse ?", "scrum", scrum),
    Node("SGBDR ! Dis-moi quel commande tu ne comprend pas en SQL ?", "SGBDR", sql),
    Node("Technologie web ! Tu peux trouver grâce à ce lien dropbox tout les cours vu avec le prof : https://www.dropbox.com/sh/hsdvu8i6bkaw6w5/AAC2-D9MnJUREUFgC3eY3bS_a/techno_web_et_internet/Groupe%201?dl=0&subfolder_nav_tracking=1", "techno", [])
]
first_list = [
    Node("Un cours ! Sur quel matière (back, front, graphique,...) ?", "cours", cours),
    Node("L'alternance ! Que veut tu savoir dessus ?", "alternance", alternance),
    Node("Le stage ! Que veut tu savoir dessus ?", "stage", stage),
    Node("Secretariat ! De quoi as-tu besoin ?", "administration", administration)
]
first_node = Node("Salut !\nJe suis G-MEC, HETIC m'a engagé afin d'apporter de l'aide et répondre à ses (nouveaux) étudiants en développement WEB.\nÀ tout moment tu peut écrire 'return' pour revenir à la question précédente, 'reset' pour redémarrer la conversation, 'fin' pour l'arrêter ou'$info' pour comprendre mon fonctionnement.\nDit-moi comment je peut t'aider ? (cours, alternance, stage, administration)","g-mec",first_list)
lescommandes = ['g-mec!','$info','$add','$modo','$heure','$date','$clear','$date','fin']
current_node = first_node
history = dict()
mode_help = False

dic_contrib = dict()

#MAIN
@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    Help_channel = client.get_channel(token)
    global current_node
    global history
    global mode_help
    
    if mode_help == False :
        for k in dic_contrib:
            if k in message.content:
                await message.channel.send(dic_contrib[k])

    if message.channel == Help_channel and message.content =='g-mec!':
        mode_help = True
        history[message.author.name]=list()
        await Help_channel.send("@"+message.author.name)
        await Help_channel.send(first_node.question)
    
    global z

    if mode_help and message.channel == Help_channel :

        j = 0
        decompt = 0
        z=0
        for child in current_node.list_child_node:
            decompt = decompt +1
            if message.content == "return":
                current_node = history[message.author.name][j-1]
                md = await Help_channel.history(limit = 3).flatten()
                for mdd in md :
                    await mdd.delete()
                break

            elif message.content == "reset":
                current_node = history[message.author.name][0]
                await Help_channel.send("@"+message.author.name)
                await Help_channel.send(first_node.question)
                break

            elif child.keyword not in message.content and decompt >= len(current_node.list_child_node)  and message.content not in lescommandes and message.content not in dic_contrib:
                await Help_channel.send("Oups ! À cette étape, je n'ai pas encore de réponse à cette demande,\n tu peut essayer quelque chose d'autre ou contribuer au développement du bot en ajoutant une réponse à ta demande en utilisant la commande (merci de respecter la syntax) '$add entrée sortie'.")
                break

            elif child.keyword not in message.content and decompt >= len(current_node.list_child_node)  and message.content not in lescommandes and message.content in dic_contrib:
                for k in dic_contrib:
                    if k in message.content:
                        await message.channel.send(dic_contrib[k])
                break

            elif message.content == "fin":
                await Help_channel.send("J'espère que j'ai pu t'aider, à la prochaine !")
                mode_help = False
                return

            elif child.keyword in message.content :
                lescommandes.append(message.content)
                j=j+1
                await Help_channel.send(child.question)
                history[message.author.name].append(current_node)
                if z<len(current_node.list_child_node):
                    current_node = child
                z=1
                break

            z=z+1
               
        if z>len(current_node.list_child_node):
            
            history[message.author.name]=[]
            await Help_channel.send('Et voila, bon courage !')
            current_node = first_node
            mode_help = False
            return

    await client.process_commands(message)

#memes
@client.command()
async def memes(ctx):
    list_meme = ['quand on fait tester une fonctionnalité au client : https://lesjoiesducode.fr/content/042/FH6Agq5.webm','https://lesjoiesducode.fr/content/042/l76P9gQ.jpg','https://lesjoiesducode.fr/content/042/ESIFsYK.jpg', 'quand je montre le rendu de mon integration au graphiste : https://lesjoiesducode.fr/content/042/ntColu0.webm','quand je vois tout les logs rouges qui defiles dans ma consol : https://lesjoiesducode.fr/content/042/V3xMThl.webm','quand tu tombe sur un bout de code en ligne qui répond à ta demande : https://lesjoiesducode.fr/content/042/eONty8S.webm', 'quand le dev senior te propose son aide : https://lesjoiesducode.fr/content/042/nptAJPE.webm', 'quand ton code compile du premier coup et sans aucune erreur : https://lesjoiesducode.fr/content/042/mldsqXy.webm', 'quand tu ouvre du code auquel tu n\'a pas toucher depuis plusieurs mois:https://lesjoiesducode.fr/content/042/q9bM1cO.webm', 'quand le dev senior debug devant toi : https://lesjoiesducode.fr/content/033/x7wuL2A.webm', 'quand toute la team respect les normes de codage : https://lesjoiesducode.fr/content/042/ddGqVNT.webm','quand tu presente la version beta au client : https://lesjoiesducode.fr/content/007/7mtLFpn.webm', 'qaund le dev senior corrige un bug a l\'ancienne : https://lesjoiesducode.fr/content/042/TQi4cGg.webm','https://lesjoiesducode.fr/content/042/CTLjwo7.jpg','quand tu voit qu\'un admin s\'est connecté à ton projet : https://lesjoiesducode.fr/content/018/i2dgAb3snnrP1.webm','https://lesjoiesducode.fr/content/042/QnX0Ku6.jpg','https://lesjoiesducode.fr/content/042/X1XbhBh.jpg','quand t\'execute les delete en masse: https://lesjoiesducode.fr/content/008/81oNBSB.webm','quand je pense finir ma tache : https://lesjoiesducode.fr/content/042/lQ25kWk.webm']
    nb_rdm = randint(1,len(list_meme))
    await ctx.send(list_meme[nb_rdm])
    
#citation
@client.command()
async def citation(ctx):
    citations = [
            "« Ce n'est pas grave si vous avancez lentement, du moment que vous ne vous arrêtez pas. », Confucius.",
            "« Il n'y a qu'une façon d'échouer, c'est d'abandonner avant d'avoir réussi. », Georges Clemenceau.",
            "« Tout est possible à qui rêve, ose, travaille et n'abandonne jamais. », Xavier Dolan.",
            "« Je ne perds jamais. Soit je gagne, soit j'apprends. », Nelson Mandela.",
            "« Croyez en vos rêves et ils se réaliseront peut-être. Croyez en vous et ils se réaliseront sûrement. », Martin Luther King.",
            "« La motivation vous sert de départ. L'habitude vous fait continuer. », Jim Ryun",
            "« Il est dur d'échouer, mais il est pire de n'avoir jamais tenté de réussir. », Franklin Delano Roosevelt",
            "« Celui qui veut réussir trouve un moyen. Celui qui veut rien faire trouve une excuse. », Proverbe"
        ]
    nb_rdm = randint(1,len(citations))
    await ctx.send(citations[nb_rdm])

#contribution
@client.command()
async def add(ctx,entre,sortie):
    global dic_contrib
    dic_contrib[entre]=sortie


#mp
@client.command()
async def modo(ctx,userid:discord.Member,*,msg=None):
    msg="Salut, "+ctx.author.name+"a besoin de ton aide !"
    embed = discord.Embed(title=msg)
    await userid.send(embed=embed)

#ABOUT
@client.command()
async def info(ctx):
    print("ok")
    await ctx.send("info :\nComment je fonctionne?\nJe dirige la discussion et je repère les mots clèfs pour répondre le plus précisement.\nLes commandes possibles : \ng-mec! -> démarrer une nouvelle discussion (uniquement sur le channel 'G-SHAME help').\n$clear nb -> supprimer des messages (nb=nombre de message à supprimer).\n$server -> afficher les information relative au serveur.\n$date -> afficher la date.\n$heure -> afficher l'heure'\n $modo @userpseudo -> permet de demander de l'aide à un modo\n $add entrée sortie -> permet de contribuer au developpement du bot en ajoutant la reponse à une entrée.\n$memes -> tu auras un memes tiré au hazard.\n$citation -> tu auras une citation tirée au hazard.\n$play -> faire jouer un morceau\n \nNB:vos données sont sauvegarder uniquement pendant la seance d'aide, une fois la seance terminer vos informations sont supprimer.")

#Heure
@client.command()
async def heure(ctx):
    await ctx.send(datetime.now().strftime('%H:%M:%S'))

#Date
@client.command()
async def date(ctx):
    await ctx.send(datetime.now().strftime('%d-%m-%Y'))

#nouveau membre
@client.event
async def on_member_join(member):
    Help_channel = client.get_channel(token)
    await Help_channel.send('Bonjour !' + member.display_name + 'bienvenu sur G-SHAME.')


#CLEAR
@client.command()
async def clear(ctx, nombre : int):
    md = await ctx.channel.history(limit = nombre+1).flatten()
    for mdd in md :
        await mdd.delete()
        


#SERVER
@client.command()
async def server(ctx):
    name = ctx.guild.name
    description = ctx.guild.description
    owner = ctx.guild.owner
    id = ctx.guild.id
    region = ctx.guild.region
    member_count = ctx.guild.member_count
    icon = ctx.guild.icon_url

    embed = discord.Embed(
        title = name ,
        description = description,
        color = discord.Color.red()
    )
    embed.set_thumbnail(url = icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server Id", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=member_count, inline=True)

    await ctx.send(embed = embed)

    #PLAY
@client.command()
async def play(ctx):
    await ctx.send("Tu veut faire jouer un morceau ?\nViens ici : https://discord.gg/'token'")

    
client.run(token)


