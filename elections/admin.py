from django.contrib.gis import admin
from models import Candidate,Race,RaceConfig,Party,BallotInitiative,Election,Office

class CandidateAdmin( admin.ModelAdmin ):
	pass

class RaceAdmin( admin.ModelAdmin ):
	pass

class RaceInline( admin.TabularInline ):
	model = Race
	
class RaceConfigAdmin( admin.ModelAdmin ):
	inlines = [
		RaceInline,
	]

class PartyAdmin( admin.ModelAdmin ):
	pass

class BallotInitiativeAdmin( admin.ModelAdmin ):
	pass

class ElectionAdmin( admin.ModelAdmin ):
	pass

class OfficeAdmin( admin.ModelAdmin ):
	pass
	


	
admin.site.register( Candidate, CandidateAdmin )
admin.site.register( Race, RaceAdmin )
admin.site.register( RaceConfig, RaceConfigAdmin )
admin.site.register( Party, PartyAdmin )
admin.site.register( BallotInitiative, BallotInitiativeAdmin )
admin.site.register( Election, ElectionAdmin )
admin.site.register( Office, OfficeAdmin )

