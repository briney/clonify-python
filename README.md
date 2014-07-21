clonify
=======
  
usage
-----
If MongoDB is local, `python clonify.py -d <database>` will iteratively run Clonify on all collections in the specified database.  
  
For remote databases, and to specify a single collection:  
`python clonify.py -i <MongoDB IP> -p <MongoDB port> -d <database> -c <collection>`  
  
Finally, to run Clonify without updating the target MongoDB with clone information and instead writing basic lineage information to an output file:  
`python clonify.py -i <MongoDB IP> -p <MongoDB port> -d <database> -c <collection> -o <output_file> -n`  

  
requirements
------------
python >=2.7  
numpy  
scipy  
biopython  
pymongo  
python-levenshtein  
fastcluster    
  
all package requirements can be installed with pip:  
`pip install <package>`


