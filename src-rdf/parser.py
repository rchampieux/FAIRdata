

filename="in/FAIR_Landscape_V1.0.0-Evaluation.tsv";

import rdflib

from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC
from rdflib.namespace import XSD

FAIRURL=""
EMPTY_STRING="unk" # what to do with empty strings?

FAIR = Namespace(FAIRURL)
g = Graph()

# Set up the Principles (columns of the curated spreadsheet)

# Findable
g.add( (Literal("FAIR.findablePrinciple"), RDF.type, Literal("FAIR.principle")) )
## requirements
g.add( (Literal("FAIR.F1Requirement"), RDF.type, Literal("FAIR.requirement")) )
g.add( (Literal("FAIR.F2Requirement"), RDF.type, Literal("FAIR.requirement")) )
g.add( (Literal("FAIR.F3Requirement"), RDF.type, Literal("FAIR.requirement")) )
g.add( (Literal("FAIR.F4Requirement"), RDF.type, Literal("FAIR.requirement")) )
## set forward and backwards pointers
g.add( (Literal("FAIR.findablePrinciple"), DC.hasPart, Literal("FAIR.F1Requirement")) )
g.add( (Literal("FAIR.F1Requirement"), DC.isPartOf, Literal("FAIR.findablePrinciple")) )
g.add( (Literal("FAIR.findablePrinciple"), DC.hasPart, Literal("FAIR.F2Requirement")) )
g.add( (Literal("FAIR.F2Requirement"), DC.isPartOf, Literal("FAIR.findablePrinciple")) )
g.add( (Literal("FAIR.findablePrinciple"), DC.hasPart, Literal("FAIR.F3Requirement")) )
g.add( (Literal("FAIR.F3Requirement"), DC.isPartOf, Literal("FAIR.findablePrinciple")) )
g.add( (Literal("FAIR.findablePrinciple"), DC.hasPart, Literal("FAIR.F4Requirement")) )
g.add( (Literal("FAIR.F4Requirement"), DC.isPartOf, Literal("FAIR.findablePrinciple")) )

# Accessible
g.add( (Literal("FAIR.accessiblePrinciple"), RDF.type, Literal("FAIR.principle")) )
## requirements
g.add( (Literal("FAIR.A1Requirement"), RDF.type, Literal("FAIR.requirement")) )
g.add( (Literal("FAIR.A1_1Requirement"), RDF.type, Literal("FAIR.requirement")) )
g.add( (Literal("FAIR.A1_2Requirement"), RDF.type, Literal("FAIR.requirement")) )
g.add( (Literal("FAIR.A2Requirement"), RDF.type, Literal("FAIR.requirement")) )
## set forward and backwards pointers
g.add( (Literal("FAIR.accessiblePrinciple"), DC.hasPart, Literal("FAIR.A1Requirement")) )
g.add( (Literal("FAIR.A1Requirement"), DC.isPartOf, Literal("FAIR.accessiblePrinciple")) )
g.add( (Literal("FAIR.accessiblePrinciple"), DC.hasPart, Literal("FAIR.A1_1Requirement")) )
g.add( (Literal("FAIR.A1_1Requirement"), DC.isPartOf, Literal("FAIR.accessiblePrinciple")) )
g.add( (Literal("FAIR.accessiblePrinciple"), DC.hasPart, Literal("FAIR.A1_2Requirement")) )
g.add( (Literal("FAIR.A1_2Requirement"), DC.isPartOf, Literal("FAIR.accessiblePrinciple")) )
g.add( (Literal("FAIR.accessiblePrinciple"), DC.hasPart, Literal("FAIR.A2Requirement")) )
g.add( (Literal("FAIR.A2Requirement"), DC.isPartOf, Literal("FAIR.accessiblePrinciple")) )

# Interoperable
g.add( (Literal("FAIR.interoperablePrinciple"), RDF.type, Literal("FAIR.principle")) )
## requirements
g.add( (Literal("FAIR.I1Requirement"), RDF.type, Literal("FAIR.requirement")) )
g.add( (Literal("FAIR.I2Requirement"), RDF.type, Literal("FAIR.requirement")) )
g.add( (Literal("FAIR.I3Requirement"), RDF.type, Literal("FAIR.requirement")) )
## set forward and backwards pointers
g.add( (Literal("FAIR.interoperablePrinciple"), DC.hasPart, Literal("FAIR.I1Requirement")) )
g.add( (Literal("FAIR.I1Requirement"), DC.isPartOf, Literal("FAIR.interoperablePrinciple")) )
g.add( (Literal("FAIR.interoperablePrinciple"), DC.hasPart, Literal("FAIR.I2Requirement")) )
g.add( (Literal("FAIR.I2Requirement"), DC.isPartOf, Literal("FAIR.interoperablePrinciple")) )
g.add( (Literal("FAIR.interoperablePrinciple"), DC.hasPart, Literal("FAIR.I3Requirement")) )
g.add( (Literal("FAIR.I3Requirement"), DC.isPartOf, Literal("FAIR.interoperablePrinciple")) )

# Reusable
g.add( (Literal("FAIR.reusablePrinciple"), RDF.type, Literal("FAIR.principle")) )
## requirements
g.add( (Literal("FAIR.R1Requirement"), RDF.type, Literal("FAIR.requirement")) )
g.add( (Literal("FAIR.R1_1Requirement"), RDF.type, Literal("FAIR.requirement")) )
g.add( (Literal("FAIR.R1_2Requirement"), RDF.type, Literal("FAIR.requirement")) )
g.add( (Literal("FAIR.R1_3Requirement"), RDF.type, Literal("FAIR.requirement")) )
## set forward and backwards pointers
g.add( (Literal("FAIR.reusablePrinciple"), DC.hasPart, Literal("FAIR.R1Requirement")) )
g.add( (Literal("FAIR.R1Requirement"), DC.isPartOf, Literal("FAIR.reusablePrinciple")) )
g.add( (Literal("FAIR.reusablePrinciple"), DC.hasPart, Literal("FAIR.R1_1Requirement")) )
g.add( (Literal("FAIR.R1_1Requirement"), DC.isPartOf, Literal("FAIR.reusablePrinciple")) )
g.add( (Literal("FAIR.reusablePrinciple"), DC.hasPart, Literal("FAIR.R1_2Requirement")) )
g.add( (Literal("FAIR.R1_2Requirement"), DC.isPartOf, Literal("FAIR.reusablePrinciple")) )
g.add( (Literal("FAIR.reusablePrinciple"), DC.hasPart, Literal("FAIR.R1_Requirement")) )
g.add( (Literal("FAIR.R1_3Requirement"), DC.isPartOf, Literal("FAIR.reusablePrinciple")) )


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
    rubricName=Literal(line[0])
    if(rubricName in rubrics):
      # xxx check for consistency
      rubricID=rubrics[rubricName]
    else:
      rubricID=rubricName # xxx this is more readable, but will it work?
      rubrics[rubricName]=rubricID
      g.add( (rubricID, RDF.type, Literal("FAIR.rubric") ) )
      g.add( (rubricName, RDF.type, Literal("FAIR.rubricTitle") ) )
      g.add( (rubricID, FAIR.hasTitle, rubricName) )
      g.add( (rubricName, FAIR.hasID, rubricID) )
      #
      authorNames=Literal(line[1])
      g.add( (authorNames, RDF.type, Literal("FAIR.Authors") ) )
      g.add( (rubricID, FAIR.createdBy, authorNames) )
      #
      contactName=Literal(line[2])
      g.add( (contactName, RDF.type, Literal("FAIR.Contact") ) )
      g.add( (rubricID, FAIR.isContactFor, contactName) )
      #      
      versionName=Literal(line[3])
      g.add( (versionName, RDF.type, Literal("FAIR.version") ) )
      g.add( (rubricID, DC.hasVersion, versionName) )
      #      
      # xxx provenance? citedBy? 
      websiteName=Literal(line[4])
      g.add( (websiteName, RDF.type, Literal("FAIR.website") ) )
      g.add( (rubricID, FAIR.hasWebsite, websiteName) )
      #      

      licenseName=Literal(line[5])
      if(licenseName in licenses):
        # xxx check for consistency
        y=1
      else: 
        licenses.append(licenseName)
        licenseType = Literal(line[6])
        # xxx check if license already has a type, otherwise set it 
        g.add( (licenseName, RDF.type, DC.license) )
        g.add( (licenseType, RDF.type, Literal("FAIR.licenseType") ) )
        # xxx subclass it 
        # g.add( license, RDF.class, licenseType) # xxx
        #      
      g.add( (Literal(line[7]), RDF.type, Literal("FAIR.certificationMethod") ) )
      g.add( (rubricID, FAIR.hasCertificationMethod, Literal(line[7])) )
      #      
      methodName=Literal(line[8])
      g.add( (methodName, RDF.type, Literal("FAIR.scoringMethod") ) )
      g.add( (rubricID, FAIR.hasScoringMethod, methodName) )
      #      
      outputName=Literal(line[9])
      g.add( (outputName, RDF.type, Literal("FAIR.scoringOutput") ) )
      g.add( (rubricID, FAIR.hasScoringOutput, outputName) )
      #      
      g.add( (Literal(line[10]), RDF.type, Literal("FAIR.implementationEvidence") ) )
      g.add( (rubricID, FAIR.hasImplementationEvidence, Literal(line[10])) )
      #      
      g.add( (Literal(line[11]), RDF.type, Literal("FAIR.communityFocus") ) )
      g.add( (rubricID, FAIR.hasCommunityFocus, Literal(line[11])) )
      #
    # criteria
    criterionName=Literal(line[12])
    criterionID=criterionName # xxx this is more readable, but will it work?
    g.add( (criterionID, RDF.type, Literal("FAIR.criterion") ) )
    g.add( (criterionName, RDF.type, Literal("FAIR.criterionTitle") ) )
    g.add( (criterionID, FAIR.hasTitle, criterionName) )
    g.add( (criterionName, FAIR.hasID, criterionID) )
    g.add( (rubricID, DC.hasPart, criterionID) )
    g.add( (criterionID, DC.isPartOf, rubricID) )
    #
    codeName=Literal(line[13])
    g.add( (codeName, RDF.type, Literal("FAIR.criterionCode") ) )
    g.add( (criterionID, FAIR.hasCode, codeName) )
    #
    otherID=Literal(line[14])
    g.add( (otherID, RDF.type, Literal("FAIR.criterionOtherID") ) )
    g.add( (criterionID, FAIR.hasOtherID, otherID) )
    #
    measurementMethod=Literal(line[15])
    g.add( (measurementMethod, RDF.type, Literal("FAIR.criterionMeasurementMethod") ) )
    g.add( (criterionID, FAIR.hasMeasurementMethod, measurementMethod) )
    #
    resourceType=Literal(line[16])
    g.add( (resourceType, RDF.type, Literal("FAIR.criterionResourceType") ) )
    g.add( (criterionID, FAIR.hasResourceType, resourceType) )
    #
    # xxx check for consistency
    mapped=EMPTY_STRING
    if line[17] == "1":
      mapped=0;
    hasMapping=Literal(line[17])
    g.add( (hasMapping, RDF.type, Literal("FAIR.mappingType") ) )
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
      g.add( (criterionID, FAIR.mapsToRequirement, Literal("FAIR.F1Requirement") ) )
      aligned = 1
    if line[20] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, Literal("FAIR.F2Requirement") ) )
      aligned = 1
    if line[21] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, Literal("FAIR.F3Requirement") ) )
      aligned = 1
    if line[22] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, Literal("FAIR.F4Requirement") ) )
      aligned = 1
    #
    if aligned == 1:
      g.add( (criterionID, FAIR.isAlignedWith, Literal("FAIR.findablePrinciple") ) )
    #
    aligned=0
    if line[23] == "1":
      # A Aligned, no requirement mapping
      aligned = 1
    if line[24] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, Literal("FAIR.A1Requirement") ) )
      aligned = 1
    if line[25] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, Literal("FAIR.A1_1Requirement") ) )
      aligned = 1
    if line[26] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, Literal("FAIR.A1_2Requirement") ) )
      aligned = 1
    if line[27] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, Literal("FAIR.A2Requirement") ) )
      aligned = 1
     #
    if aligned == 1:
      g.add( (criterionID, FAIR.isAlignedWith, Literal("FAIR.accessiblePrinciple") ) )
    #
    aligned=0
    if line[28] == "1":
      # I Aligned, no requirement mapping
      aligned = 1
    if line[29] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, Literal("FAIR.I1Requirement") ) )
      aligned = 1
    if line[30] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, Literal("FAIR.I2Requirement") ) )
      aligned = 1
    if line[31] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, Literal("FAIR.I3Requirement") ) )
      aligned = 1
    #
    if aligned == 1:
      g.add( (criterionID, FAIR.isAlignedWith, Literal("FAIR.interoperablePrinciple") ) )
    #
    aligned=0
    if line[32] == "1":
      # R Aligned, no requirement mapping
      aligned = 1
    if line[33] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, Literal("FAIR.R1Requirement") ) )
      aligned = 1
    if line[34] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, Literal("FAIR.R1_1Requirement")) )
      aligned = 1
    if line[35] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, Literal("FAIR.R1_2Requirement") ) )
      aligned = 1
    if line[36] == "1":
      g.add( (criterionID, FAIR.mapsToRequirement, Literal("FAIR.R1_3Requirement") ) )
      aligned = 1
    if aligned == 1:
      g.add( (criterionID, FAIR.isAlignedWith, Literal("FAIR.reusablePrinciple") ) )
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

#print(g.serialize(format='xml').decode('UTF-8'))
#print(g.serialize(format='turtle'))
print( g.serialize(format='n3') )
