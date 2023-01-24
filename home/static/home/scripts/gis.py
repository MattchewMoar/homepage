#Script to connect to an ArcGIS Server and get the list of services
#and their properties

import sys
import arcgis

#Connect to the ArcGIS Server
print("Connecting to ArcGIS Server...")
api_token = 'AAPKc1d344f69e094823862ef2f539973a3a2IW8P-P5JdXF1-4JsmVMr3XpfuefE7HOTc8Ju6DjIK2yKKowGhUH8Y1Pw1dwWaMU'

gis = arcgis.GIS("https://www.arcgis.com", api_token)

#Connect to franklin county gis server
gis = arcgis.GIS("https://gis.franklincountyohio.gov/arcgis/rest/services", api_token)

#Get the list of services
services = gis.services
print(services)
