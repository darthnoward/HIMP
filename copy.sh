#!/bin/bash
TYPE=$(file -b --mime-type "$1")
xclip -selection clipboard -t "$TYPE" < "$1"
