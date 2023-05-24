import json

def lecture():
    with open("eleve.json","r") as f:
        x = json.load(f)
        return x
def sauvegarde():
    with open("eleve.json","w") as f:
        json.dump(eleves, f)

eleves = lecture()

def afficher_users():
    for eleve in eleves:
        print(f"l'user {eleve['nom']} en classe {eleve['classe']}")

    d = retour_menu()
    if d == True:
        return True
    elif d == False:
        return False

def ajouter_users():
    print("entre le nom se l'eleve")
    a= input("==>")
    print("entre le pass de l'eleve")
    b= input("==>")
    print("entre la note de l'eleve")
    c= nombre_note()
    print("entre la classe de l'eleve")
    d= nombre_note()
    
    x={
        'nom':a,
        'pass':b,
        'role':"eleve",
        'svt':[], 
        'math':[], 
        'francais':[], 
        'histoire':[], 
        'anglais':[], 
        'note':c,
        'classe':d
    }
    eleves.append(x)
    print(f"l'eleve {a} a bien etait ajouter avec le rôle eleve")
    sauvegarde()
    d = retour_menu()
    if d == True:
        return True
    elif d == False:
        return False
    
def add_note():
    print("a quel eleve veut tu ajouter une note ?")
    x=input("==>")
    print("pour quel matiere ?")
    y=input("==>")
    for eleve in eleves:
        #print("12")
        if x == eleve['nom']:
            #print("1234")
            for cle,val in eleve.items():
                #print("123456")
                if y == cle:
                    print("entre une note:")
                    z=nombre_note()
                    eleve[cle].append(z)
                    print(f"\nla note {z} de {eleve['nom']} a bien etait ajouté | {eleve[cle]}")
                    sauvegarde()
                    break
    
    d = retour_menu()
    if d == True:
        return True
    elif d == False:
        return False





def montre_note():
    print("pour quel eleve veut tu afficher les notes ?")
    x=input("==>")
    print("pour quel matiere ?")
    y=input("==>")
    for eleve in eleves:
        #print("12")
        if x == eleve['nom']:
            #print("1234")
            for cle,val in eleve.items():
                #print("123456")
                if y == cle:
                    print(f"\nles notes en {cle} pour l'eleve {eleve['nom']} sont:")
                    print(f"{eleve[cle]}")
                    
                    
                    break
    
    d = retour_menu()
    if d == True:
        return True
    elif d == False:
        return False

def modifie_note():
    print("pour quel eleve veut tu modifier une note ?")
    x=input("==>")
    print("pour quel matiere ?")
    y=input("==>")
    for eleve in eleves:
        #print("12")
        if x == eleve['nom']:
            #print("1234")
            for cle,val in eleve.items():
                #print("123456")
                if y == cle:
                    print(f"\nles notes en {cle} pour l'eleve {eleve['nom']} sont:")
                    print(f"{eleve[cle]}")
                    print("quel note souhaite tu modifier ?")
                    note = nombre_note()
                    for i in eleve[cle]:
                        if note == i:
                            
                            eleve[cle].remove(i)
                            print(f"{note} a bien etait supprimer")
                            print("entre la nouvel note")
                            n_not=nombre_note()
                            eleve[cle].append(n_not)
                            sauvegarde()
                    
                    break
    
    d = retour_menu()
    if d == True:
        return True
    elif d == False:
        return False
    
def supprimer_unne_note():
    print("pour quel eleve veut tu supprimer une notes ?")
    x=input("==>")
    print("pour quel matiere ?")
    y=input("==>")
    for eleve in eleves:
        #print("12")
        if x == eleve['nom']:
            #print("1234")
            for cle,val in eleve.items():
                #print("123456")
                if y == cle:
                    print(f"\nles notes en {cle} pour l'eleve {eleve['nom']} sont:")
                    print(f"{eleve[cle]}")
                    print("quel note souhaite tu supprimer ?")
                    note = nombre_note()
                    for i in eleve[cle]:
                        if note == i:
                            print("salut")
                            eleve[cle].remove(i)
                            print(f"{note} a bien etait supprimer")
                            sauvegarde()
                    
                    break
    
    d = retour_menu()
    if d == True:
        return True
    elif d == False:
        return False

def deconnexion():
    global statut_user,nom_user
    statut_user = None
    nom_user = None
    print("tu as bien etait deconnecter")

def conexion():
    global statut_user,nom_user
    print("Entre un identifiant")
    x = input("==>")
    print("Entre le pass")
    y = input("==>")
    for eleve in eleves:
        if x == eleve['nom'] and y == eleve['pass']:
            print(f"\n{eleve['nom']} connexion accepter")
            statut_user = eleve['role']
            nom_user=eleve['nom']
            break
            

def print_menu():
    global statut_user
    te= statut_user
    y=len(te)+2
    x= len(te)+4
    b="*"+" "*y+"*"
    a= "*"+" "+te+" "+"*"
    print("")

    print("*"*x)
    print(b)
    print(a)
    print(b)
    print("*"*x)


def quitte():
    global statut_user
    statut_user= "quit"

def nombre_note():
    x=input("==>")
    verif= x.isdigit()
    while verif is False:
        x=input("==>")
        verif= x.isdigit() 
    x=int(x)
    return x


def modif_note():
    print("entre le nom de l'eleve au quel tu souhaite modifier la note")
    x= input("==>")
    for eleve in eleves:
        if x == eleve['nom']:
            print(f"{eleve['nom']} a actuellement la note de {eleve['note']}/20\n\nquel note veut tu lui atttribuer ?")
            x= nombre_note()
            eleve['note']=x
            print(f"\nla note de l'eleve {eleve['nom']} a etait modifier a {eleve['note']}/20 ")
    sauvegarde()
    d = retour_menu()
    if d == True:
        return True
    elif d == False:
        return False
    

def retour_menu():
    liste_choix=["oui","OUI","non","NON"]
    print("")
    print("Veut tu retourné au menu ?")
    x=input("==>")
    while x not in liste_choix:
        print("Veut tu retourné au menu ?")
        x=input("==>")
    if x == "oui" or x == "OUI":
        return True
    elif x == "non" or x == "NON":
        return False
    
def afficher_moyenne():
    liste_moyene=[]
    print("de quel eleve souhaite tu afficher la note ?")
    x=input("==>")
    for eleve in eleves:
        if x == eleve['nom']:
            if len(eleve['svt']) != 0:

                moyenne_svt = sum(eleve['svt'])/len(eleve['svt'])
                liste_moyene.append(moyenne_svt)
                
            if len(eleve['math']) != 0:
                moyenne_math = sum(eleve['math'])/len(eleve['math'])
                liste_moyene.append(moyenne_math)
            if len(eleve['francais']) != 0:
                moyenne_francais = sum(eleve['francais'])/len(eleve['francais'])
                liste_moyene.append(moyenne_francais)
            if len(eleve['histoire']) != 0:
                moyenne_histoire = sum(eleve['histoire'])/len(eleve['histoire'])
                liste_moyene.append(moyenne_histoire)
            if len(eleve['anglais']) != 0:
                moyenne_anglais = sum(eleve['anglais'])/len(eleve['anglais'])
                liste_moyene.append(moyenne_anglais)
    
    if len(liste_moyene) != 0:
        u=sum(liste_moyene)/len(liste_moyene)
        print(f"la moyenne général de {x} est de {u}/20") 
            
    
    d = retour_menu()
    if d == True:
        return True
    elif d == False:
        return False

def supprimer_eleve():
    print("Entre le nom de l'eleve que tu souhaite supprimer")
    x=input("==>")
    for eleve in eleves:
        if x == eleve['nom']:
            eleves.remove(eleve)#!!!!!!!!!!!!!!!!premiere utilisation!!!!!!!!!!!!!!!!!!!
            
    sauvegarde()
    d = retour_menu()
    if d == True:
        return True
    elif d == False:
        return False

def afficher_une_classe():
    liste_choix=["oui","OUI","non","NON"]
    print("[3] Troisieme\n[4] Quatrième\n[5] Cinquième\n[6] Sixième\n\nEntre la classe que tu souhaite consulter")
    x=nombre_note()
    
    print("")
    for eleve in eleves:
        if x == eleve['classe']:
            print(f"{eleve['nom']} a la note de : {eleve['note']}/20")
    
    print("veut tu afficher la moyenne de la classe ?")
    m = input("==>")
    while m not in liste_choix:
        m = input("==>")
    c=0
    liste_note=[]
    if m=='oui'or m=='OUI':
        for eleve in eleves:
            
            if x == eleve['classe']:
                z= eleve['classe']
                liste_note.append(eleve['note'])
                c+=1
        print(f"la moyenne des eleves {z} ème est de {sum(liste_note)/c}/20")

    d = retour_menu()
    if d == True:
        return True
    elif d == False:
        return False

def modif_mot_de_passe():
    global nom_user
    for eleve in eleves:
        if nom_user == eleve['nom']:
            print(f"\n{nom_user} ton mot de passe actuel est : {eleve['pass']}")
            v=eleve['pass']
            print("Entre ton nouveau mot de passe :")
            x = input('==>')
            print("Entre a nouveau ton nouveau mot de passe :")
            y = input('==>')
            while x!=y:
                print(f"\n{nom_user} ton mot de passe actuel est : {eleve['pass']}")
                print("Entre ton nouveau mot de passe :")
                x = input('==>')
                print("Entre a nouveau ton nouveau mot de passe :")
                y = input('==>')
            eleve['pass'] = y
            print(f"\n{eleve['nom']} ton ancien mot de passe {v}")
            print(f"a bien était remplacer par {eleve['pass']}")
            sauvegarde()
            d = retour_menu()
            if d == True:
                return True
            elif d == False:
                return False
            

def print_note_eleve():
    global noteT_eleve
    print("!NOTE POUR TOUT LES ELEVES:!")
    print(f"\n{noteT_eleve}")

    d = retour_menu()
    if d == True:
        return True
    elif d == False:
        return False
    
def mod_print_note_eleve():
    global noteT_eleve
    z= noteT_eleve
    liste_choix=["oui","OUI","non","NON"]
    print("Veut-tu modifié les informations pour les eleves:")
    x = input("==>")
    while x not in liste_choix:
        print("Veut-tu modifié les informations pour les eleves:")
        x = input("==>")
    if x =='oui' or x =='OUI':
        print("Entre les informations que souhaite partager au eleves")
        noteT_eleve=input("==>")

    print(f"{z} est maintenant:\n{noteT_eleve}")
    sauvegarde()
    d = retour_menu()
    if d == True:
        return True
    elif d == False:
        return False          


def reset_user():
    liste_choix=["oui","OUI","non","NON"]
    print("Veut tu vraiment supprimer la liste de tout les user ?")
    x=input("==>")
    while x not in liste_choix:
        print("Veut tu vraiment supprimer la liste de tout les user ?")
        x=input("==>")
    if x == "oui" or x == "OUI":
        eleves_copy=eleves.copy()#!!!!!!!!!!ouaah j'ai pas capter pourquoi faut faire une copie!!!!!!!!!!!!
        for eleve in eleves_copy:
            #print(eleve)
            if eleve['role'] == 'eleve':
                print(eleve)
                eleves.remove(eleve)
        
                
    sauvegarde()
    print(f"liste apres : {eleves}")
    d = retour_menu()
    if d == True:
        return True
    elif d == False:
        return False 

noteT_eleve="aucune"
nom_user=None
statut_user = None
menu_option=[{
    'indice':'1',
    'description':'Connection',
    'fonction': conexion,
    'role': 'all',
    'start': True
    
},{
    'indice':'2',
    'description':'Affi les utilisateur',
    'fonction': afficher_users,
    'role': 'prof',
    'start': False
    
},{
    'indice':'3',
    'description':'ajoutez un eleve/prof',
    'fonction' : ajouter_users,
    'role': 'admin',
    'start': False
},{
    'indice':'4',
    'description':'modifier note(a refaire)',
    'fonction' : modif_note,
    'role' : 'prof',
    'start' : False
},{
    'indice':'5',
    'description':"affiche la note d'un eleve(a refaire)",
    'fonction':afficher_moyenne,
    'role': 'eleve',
    'start': False
},{
    'indice':'6',
    'description':'supprime un eleve',
    'fonction': supprimer_eleve,
    'role': 'admin',
    'start': False
},{
    'indice':'7',
    'description':"afficher les infos d'une classe",
    'fonction': afficher_une_classe,
    'role': 'eleve',
    'start': False
},{
    'indice':'8',
    'description':"modifie ton mot de passe",
    'fonction': modif_mot_de_passe,
    'role': 'eleve',
    'start': False
},{
    'indice':'9',
    'description':"information pour les eleves",
    'fonction': print_note_eleve,
    'role': 'eleve',
    'start': False
},{
    'indice':'10',
    'description':"modifie information pour les eleves",
    'fonction': mod_print_note_eleve,
    'role': 'prof',
    'start': False
},{
    'indice':'11',
    'description':'reset tout les eleves',
    'fonction' : reset_user,
    'role': 'admin',
    'start': False
},{
    'indice':'12',
    'description':'ajouter une note a un eleve',
    'fonction' : add_note,
    'role': 'prof',
    'start': False
},{
    'indice':'13',
    'description':'affiche les notes des eleve',
    'fonction' : montre_note,
    'role': 'prof',
    'start': False
},{
    'indice':'14',
    'description':'modifie les notes des eleve',
    'fonction' : modifie_note,
    'role': 'prof',
    'start': False
},{
    'indice':'15',
    'description':'supprime les notes des eleve',
    'fonction' : supprimer_unne_note,
    'role': 'prof',
    'start': False
},{
    'indice':'0',
    'description':'deconnexion',
    'fonction' : deconnexion,
    'role': 'eleve',
    'start': False
},{
    'indice':'quit',
    'description':'Quittez',
    'fonction': quitte,
    'role': 'all',
    'start': True
}]

#!!!!!!!!!!!!!!!!!!!!!!JUSTE POUR QUITTEZ!!!!!!!!!!!!!!!!!!!!
def pre_menu():
    global statut_user,nom_user
    
    ch=[]
    while statut_user == None:
        print("\n*******************")
        for option in menu_option:
            if option['start']==True:
                print(f"[{option['indice']}] {option['description']}")
                ch.append(option['indice'])
        
        print("\n*****************")
        print("\nQue veut tu faire ?")
        x = input("==>")
        print("")
        while x not in ch:
            print("entre un choix valide:")
            print("\nQue veut tu faire ?")
            x = input("==>")
            print("")
        
        for option in menu_option:
            if x == option['indice']:

                
                x={option['fonction']()}
                
                if statut_user == "quit":
                    print(statut_user)
                    return False
    
    print(nom_user)
    return True

    
def menu():
    global statut_user
    g= True
    while g:
        z=pre_menu()
        if z is False:
            g=False
            break
        

            
        #!!!!!!!!!!!!TEST DE FAIRE UE FONCTION AVEC PARAMETRE!!!!!!!!!!!!!!!!!!!
        if statut_user == "admin":
            print_menu()
        
            
            print("")
            choix=[]
            for option in menu_option:
                if option['role'] == 'admin' or option['role'] == 'prof' or option['role'] == 'eleve':
                    choix.append(option['indice'])
                    print(f"[{option['indice']}] {option['description']}")

            
            print("\nQue veut tu faire ?")
            x= input("==>")
            print("")
            while x not in choix:
                print("\nQue veut tu faire ?")
                x= input("==>")
                print("")
            for option in menu_option:
                if x == option['indice']:
                    x={option['fonction']()}

                    for i in x:
                        
                        if i == False:
                            print("FERME LE PROGRAMME")
                            g=False
                      
                        
                        


        if statut_user == "prof":
            print_menu()
            
            print("")
            choix=[]
            for option in menu_option:
                if option['role'] == 'prof' or option['role'] == 'eleve':
                    print(f"[{option['indice']}] {option['description']}")
                    choix.append(option['indice'])
            print("\nQue veut tu faire ?")
            x= input("==>")
            print("")
            while x not in choix:
                print("\nQue veut tu faire ?")
                x= input("==>")
            for option in menu_option:
                if x == option['indice']:
                    x={option['fonction']()}
                    for i in x:
                        
                        if i == False:
                            print("FERME LE PROGRAMME")
                            g=False



        if statut_user == "eleve":
            print_menu()
            
            print("")
            choix=[]
            for option in menu_option:
                if option['role'] == 'eleve':
                    print(f"[{option['indice']}] {option['description']}")
                    choix.append(option['indice'])
            print("\nQue veut tu faire ?")
            x= input("==>")
            print("")
            while x not in choix:
                print("\nQue veut tu faire ?")
                x= input("==>")
            for option in menu_option:
                if x == option['indice']:
                    x={option['fonction']()}
                    for i in x:
                        
                        if i == False:
                            print("FERME LE PROGRAMME")
                            g=False
        

menu()
#ajouter_users()
#sauvegarde()
#for eleve in eleves:
#    print(eleve['note'])
#afficher_users()