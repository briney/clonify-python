clonify
=======
  
usage
-----
If MongoDB is local, `python clonify.py -d <database>` will iteratively run Clonify on all collections in the specified database.  
  
For remote databases, and to specify a single collection:  
`python clonify.py -i <MongoDB IP> -p <MongoDB port> -d <database> -c <collection>`  
  
To run Clonify without updating the target MongoDB with lineage information and instead writing basic lineage information to an output file:  
`python clonify.py -i <MongoDB IP> -p <MongoDB port> -d <database> -c <collection> -o <output_file> -n`  

By default, Clonify will group sequences by variable gene family and separately assign lineages within each group. To group by variable gene instead of variable gene family:  
`python clonify.py -d <database> -s gene`

To run Clonify on the entire dataset without grouping by gene or family (NOTE: this can be slow and very memory intensive):  
`python clonify.py -d <database> -s none`

  
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


