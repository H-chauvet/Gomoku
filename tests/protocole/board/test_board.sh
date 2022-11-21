#!/bin/bash

BLACK="\033[1;0m"
GREEN="\033[1;32m"
RED=`tput setaf 1`

echo -e "\E[32mBOARD TESTS\E[0m"

echo -e "START 5\nBOARD\n0,1,1\n3,0,2\nDONE\nEND" | ./pbrain-gomoku-ai > tests/protocole/board/got_board

sed --in-place '2d' tests/protocole/board/got_board

cmp tests/protocole/board/got_board tests/protocole/board/expected_board 1>/dev/null 2>&1; status=$?

echo -e "Size of 5"

if test $status -eq 0
then
    echo -e "${GREEN}OK${BLACK}"
else
    echo -e "${RED}KO"
fi