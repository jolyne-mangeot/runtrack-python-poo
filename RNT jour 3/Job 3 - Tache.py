class Tache:
    def __init__(self, titre, description, status):
        self.titre = titre
        self.description = description
        self.status = status

class Listedetache:
    def __init__(self, taches):
        self.taches = taches #list
    
    def ajouter_tache(self, tache):
        self.taches.append(tache)
    
    def supprimer_tache(self, tache):
        self.taches.pop(self.taches.index(tache))
    
    def marquer_fini(self, tache):
        self.taches[self.taches.index(tache)].status = "finie"
    
    def afficher_list(self):
        tache_print = []
        for tache in self.taches:
            tache_print.append(tache.titre)
        return tache_print
    
    def filtrer_liste(self):
        for tache in self.taches:
            if tache.status == 'finie':
                print(tache.titre)
    
def main():
    manger = Tache('manger', 'manger miam-miam', 'en cours')
    balayer = Tache('balayer', 'enlever la poussière', 'en cours')
    taches = [manger, balayer]
    taches_classe = Listedetache(taches)
    taches_classe.marquer_fini(manger)
    print(taches_classe.afficher_list())
    taches_classe.filtrer_liste()
    cuisiner = Tache('cuisiner', 'sortir la poêle et cuire', 'en cours')
    taches_classe.ajouter_tache(cuisiner)
    taches_classe.supprimer_tache(manger)
    print(taches_classe.afficher_list())
    

main()