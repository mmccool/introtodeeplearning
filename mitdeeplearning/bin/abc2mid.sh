#!/bin/bash

abcfile=$1
suffix=${abcfile%.abc}
# stupid abc2midi program does not return normal error exit codes or use stderr for errors, argh argh argh
$HOME/.local/bin/abc2midi $abcfile -o "$suffix.mid" > "$suffix.err.txt"
# ... so scan output for any errors
grep Error "$suffix.err.txt"
code=$?
# rm "$suffix.abc"
# note that grep returns 0 if there is a match, it succeeds if there is an error, so we have to negate it
if [ "$code" -eq "0" ]
then
        exit 1
else
        exit 0
fi
