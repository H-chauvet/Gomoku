##
## EPITECH PROJECT, 2022
## Gomoku
## File description:
## Makefile
##

SRC		=	main.py

NAME	=	pbrain-gomoku-ai

PYTHON  =   python3


$(NAME):
			cp $(SRC) $(NAME)
			chmod +x $(NAME)

all: 		$(NAME)

tests_run:
			./tests/tests_launch.sh

clean:
			rm -f $(NAME)

fclean:		clean

re:			fclean all