# FEMA API thing for Civis Analytics 
#Nolan Winkler August 3rd, 2016

from urllib2 import urlopen
import requests
from json import load
import csv

#Get our the disasters records from FEMA
url = 'http://www.fema.gov/api/open' #API endpoint
#extract the first 5000 records for title, distasterNumber, incidentEndDate, and incidentBeginDate
param = '/v1/DisasterDeclarationsSummaries' + '?' + '$top=5000' + '&$select=title,distasterNumber,incidentEndDate,incidentBeginDate'
outputFormat = "&$format=json"

#combine & GET
response = urlopen(url + param + outputFormat)
#load
json_obj = load(response)

#write to a CSV file..



