# bug: FM-F1A???

print("@prefix fair: <https://go-fair.org/schema/> .\n@prefix eval: <https://go-fair.org/data/> .\n@prefix schema: <http://schema.org/> .\n@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n@base <http://go-fair.org/data/> .\n");

filename="in/FAIR_Landscape_V1.0.0-Evaluation.tsv";
import csv
rubrics=[]
licenses=[]
with open(filename) as tsvfile:
  reader=csv.reader(tsvfile, delimiter='\t')
  x=next(reader) # skip first 4 lines
#  print(x);
  x=next(reader) # skip first 4 lines
#  print(x);
  x=next(reader) # skip first 4 lines
#  print(x);
#  x=next(reader) # skip first 4 lines
#  print(x);
  for line in reader:
    authors=""
    rubricName=line[0]
    rubric=rubricName.lower().replace(" ", "-");
    licenseName=line[5]
    if(rubricName not in rubrics):
      rubrics.append(rubricName)
      print("eval:"+rubric+" a fair:Rubric ;");
      print("    fair:communityFocus \""+line[11]+"\" ;");
      print("    fair:hasCertificationMethod "+line[7]+" ;");
      print("    fair:hasImplementationEvidence "+line[10]+" ;");
      print("    fair:hasScoringMethod "+line[8]+" ;");
      print("    fair:scoringOutput \""+line[9]+"\" ;");
      if(licenseName in licenses):
        y=1
      else: 
        licenses.append(licenseName)
        licenseType = line[6]
        print("    fair:licenseType \""+licenseType+"\" ;");
      authorNames=line[1].split(", ");
      for authorName in authorNames:
        author = authorName.lower().replace(" ", "-");
        print("    schema:author eval:"+author+" ;");
        authors = authors + "eval:"+author+" a schema:Person ;\n    schema:name \""+authorName+"\" ;\"\n.\n";
      print("    schema:license \""+licenseName+"\" ;");
      print("    schema:name \""+rubricName+"\" ;");
      print("    schema:version \""+line[3]+"\" ;");
      print("    schema:url <"+line[4]+"> ;");
      print(".");
      print(authors);

    # criteria


    alignmentStr=""
    hasNoDirectMapping=0;
    mapped="";
    if line[17] == "1":
      mapped=0;
    hasMapping=line[17]
    hasAlignment=""
    reqs=""
    aligned=0
    criterion = line[12].lower().replace(" ","-");
    print("eval:"+criterion+" a fair:Criterion ;");
    if line[18] == "1":
      # F Aligned, no requirement mapping
      aligned = 1
    if line[19] == "1":
      aligned = 1
      alignmentStr +="    fair:mapsTo fair:F1 ;\n";
    if line[20] == "1":
      aligned = 1
      alignmentStr +="    fair:mapsTo fair:F2 ;\n";
    if line[21] == "1":
      aligned = 1
      alignmentStr +="    fair:mapsTo fair:F3 ;\n";
    if line[22] == "1":
      aligned = 1
      alignmentStr +="    fair:mapsTo fair:F4 ;\n";
    #

#    if aligned == 1:
#      print("    fair:mapsTo fair:"++" ;")
#    aligned=0

    if line[23] == "1":
      # A Aligned, no requirement mapping
      aligned = 1
    if line[24] == "1":
      aligned = 1
      alignmentStr +="    fair:mapsTo fair:A1 ;\n";
    if line[25] == "1":
      aligned = 1
      alignmentStr +="    fair:mapsTo fair:A1_1 ;\n";
    if line[26] == "1":
      aligned = 1
      alignmentStr +="    fair:mapsTo fair:A1_2 ;\n";
    if line[27] == "1":
      aligned = 1
      alignmentStr +="    fair:mapsTo fair:A2 ;\n";
     #
    if line[28] == "1":
      # I Aligned, no requirement mapping
      aligned = 1
    if line[29] == "1":
      aligned = 1
      alignmentStr +="    fair:mapsTo fair:I1 ;\n";
    if line[30] == "1":
      aligned = 1
      alignmentStr +="    fair:mapsTo fair:I2 ;\n";
    if line[31] == "1":
      aligned = 1
      alignmentStr +="    fair:mapsTo fair:I3 ;\n";
    #
    if line[32] == "1":
      # R Aligned, no requirement mapping
      aligned = 1
    if line[33] == "1":
      aligned = 1
      alignmentStr +="    fair:mapsTo fair:R1 ;\n";
    if line[34] == "1":
      aligned = 1
      alignmentStr +="    fair:mapsTo fair:R1_1 ;\n";
    if line[35] == "1":
      aligned = 1
      alignmentStr +="    fair:mapsTo fair:R1_2 ;\n";
    if line[36] == "1":
      aligned = 1
      alignmentStr +="    fair:mapsTo fair:R1_3 ;\n";
    # xxx what about 'there is a comment'?

    import sys
    sys.stdout.write(alignmentStr);
    if aligned == 1:
      print("    fair:hasNoDirectMapping 0 ;");
    else:
      print("    fair:hasNoDirectMapping 1 ;");

    print("    fair:measurementMethod \""+line[15]+"\" ;");
    print("    fair:researchResourceType \""+line[16]+"\" ;");
    print("    schema:identifier \""+line[13]+"\" ;");
    print("    schema:name \""+line[12]+"\" ;");
    print("    schema:url <"+line[14]+"> ;");
