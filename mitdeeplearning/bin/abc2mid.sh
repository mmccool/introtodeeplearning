#!/bin/bash

abcfile=$1
suffix=${abcfile%.abc}
$HOME/.local/bin/abc2midi $abcfile -o "$suffix.mid" 2> "$suffix.err.txt"
grep Error "$suffix.err.txt"
code=$?
# rm "$suffix.abc"
exit $code
