#!/bin/bash

abcfile=$1
suffix=${abcfile%.abc}
$HOME/.local/bin/abc2midi $abcfile -o "$suffix.mid" 2> "$suffix.err.txt"
# note that grep returns 0 if there is a match, so we have to negate it
grep Error "$suffix.err.txt"
code=$?
# rm "$suffix.abc"
exit [ "$code" -eq 0 ]
