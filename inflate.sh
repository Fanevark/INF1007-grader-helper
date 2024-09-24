#!/bin/bash

usage() { 
  echo "Help unpack and inflate all submissions zip"
}

help() { 

  echo "Unzips moodle archive, filter only specific group and unzip all subzips
  usage: prepare_correction {options}
  [-a|--archive] <moodle archive name> 
  [-d|--directory] <correction directory> 
  [-p|--prefix] <laboratory prefix>"
}

SHORT_OPTS="ha:d:p:"
LONG_OPTS="archive:,directory:,prefix:"

ARGS=$(getopt -o ${SHORT_OPTS} -l ${LONG_OPTS} --  "$@")

eval set -- "${ARGS}" 

while :; do 
  case $1 in 
    -a|--archive) ARCHIVE=$2; shift 2
      ;;
    -d|--directory) DIRECTORY=$2;shift 2 
      ;;
    -p|--prefix) PREFIX=$2;shift 2
      ;;
    -h) help;exit 1
      ;;
    --) shift; break
      ;;
    *) echo "Unkown option $1"; help; exit 1
      ;;
  esac
done

# Abort if destionation exists
if [ -d $DIRECTORY ]; then 
  echo "Directory $DIRECTORY already exists"
  exit 1
fi

# Unzip archive to selected discovery
unzip "./$ARCHIVE" -d $DIRECTORY

# Removes everything that does not start with prefix
rm -rf $(find ./$DIRECTORY/* -not -name "$PREFIX*")

# Unzip subfolder zips
for team_directory in ./$DIRECTORY/*; do 
  unzip $team_directory/*.zip -d $team_directory/
done
