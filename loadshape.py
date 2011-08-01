import os,sys
sys.path.append('/Users/tlane2/Code/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.contrib.gis.utils import LayerMapping
from zones.models import Counties



# Auto-generated `LayerMapping` dictionary for SchoolDistricts model
"""schooldisctricts_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'unsd_field' : 'UNSD_',
    'unsd_id' : 'UNSD_ID',
    'statefp' : 'STATEFP',
    'statens' : 'STATENS',
    'unsdlea' : 'UNSDLEA',
    'unsdidfp' : 'UNSDIDFP',
    'name' : 'NAME',
    'lsad' : 'LSAD',
    'lograde' : 'LOGRADE',
    'higrade' : 'HIGRADE',
    'mtfcc' : 'MTFCC',
    'sdtyp' : 'SDTYP',
    'funcstat' : 'FUNCSTAT',
    'aland' : 'ALAND',
    'awater' : 'AWATER',
    'intptlat' : 'INTPTLAT',
    'intptlon' : 'INTPTLON',
    'geom' : 'POLYGON',
}"""
# Auto-generated `LayerMapping` dictionary for County model
# Auto-generated `LayerMapping` dictionary for Counties model
counties_mapping = {
    'countyname' : 'COUNTYNAME',
    'countyfips' : 'COUNTYFIPS',
    'countygnis' : 'COUNTYGNIS',
    'name_ucase' : 'NAME_UCASE',
    'pop_1990' : 'POP_1990',
    'pop_2000' : 'POP_2000',
    'acres' : 'ACRES',
    'sq_miles' : 'SQ_MILES',
    'cnty_seat' : 'CNTY_SEAT',
    'co_class' : 'CO_CLASS',
    'geom' : 'MULTIPOLYGON',
}

"""schools_mapping = {
    'ctydist' : 'CtyDist',
    'schnum' : 'SchNum',
    'schid' : 'SchID',
    'facility' : 'Facility',
    'address' : 'Address',
    'address2' : 'Address2',
    'city' : 'City',
    'state' : 'State',
    'zip_code' : 'ZIP',
    'county' : 'County',
    'phone' : 'Phone',
    'fax' : 'FAX',
    'bgrade' : 'BGrade',
    'egrade' : 'EGrade',
    'principal' : 'Principal',
    'printitle' : 'PrinTitle',
    'teachers' : 'Teachers',
    'enrollment' : 'Enrollment',
    'schemail' : 'SchEmail',
    'latitude' : 'Latitude',
    'longitude' : 'Longitude',
    'loc_code' : 'Loc_Code',
    'geom' : 'POINT',
}"""
# Auto-generated `LayerMapping` dictionary for ZipCodes model
"""zipcodes_mapping = {
    'zcta5ce' : 'ZCTA5CE',
    'classfp' : 'CLASSFP',
    'mtfcc' : 'MTFCC',
    'funcstat' : 'FUNCSTAT',
    'geom' : 'MULTIPOLYGON',
}"""





#zipcodes_shp = os.path.abspath('/Users/tlane2/Code/crime/data/tl_2008_us_zcta5.shp')
counties_shp = os.path.abspath('/Users/tlane2/Code/crime/data/COUNTY.shp')
def run( verbose=True ):
	lm = LayerMapping(Counties, counties_shp, counties_mapping,transform=False )
	lm.save( strict=True, verbose=verbose )

run()