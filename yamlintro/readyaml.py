#!/usr/bin/env python3
import yaml
def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox" , "species":"Betelgueusi"}, {"name" : "Arthur Dent", "species" : "Human"}]
    print(hitchhikers)

    yamlstring = yaml.dump(hitchhikers)

    print(hitchhikers)

main()
