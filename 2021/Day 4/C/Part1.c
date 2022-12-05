#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void get_input(int values[100], int boards[100][25]);
void draw(int value, int boards[100][25]);
int win_check(int boards[100][25]);
int calculate_result(int winner, int boards[100][25], int multiplier);

int main()
{
    int values[100], boards[100][25];
    get_input(values, boards);
    draw(values[0], boards);
    int winner;

    for (int i = 0; i < 100; i++)
    {
	    draw(values[i], boards);
	    winner = win_check(boards);

	    if (winner != -1)
	    {
		printf("Winner: %d\nResult: %d\n", winner, calculate_result(winner, boards, i));
		break;
	    }
    }
    return 0;
}

void get_input(int values[100], int boards[100][25])
{
    FILE* input = fopen("../input.txt", "r");
    if (input == NULL)
	exit(1);

    char str[1000];
    fgets(str, 1000, input);

    char* token = strtok(str, ",");

    int a = 0;
    while (token != NULL)
    {
	values[a++] = atoi(token);
	token = strtok(NULL, ",");
    }

    for (int i = 0; i < 100; ++i)
    {
	fgets(str, 1000, input);
	for (int j = 0; j < 5; ++j)
	    for (int k = 0; k < 5; ++k)
		fscanf(input, "%d", &boards[i][k + 5*j]);
    }
    fclose(input);
}

void draw(int value, int boards[100][25])
{
    for (int i = 0; i < 100; ++i)
	for (int j = 0; j < 25; ++j)
		if (boards[i][j] == value)
		    boards[i][j] = -1;
}

int win_check(int boards[100][25])
{
	int horizontal = 0, vertical = 0;

	for (int i = 0; i < 100; ++i)
	{
		horizontal = vertical = 1;
		for (int j = 0; j < 5; ++j)
		{
			for (int k = 0; k < 5; ++k)
			{
				if (boards[i][j*5 + k] != -1)
					horizontal = 0;
				if (boards[i][j + k*5] != -1)
					vertical = 0;
			}
			if (horizontal || vertical)
				return i;
		}
	}

	return -1;
}

int calculate_result(int winner, int boards[100][25], int multiplier)
{
	int sum = 0;
	for (int i = 0; i < 25; i++)
		if (boards[winner][i] != -1)
			sum += boards[winner][i];
	sum *= multiplier;
	return sum;
}
