#!/bin/bash

SCRIPT_PATH="$0"
WORKDIR=$(dirname "$(readlink -f $SCRIPT_PATH)")


python $WORKDIR/terraria_workshop_loader.py $@