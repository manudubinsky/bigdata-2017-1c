#!/bin/bash
FILES="$@"
for f in $FILES
do
    echo importando $f
    rethinkdb import -f $f --table elecciones.tweets --format json --force --max-document-size 10000000000
done
