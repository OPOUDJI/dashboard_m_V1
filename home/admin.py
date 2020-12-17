from django.contrib import admin
from .models import Mere, Pere, Frere, Soeur, Enfant, Qualif, Agent, Details_banc, Conjoint, Passeport, Carte_ident, Ant_sante

class AgentQualif(admin.TabularInline):
    model = Agent.qualifications.through
    extra = 1
    verbose_name = "Qualification"
    verbose_name_plural = "Qualifications"

class AgentEnfant(admin.TabularInline):
    model = Agent.enfants.through
    extra = 1
    verbose_name = "Enfant"
    verbose_name_plural = "Enfants"

class AgentFrere(admin.TabularInline):
    model = Agent.freres.through
    extra = 1
    verbose_name = "Frère"
    verbose_name_plural = "Frères"


class AgentSoeur(admin.TabularInline):
    model = Agent.soeurs.through
    extra = 1
    verbose_name = "Soeur"
    verbose_name_plural = "Soeurs"


class AgentDetailsBanc(admin.TabularInline):
    model = Details_banc
    extra = 1
    verbose_name = "Détails bancaires"
    verbose_name_plural = "Détails bancaires"

class AgentAntSante(admin.TabularInline):
    model = Ant_sante
    extra = 1
    verbose_name = "Antécedents de santé"
    verbose_name_plural = "Antécedents de santé"

class AgentConjoint(admin.TabularInline):
    model = Conjoint
    extra = 1
    verbose_name = "Conjoint"
    verbose_name_plural = "Conjoints"

class AgentPasseport(admin.TabularInline):
    model = Passeport
    extra = 1
    verbose_name = "Passeport"
    verbose_name_plural = "Passeports"

class AgentCarteIdent(admin.TabularInline):
    model = Carte_ident
    extra = 1
    verbose_name = "Carte d'identité"
    verbose_name_plural = "Cartes d'identité"


class PereMereAgent(admin.TabularInline):
    model = Agent
    extra = 1
    verbose_name = "Agent"
    verbose_name_plural = "Agents"

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    inlines = [AgentConjoint, AgentEnfant, AgentFrere, AgentSoeur, AgentQualif, AgentDetailsBanc, AgentCarteIdent, AgentPasseport, AgentAntSante, ]
    search_fields = ['n_matricule', 'nom', 'prenom']

@admin.register(Mere)
class MereAdmin(admin.ModelAdmin):
    inlines = [PereMereAgent,]
    search_fields = [ 'nom', 'prenom']

@admin.register(Pere)
class PereAdmin(admin.ModelAdmin):
    inlines = [PereMereAgent,]
    search_fields = [ 'nom', 'prenom']

admin.site.register(Frere)

admin.site.register(Soeur)

admin.site.register(Enfant)

admin.site.register(Qualif)

admin.site.register(Details_banc)

admin.site.register(Conjoint)

admin.site.register(Passeport)

admin.site.register(Carte_ident)

admin.site.register(Ant_sante)

