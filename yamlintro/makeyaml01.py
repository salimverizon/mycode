#!/usr/bin/env python3

#yaml is NOT part of the standard library
#python3 -m pip install import yaml

def main():
  ## create a blob of data to work with
  hitchhikers = [{"name": "Zaphod Beeblebrox" , "species":"Betelgueusi"}, {"name" : "Arthur Dent", "species" : "Human"}]

  ## displayour phthon data (a list contraining two dictionaries)
  print(hitchhikers)

  ##open a new file in write mode
  zfile = open ("galaxyguide.ymal" , "w")

  #use the YAML librery 
  ##Usage: yaml.dump(input data, file like object)
  # unlike json, the yaml lib uses .dump() to create YAML strings and write to files
  ## The json lib uses .dump() to create a string and .dump() to write to files yaml.dump(hichhikers, zfile)
  ##close the file
  zfile.close()
main()
