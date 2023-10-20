#!/bin/bash

abcfile=$1
suffix=${abcfile%.abc}
$HOME/.local/bin/abc2midi $abcfile -o "$suffix.mid"
rm "$suffix.abc"
