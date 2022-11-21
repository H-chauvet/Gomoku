#!/bin/bash

BLACK="\033[1;0m"
GREEN="\033[1;32m"
RED=`tput setaf 1`

echo -e "\E[32mBEGIN TESTS\E[0m"

echo -e "START 5\nBEGIN\nDISPLAY\nEND" | ./pbrain-gomoku-ai > tests/protocole/begin/got_begin

sed --in-place '2d' tests/protocole/begin/got_begin

cmp tests/protocole/begin/got_begin tests/protocole/begin/expected_begin 1>/dev/null 2>&1; status=$?

if test $status -eq 0
then
    echo -e "${GREEN}OK${BLACK}"
else
    echo -e "${RED}KO"
fi