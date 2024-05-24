#!/bin/bash

# Read the .gitignore file and extract all folder patterns
IGNORED_FOLDERS=$(/.gitignore | grep -Ev '^#' | grep -o '[^/]*\/$')

# Construct the find command to exclude the ignored folders
FIND_COMMAND="find . -type d "
for FOLDER in $IGNORED_FOLDERS; do
    FIND_COMMAND+="( -not -path */$FOLDER* ) "
done
FIND_COMMAND+="-exec bash -c 'echo \"Folder: \$0\"; ls -p \"\$0\" | grep -v /' {} \;"

# Execute the find command
eval $FIND_COMMAND

