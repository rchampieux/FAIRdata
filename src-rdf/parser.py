#!/home/ubuntu/.conda/envs/rdf/bin/python

filename="in/FAIR_Landscape_V1.0.0-Evaluation.tsv";

import rdflib

from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC

FAIRURL="http://example.org/fair/"
EMPTY_STRING="unk" # what to do with empty strings?

FAIR = Namespace(FAIRURL)
g = Graph()

# Set up the Principles (columns of the curated spreadsheet)

# Findable
g.add( (FAIR.findablePrinciple, RDF.type, FAIR.principle) )
## requirements
g.add( (FAIR.F1Requirement, RDF.type, FAIR.requirement) )
g.add( (FAIR.F2Requirement, RDF.type, FAIR.requirement) )
g.add( (FAIR.F3Requirement, RDF.type, FAIR.requirement) )
g.add( (FAIR.F4Requirement, RDF.type, FAIR.requirement) )
## set forward and backwards pointers
g.add( (FAIR.findablePrinciple, DC.hasPart, FAIR.F1Requirement) )
g.add( (FAIR.F1Requirement, DC.isPartOf, FAIR.findablePrinciple) )
g.add( (FAIR.findablePrinciple, DC.hasPart, FAIR.F2Requirement) )
g.add( (FAIR.F2Requirement, DC.isPartOf, FAIR.findablePrinciple) )
g.add( (FAIR.findablePrinciple, DC.hasPart, FAIR.F3Requirement) )
g.add( (FAIR.F3Requirement, DC.isPartOf, FAIR.findablePrinciple) )
g.add( (FAIR.findablePrinciple, DC.hasPart, FAIR.F4Requirement) )
g.add( (FAIR.F4Requirement, DC.isPartOf, FAIR.findablePrinciple) )

# Accessible
g.add( (FAIR.accessiblePrinciple, RDF.type, FAIR.principle) )
## requirements
g.add( (FAIR.A1Requirement, RDF.type, FAIR.requirement) )
g.add( (FAIR.A1_1Requirement, RDF.type, FAIR.requirement) )
g.add( (FAIR.A1_2Requirement, RDF.type, FAIR.requirement) )
g.add( (FAIR.A2Requirement, RDF.type, FAIR.requirement) )
## set forward and backwards pointers
g.add( (FAIR.accessiblePrinciple, DC.hasPart, FAIR.A1Requirement) )
g.add( (FAIR.A1Requirement, DC.isPartOf, FAIR.accessiblePrinciple) )
g.add( (FAIR.accessiblePrinciple, DC.hasPart, FAIR.A1_1Requirement) )
g.add( (FAIR.A1_1Requirement, DC.isPartOf, FAIR.accessiblePrinciple) )
g.add( (FAIR.accessiblePrinciple, DC.hasPart, FAIR.A1_2Requirement) )
g.add( (FAIR.A1_2Requirement, DC.isPartOf, FAIR.accessiblePrinciple) )
g.add( (FAIR.accessiblePrinciple, DC.hasPart, FAIR.A2Requirement) )
g.add( (FAIR.A2Requirement, DC.isPartOf, FAIR.accessiblePrinciple) )

# Interoperable
g.add( (FAIR.interoperablePrinciple, RDF.type, FAIR.principle) )
## requirements
g.add( (FAIR.I1Requirement, RDF.type, FAIR.requirement) )
g.add( (FAIR.I2Requirement, RDF.type, FAIR.requirement) )
g.add( (FAIR.I3Requirement, RDF.type, FAIR.requirement) )
## set forward and backwards pointers
g.add( (FAIR.interoperablePrinciple, DC.hasPart, FAIR.I1Requirement) )
g.add( (FAIR.I1Requirement, DC.isPartOf, FAIR.interoperablePrinciple) )
g.add( (FAIR.interoperablePrinciple, DC.hasPart, FAIR.I2Requirement) )
g.add( (FAIR.I2Requirement, DC.isPartOf, FAIR.interoperablePrinciple) )
g.add( (FAIR.interoperablePrinciple, DC.hasPart, FAIR.I3Requirement) )
g.add( (FAIR.I3Requirement, DC.isPartOf, FAIR.interoperablePrinciple) )

# Reusable
g.add( (FAIR.reusablePrinciple, RDF.type, FAIR.principle) )
## requirements
g.add( (FAIR.R1Requirement, RDF.type, FAIR.requirement) )
g.add( (FAIR.R1_1Requirement, RDF.type, FAIR.requirement) )
g.add( (FAIR.R1_2Requirement, RDF.type, FAIR.requirement) )
g.add( (FAIR.R1_3Requirement, RDF.type, FAIR.requirement) )
## set forward and backwards pointers
g.add( (FAIR.reusablePrinciple, DC.hasPart, FAIR.R1Requirement) )
g.add( (FAIR.R1Requirement, DC.isPartOf, FAIR.reusablePrinciple) )
g.add( (FAIR.reusablePrinciple, DC.hasPart, FAIR.R1_1Requirement) )
g.add( (FAIR.R1_1Requirement, DC.isPartOf, FAIR.reusablePrinciple) )
g.add( (FAIR.reusablePrinciple, DC.hasPart, FAIR.R1_2Requirement) )
g.add( (FAIR.R1_2Requirement, DC.isPartOf, FAIR.reusablePrinciple) )
g.add( (FAIR.reusablePrinciple, DC.hasPart, FAIR.R1_Requirement) )
g.add( (FAIR.R1_3Requirement, DC.isPartOf, FAIR.reusablePrinciple) )


import csv
import uuid
import urllib.parse
rubrics=dict()
licenses=[]
with open(filename) as tsvfile:
  reader=csv.reader(tsvfile, delimiter='\t')
  x=next(reader) # skip first 4 lines
  x=next(reader) # skip first 4 lines
  x=next(reader) # skip first 4 lines
  x=next(reader) # skip first 4 lines
  for line in reader:
    rubricName=rdflib.term.URIRef(FAIRURL+(urllib.parse.urlencode({"title":line[0]})))
    if(rubricName in rubrics):
      # xxx check for consistency
      rubricID=rubrics[rubricName]
    else:
      rubricID=rdflib.term.URIRef(FAIRURL+str(uuid.uuid4()))
      rubrics[rubricName]=rubricID
      g.add( (rubricID, RDF.type, FAIR.rubric) )
      g.add( (rubricName, RDF.type, FAIR.rubricTitle) )
      g.add( (rubricID, FAIR.hasTitle, rubricName) )
      g.add( (rubricName, FAIR.hasID, rubricID) )
      #
      authorNames=rdflib.term.URIRef(FAIRURL+(urllib.parse.urlencode({"authors":line[1]})))
      g.add( (authorNames, RDF.type, FAIR.Authors) )
      g.add( (rubricID, FAIR.createdBy, authorNames) )
      #
      contactName=rdflib.term.URIRef(FAIRURL+(urllib.parse.urlencode({"contact":line[2]})))
      g.add( (contactName, RDF.type, FAIR.Contact) )
      g.add( (rubricID, FAIR.isContactFor, contactName) )
      #      
      versionName=rdflib.term.URIRef(FAIRURL+(urllib.parse.urlencode({"version":line[3]})))
      g.add( (versionName, RDF.type, FAIR.version) )
      g.add( (rubricID, DC.hasVersion, versionName) )
      #      
      # xxx provenance? citedBy? 
      websiteName=rdflib.term.URIRef(FAIRURL+(urllib.parse.urlencode({"website":line[4]})))
      g.add( (websiteName, RDF.type, FAIR.website) )
      g.add( (rubricID, FAIR.hasWebsite, websiteName) )
      #      

      licenseName=rdflib.term.URIRef(FAIRURL+(urllib.parse.urlencode({"license":line[5]})))
      if(licenseName in licenses):
        # xxx check for consistency
        y=1
      else: 
        licenses.append(licenseName)
        licenseType = rdflib.term.URIRef(FAIRURL+line[6])
        # xxx check if license already has a type, otherwise set it 
        g.add( (licenseName, RDF.type, DC.license) )
        g.add( (licenseType, RDF.type, FAIR.licenseType) )
        # xxx subclass it 
        # g.add( license, RDF.class, licenseType) # xxx
        #      
      g.add( (rdflib.term.URIRef(FAIRURL+line[7]), RDF.type, FAIR.certificationMethod) )
      g.add( (rubricID, FAIR.hasCertificationMethod, rdflib.term.URIRef(FAIRURL+line[7])) )
      #      
      methodName=rdflib.term.URIRef(FAIRURL+(urllib.parse.urlencode({"scoringMethod":line[8]})))
      g.add( (methodName, RDF.type, FAIR.scoringMethod) )
      g.add( (rubricID, FAIR.hasScoringMethod, methodName) )
      #      
      outputName=rdflib.term.URIRef(FAIRURL+(urllib.parse.urlencode({"scoringOutput":line[9]})))
      g.add( (outputName, RDF.type, FAIR.scoringOutput) )
      g.add( (rubricID, FAIR.hasScoringOutput, outputName) )
      #      
      g.add( (rdflib.term.URIRef(FAIRURL+line[10]), RDF.type, FAIR.implementationEvidence) )
      g.add( (rubricID, FAIR.hasImplementationEvidence, rdflib.term.URIRef(FAIRURL+line[10])) )
      #      
      g.add( (rdflib.term.URIRef(FAIRURL+line[11]), RDF.type, FAIR.communityFocus) )
      g.add( (rubricID, FAIR.hasCommunityFocus, rdflib.term.URIRef(FAIRURL+line[11])) )
      #
    # criteria
    criterionName=rdflib.term.URIRef(FAIRURL+(urllib.parse.urlencode({"criterionTitle":line[12]})))
    criterionID=rdflib.term.URIRef(FAIRURL+str(uuid.uuid4()))
    g.add( (criterionID, RDF.type, FAIR.criterion) )
    g.add( (criterionName, RDF.type, FAIR.criterionTitle) )
    g.add( (criterionID, FAIR.hasTitle, criterionName) )
    g.add( (criterionName, FAIR.hasID, criterionID) )
    g.add( (rubricID, DC.hasPart, criterionID) )
    g.add( (criterionID, DC.isPartOf, rubricID) )
    #
    codeName=rdflib.term.URIRef(FAIRURL+(urllib.parse.urlencode({"code":line[13]})))
    g.add( (codeName, RDF.type, FAIR.criterionCode) )
    g.add( (criterionID, FAIR.hasCode, codeName) )
    #
    otherID=rdflib.term.URIRef(FAIRURL+(urllib.parse.urlencode({"criterionOtherID":line[14]})))
    g.add( (otherID, RDF.type, FAIR.criterionOtherID) )
    g.add( (criterionID, FAIR.hasOtherID, otherID) )
    #
    measurementMethod=rdflib.term.URIRef(FAIRURL+(urllib.parse.urlencode({"measurementMethod":line[15]})))
    g.add( (measurementMethod, RDF.type, FAIR.criterionMeasurementMethod) )
    g.add( (criterionID, FAIR.hasMeasurementMethod, measurementMethod) )
    #
    resourceType=rdflib.term.URIRef(FAIRURL+(urllib.parse.urlencode({"resourceType":line[16]})))
    g.add( (resourceType, RDF.type, FAIR.criterionResourceType) )
    g.add( (criterionID, FAIR.hasResourceType, resourceType) )
    #
    # xxx check for consistency
    mapped=EMPTY_STRING
    if line[17] == "1":
      mapped=0;
    hasMapping=rdflib.term.URIRef(FAIRURL+(urllib.parse.urlencode({"hasMapping":line[17]})))
    g.add( (hasMapping, RDF.type, FAIR.mappingdType) )
    g.add( (criterionID, FAIR.isMapped, hasMapping) )
    #
    #
    # xxx this is tricky might want to embed more relationships in here
    hasAlignment=EMPTY_STRING
    #
    reqs=""
    aligned=0
    if line[18] == "1":
      # F Aligned, no requirement mapping
      aligned = 1
    if line[19] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, FAIR.F1Requirement) )
      aligned = 1
    if line[20] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, FAIR.F2Requirement) )
      aligned = 1
    if line[21] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, FAIR.F3Requirement) )
      aligned = 1
    if line[22] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, FAIR.F4Requirement) )
      aligned = 1
    #
    if aligned == 1:
      g.add( (criterionID, FAIR.isAlignedWith, FAIR.findablePrinciple) )
    #
    aligned=0
    if line[23] == "1":
      # A Aligned, no requirement mapping
      aligned = 1
    if line[24] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, FAIR.A1Requirement) )
      aligned = 1
    if line[25] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, FAIR.A1_1Requirement) )
      aligned = 1
    if line[26] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, FAIR.A1_2Requirement) )
      aligned = 1
    if line[27] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, FAIR.A2Requirement) )
      aligned = 1
     #
    if aligned == 1:
      g.add( (criterionID, FAIR.isAlignedWith, FAIR.accessiblePrinciple) )
    #
    aligned=0
    if line[28] == "1":
      # I Aligned, no requirement mapping
      aligned = 1
    if line[29] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, FAIR.I1Requirement) )
      aligned = 1
    if line[30] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, FAIR.I2Requirement) )
      aligned = 1
    if line[31] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, FAIR.I3Requirement) )
      aligned = 1
    #
    if aligned == 1:
      g.add( (criterionID, FAIR.isAlignedWith, FAIR.interoperablePrinciple) )
    #
    aligned=0
    if line[32] == "1":
      # R Aligned, no requirement mapping
      aligned = 1
    if line[33] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, FAIR.R1Requirement) )
      aligned = 1
    if line[34] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, FAIR.R1_1Requirement) )
      aligned = 1
    if line[35] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, FAIR.R1_2Requirement) )
      aligned = 1
    if line[36] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, FAIR.R1_3Requirement) )
      aligned = 1
    if aligned == 1:
      g.add( (criterionID, FAIR.isAlignedWith, FAIR.reusablePrinciple) )
    # xxx what about 'there is a comment'?


if 0:
  # print all triples
  print("--- printing raw triples ---")
  for s, p, o in g:
      print((s, p, o))

  # print the types
  print("------")
  for s,p,o in g.triples( (None, RDF.type, FAIR.principle) ):
     print("%s is a principle"%s)

  print("------")
  for s,p,o in g.triples( (None, RDF.type, FAIR.requirement) ):
     print("%s is a requirement"%s)

  print("------")
  for s,p,o in g.triples( (None, RDF.type, FAIR.rubricTitle) ):
     print("%s is a rubricTitle"%s)

  print("------")
  for s,p,o in g.triples( (None, RDF.type, FAIR.criteria) ):
     print("%s is a criterion"%s)

  print("------")

  # For each FAIR:rubric in the store print out its criteria
  for rubricID in g.subjects(RDF.type, FAIR.rubric):
    print("------rubricID=")
    print(rubricID)
    print("------title=")
    for title in g.objects(rubricID, FAIR.hasTitle):
        print(title)
    print("------criteria=")
    for criterion in g.objects(rubricID, DC.hasPart):
        print(criterion)

  print()
  # For each criterion, print out its rubrics
  for criterion in g.subjects(RDF.type, FAIR.criteria):
    print("------Criterion=")
    print(criterion)
    print("------Rubrics=")
    for rubric in g.objects(criterion, DC.isPartOf):
        print(rubric)

  print()

# Bind a few prefix, namespace pairs for more readable output
g.bind("dc", DC)
g.bind("fair", FAIR)

print(g.serialize(format='xml').decode('UTF-8'))
#print(g.serialize(format='turtle'))
#print( g.serialize(format='n3') )
