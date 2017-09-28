#!/bin/bash

#=====================================================
# 
# File: AppSecASA.sh
#
# Usage: ./AppSecASA.sh
# 
# Description:
# To copy only the iAppli files from NAS parent folder
# to ASA subfolder to using from Excel Macro.
# 
# Need to keep the same filename as it changes everyday
#
# Author: tanveerchowdhury
#
# Created: Sept 27, 2017
#
# Revision: 1.0
# =====================================================

# NAS Shared Drive Location
PARENT_DIR="/files/infosec"
# App Sec File Location
DEST_DIR="/files/infosec/ASA"

# Change directory to parent folder
cd $PARENT_DIR 

# Loop through the files in NAS folder and search for iAppli files
for file in `ls -1`;
   do
	if [[ "$file" == *"iAppli"* ]] || [[ "$file" == *"IAPPLI"* ]]; then 

		NewFile=`echo $file | cut -d _ -f2-5` # Create new filename by removing the timestamp part
	 	/bin/mv -v $file $DEST_DIR/$NewFile   # Use new filename for move to ASA subfolder	
	fi 
   done
