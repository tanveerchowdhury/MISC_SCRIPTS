#!/bin/bash

# 


# 

PARENT_DIR="/files/infosec"
DEST_DIR="/files/infosec/ASA"

echo $PARENT_DIR
cd $PARENT_DIR 

for file in `ls -1`;
   do
	if [[ "$file" == *"iAppli"* ]] || [[ "$file" == *"IAPPLI"* ]]; then 
		echo $file
	fi 
   done
