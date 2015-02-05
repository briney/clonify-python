#!/usr/bin/python
# filename: unset_clonify.py


###########################################################################
#
# Copyright (c) 2014 Bryan Briney.  All rights reserved.
#
# @version: 1.0.0
# @author: Bryan Briney
# @license: MIT (http://opensource.org/licenses/MIT) 
#
###########################################################################


import argparse

from pymongo import MongoClient


parser = argparse.ArgumentParser("Removes Clonify lineage assignments from a MongoDB database.")
parser.add_argument('-i', '-ip', dest='mongo_ip', default='localhost', 
					help="The IP address of the MongoDB server. Default is 'localhost'.")
parser.add_argument('-p', '-port', dest='mongo_port', default=27017, type=int, 
					help="The MongoDB port. Default is 27017.")
parser.add_argument('-d' '-database', dest='database', required=True, 
					help="The database to query. Required.")
parser.add_argument('-c' '-collection', dest='collection', default=None, 
					help="The collection to query. If not provided, \
					all collections in the database will be processed iteratively.")
args = parser.parse_args()


def get_collections():
	if args.collection:
		return [args.collection,]
	conn = MongoClient(args.mongo_ip, args.mongo_port)
	db = conn[args.database]
	collections = db.collection_names(include_system_collections=False)
	return sorted(collections)
		

def update_db(collection):
	conn = MongoClient(args.mongo_ip, args.mongo_port)
	db = conn[args.database]
	coll = db[collection]
	coll.update({'clonify': {'$exists': True}}, {'$unset': {'clonify': 1}}, multi=True)

def main():
	collections = get_collections()
	print '\n\n{0} collection(s) will be processed.\n\n'.format(len(collections))
	for collection in collections:
		print 'processing {0}...'.format(collection)
		update_db(collection)


if __name__ == '__main__':
	main()


