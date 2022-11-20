#!/bin/bash

BLACK="\033[1;0m"
GREEN="\033[1;32m"
RED=`tput setaf 1`

echo -e "\E[32mSTART TESTS\E[0m"

echo -e "START 5\nDISPLAY\nEND" | ./pbrain-gomoku-ai > tests/protocole/start/got_map_5

cmp tests/protocole/start/got_map_5 tests/protocole/start/expected_map_5 1>/dev/null 2>&1; status=$?

echo -e "Size of 5"

if test $status -eq 0
then
    echo -e "${GREEN}OK${BLACK}"
else
    echo -e "${RED}KO"
fi

echo -e "START 20\nDISPLAY\nEND" | ./pbrain-gomoku-ai > tests/protocole/start/got_map_20

cmp tests/protocole/start/got_map_20 tests/protocole/start/expected_map_20 1>/dev/null 2>&1; status=$?

echo -e "Size of 20"

if test $status -eq 0
then
    echo -e "${GREEN}OK${BLACK}"
else
    echo -e "${RED}KO"
fi