#!/bin/bash

abcfile=$1
suffix=${abcfile%.abc}
$HOME/.local/bin/abc2midi $abcfile -o "$suffix.mid"
code = $?
echo "Return code of abc2midi is $code"
# rm "$suffix.abc"
exit $code
