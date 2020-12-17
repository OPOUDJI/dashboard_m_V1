from django.db import models

class Mere(models.Model):
    nom = models.CharField("Nom", max_length=100)
    prenoms = models.CharField("Prénoms", max_length=300)
    date_naissance = models.DateField("Date de naissance")
    etat_sante = models.CharField("Etat de santé", max_length=200)
    
    def __str__(self):
        return self.nom
        
    class Meta:
        verbose_name = "Mère"


   
class Pere(models.Model):
    nom = models.CharField("Nom", max_length=100)
    prenoms = models.CharField("Prénoms", max_length=300)
    date_naissance = models.DateField("Date de naissance")
    etat_sante = models.CharField("Etat de santé", max_length=200)
    
    def __str__(self):
        return self.nom
        
    class Meta:
        verbose_name = "Père"



class Frere(models.Model):
    nom = models.CharField("Nom", max_length=100)
    prenoms = models.CharField("Prénoms", max_length=300)
    date_naissance = models.DateField("Date de naissance")
    etat_sante = models.CharField("Etat de santé", max_length=200)
    
    def __str__(self):
        return self.nom
        
    class Meta:
        verbose_name = "Frère"



class Soeur(models.Model):
    nom = models.CharField("Nom", max_length=100)
    prenoms = models.CharField("Prénoms", max_length=300)
    date_naissance = models.DateField("Date de naissance")
    etat_sante = models.CharField("Etat de santé", max_length=200)
    
    def __str__(self):
        return self.nom
        
    class Meta:
        verbose_name = "Soeur"


class Enfant(models.Model):
    CHOICES_1 = [('0','Homme'),('1','Femme')]
    nom = models.CharField("Nom", max_length=100)
    prenoms = models.CharField("Prénoms", max_length=300)
    date_naissance = models.DateField("Date de naissance")
    sexe = models.CharField("Sexe", max_length=1, choices=CHOICES_1)
    niveau_sc = models.CharField("Niveau scolaire", max_length=100)
    img_extrait_naiss = models.FileField("Extrait de naissance", null=True)
    img_ident = models.ImageField("Photo d'identité", null=True)
    etat_sante = models.CharField("Etat de santé", max_length=200)
    
    def __str__(self):
        return self.nom
        
    class Meta:
        verbose_name = "Enfant"



class Qualif(models.Model):
    diplome = models.CharField("Diplôme", max_length=500)
    etabl = models.CharField("Etablissement", max_length=500)
    annee = models.CharField("Année", max_length=9)
    
    def __str__(self):
        return self.diplome
        
    class Meta:
        verbose_name = "Qualification"



class Agent(models.Model):
    CHOICES_1 = [('0','Monsieur'),('1','Madame'),('2','Mademoiselle')]
    CHOICES_2 = [('0','Homme'),('1','Femme')]
    CHOICES_3 = [('0','Marié(e)'),('1','Célibataire'),('2','Voeuf(e)'),('3','Divorcé(e)')]
    n_matricule = models.CharField(primary_key=True, max_length=500)
    civilite = models.CharField("Civilité", max_length=1, choices=CHOICES_1)
    nom = models.CharField("Nom", max_length=100)
    prenoms = models.CharField("Prénoms", max_length=300)
    nom_jeune_fille = models.CharField("Nom de jeune fille", null=True, max_length=400)
    date_naissance = models.DateField("Date de naissance")
    sexe = models.CharField("Sexe", max_length=1, choices=CHOICES_2)
    domicile = models.CharField("Domicile", max_length=200)
    n_cnps = models.CharField("Numéro CNPS", max_length=200)
    telephone_fixe = models.CharField("Téléphone fixe", max_length=10)
    telephone_portable = models.CharField("Téléphone portable", max_length=10)
    email = models.EmailField("Email")
    situation_matri = models.CharField("Situation matrimoniale", max_length=1, choices=CHOICES_3)
    pointure_chauss = models.PositiveIntegerField("Pointure de chaussure")
    date_entree = models.DateField("Date d'entrée")
    date_depart = models.DateField("Date de départ")
    nom_urgence = models.CharField("Nom de la personne à contacter en cas d'urgence", max_length=300)
    contact_urgence = models.CharField("Contact de la personne à contacter en cas d'urgence", max_length=10)
    dernier_emploi_exerce = models.CharField("Dernier emploi exercé", max_length=100)
    precedent_employeur = models.CharField("Précédent employeur", max_length=100)
    img_cv = models.FileField("CV", null=True)
    img_dernier_diplome = models.FileField("Dernier diplôme obtenu", null=True)
    img_extrait_naiss = models.FileField("Extrait de naissance", null=True)
    img_ident = models.ImageField("Photo d'identité", null=True)
    img_immat = models.ImageField("Photo de l'immatriculation CNPS", null=True)
    img_carte_ident_pass = models.ImageField("Photo de la carte d'identité ou du passeport", null=True)
    enfants = models.ManyToManyField(Enfant, related_name='agents', blank=True)
    freres = models.ManyToManyField(Frere, related_name='agents', blank=True)
    soeurs = models.ManyToManyField(Soeur, related_name='agents', blank=True)
    qualifications = models.ManyToManyField(Qualif, related_name='agents', blank=True)
    mere = models.ForeignKey(Mere, on_delete=models.CASCADE)
    pere = models.ForeignKey(Pere, on_delete=models.CASCADE)

    def __str__(self):
        return self.n_matricule
        
    class Meta:
        verbose_name = "Agent"

class Details_banc(models.Model):
    n_compte = models.CharField("Numéro de compte", max_length=200, primary_key=True)
    nom_etabl = models.CharField("Nom de l'établissement", max_length=500)
    adresse = models.CharField("Adresse", max_length=200)
    telephone = models.CharField("Téléphone", max_length=10)
    code_iban = models.CharField("CODE IBAN", max_length=200)
    code_swift = models.CharField("CODE SWIFT", max_length=200)
    img_rib = models.ImageField("Photo RIB", null=True)
    img_releve_banc = models.ImageField("Photo rélévé bancaire", null=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.n_compte
        
    class Meta:
        verbose_name = "Détails bancaires"

class Conjoint(models.Model):
    nom = models.CharField("Nom", max_length=100)
    prenoms = models.CharField("Prénoms", max_length=300)
    date_naissance = models.DateField("Date de naissance")
    telephone_portable = models.CharField("Téléphone portable", max_length=10)
    img_extrait_naiss = models.FileField("Extrait de naissance", null=True)
    img_ident = models.ImageField("Photo d'identité", null=True)
    etat_sante = models.CharField("Etat de santé", max_length=200, null=True)
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom
        
    class Meta:
        verbose_name = "Conjoint"

class Passeport(models.Model):
    n_passeport = models.CharField("Numéro du passeport ", max_length=200, primary_key=True)
    lieu_del = models.CharField("Lieu de délivrance", max_length=200)
    date_del = models.DateField("Date de délivrance")
    date_exp = models.DateField("Date d'expiration'")
    nationalite = models.CharField("Nationalité", max_length=200)
    sec_nationalite = models.CharField("Seconde nationalité", max_length=200)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.n_passeport
        
    class Meta:
        verbose_name = "Passeport"

class Carte_ident(models.Model):
    n_carte_ident = models.CharField("Numéro de la carte d'identité ", max_length=200, primary_key=True)
    lieu_del = models.CharField("Lieu de délivrance", max_length=200)
    date_del = models.DateField("Date de délivrance")
    date_exp = models.DateField("Date d'expiration'")
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.n_carte_ident
        
    class Meta:
        verbose_name = "Carte d'identité"

class Ant_sante(models.Model):
    CHOICES = [('0','Non'),('1', 'Oui')]
    hosp_chir = models.CharField("Avez-vous déjà été hospitalisé(e) pour opération chirugicale ?", max_length=1, choices=CHOICES)
    hosp_acc = models.CharField("Avez-vous déjà été hospitalisé(e) pour accident ?", max_length=1, choices=CHOICES)
    hosp_rep = models.CharField("Avez-vous déjà été hospitalisé(e) pour cure de repos ?", max_length=1, choices=CHOICES)
    hosp_mal = models.CharField("Avez-vous déjà été hospitalisé(e) pour maladie ?", max_length=1, choices=CHOICES)
    pre_1 = models.CharField("Si oui, précisez ?", max_length=300, null=True)
    att_ecz = models.CharField("Avez-vous été ou êtes-vous atteint(e) de problème d'eczéma aux mains ?", max_length=1, choices=CHOICES)
    att_all = models.CharField("Avez-vous été ou êtes-vous atteint(e) d'allergie, eczéma(autre), rhume des foins ?", max_length=1, choices=CHOICES)
    att_resp = models.CharField("Avez-vous été ou êtes-vous atteint(e) de problèmes respiratoires (asthme, bronchite, emphysème, tuberculose) ?", max_length=1, choices=CHOICES)
    att_con = models.CharField("Avez-vous été ou êtes-vous atteint(e) de perte de connaissance ?", max_length=1, choices=CHOICES)
    att_cer = models.CharField("Avez-vous été ou êtes-vous atteint(e) de commotion cérébrale ?", max_length=1, choices=CHOICES)
    att_conv = models.CharField("Avez-vous été ou êtes-vous atteint(e) d'épilepsie ? Convulsions ?", max_length=1, choices=CHOICES)
    att_depr = models.CharField("Avez-vous été ou êtes-vous atteint(e) de dépression nerveuse ? Epuisement ?", max_length=1, choices=CHOICES)
    att_stress = models.CharField("Avez-vous été ou êtes-vous atteint(e) du stress ? Burn-out ?", max_length=1, choices=CHOICES)
    att_peur = models.CharField("Avez-vous été ou êtes-vous atteint(e) de la peur du vide ou du travail en hauteur ?", max_length=1, choices=CHOICES)
    att_diab = models.CharField("Avez-vous été ou êtes-vous atteint(e) du diabète ?", max_length=1, choices=CHOICES)
    att_diges = models.CharField("Avez-vous été ou êtes-vous atteint(e) de maladie digestive ?", max_length=1, choices=CHOICES)
    att_her = models.CharField("Avez-vous été ou êtes-vous atteint(e) d' hernie ?", max_length=1, choices=CHOICES)
    att_art = models.CharField("Avez-vous été ou êtes-vous atteint(e) d' hypertension artérielle ?", max_length=1, choices=CHOICES)
    att_coeur = models.CharField("Avez-vous été ou êtes-vous atteint(e) de maladie du coeur ?", max_length=1, choices=CHOICES)
    att_vein = models.CharField("Avez-vous été ou êtes-vous atteint(e) de maladie des artères, des veines ?", max_length=1, choices=CHOICES)
    att_or = models.CharField("Avez-vous été ou êtes-vous atteint(e) de maladie des oreilles, du nez, des sinus ?", max_length=1, choices=CHOICES)
    att_ves = models.CharField("Avez-vous été ou êtes-vous atteint(e) de vestiges, perte de l'équilibre ?", max_length=1, choices=CHOICES)
    att_sg = models.CharField("Avez-vous été ou êtes-vous atteint(e) de maladie du sang ?", max_length=1, choices=CHOICES)
    att_dos = models.CharField("Avez-vous été ou êtes-vous atteint(e) de maux de dos, rhumatismes ?", max_length=1, choices=CHOICES)
    att_mus = models.CharField("Avez-vous été ou êtes-vous atteint(e) de tendinites, problèmes articulaires, musculaires ?", max_length=1, choices=CHOICES)
    sub_car = models.CharField("Avez-vous précédemment subi un éléctrocardiogramme ?", max_length=1, choices=CHOICES)
    sub_enc = models.CharField("Avez-vous précédemment subi un éléctroencéphalogramme ?", max_length=1, choices=CHOICES)
    trait_med = models.CharField("Avez-vous précédemment été traité(e) par des médicaments pendant une longue période ?", max_length=1, choices=CHOICES)
    pre_2 = models.CharField("Si oui, précisez ?", max_length=300, null=True)
    prat = models.CharField("Pratiquez-vous régulièrement une ou plusieurs activités physiques ?", max_length=1, choices=CHOICES)
    pre_3 = models.CharField("Si oui le(s) quel(s) ?", max_length=300)
    cons_al = models.CharField("Consommez-vous régulièrement de l'alcool, du vin, de la bière ?", max_length=1, choices=CHOICES)
    cons_tab = models.CharField("Consommez-vous régulièrement du tabac ?", max_length=1, choices=CHOICES)
    cons_med = models.CharField("Consommez-vous régulièrement des médicaments ?", max_length=1, choices=CHOICES)
    pre_4 = models.CharField("Si oui, lesquels ?", max_length=300, null=True)
    cons_drog = models.CharField("Consommez-vous régulièrement des drogues, stupéfiants ?", max_length=1, choices=CHOICES)
    pre_5 = models.CharField("Si oui, lesquels ?", max_length=300, null=True)
    inv = models.CharField("Une ou des invalidités ou incapacités permanentes vous sont-elles reconnues ?", max_length=1, choices=CHOICES)
    pre_6 = models.CharField("Si oui, quels en sont les taux ?", max_length=300, null=True)
    vac_tet = models.CharField("Etes-vous vacciné contre le tétanos ?", max_length=1, choices=CHOICES)
    vac_ha = models.CharField("Etes-vous vacciné contre l'hépatite A ?", max_length=1, choices=CHOICES)
    vac_hb = models.CharField("Etes-vous vacciné contre l'hépatite B ?", max_length=1, choices=CHOICES)
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.agent
        
    class Meta:
        verbose_name = "Antécédents de santé"
