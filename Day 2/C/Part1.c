#include <stdio.h>
#include <string.h>

int main()
{
    int depth = 0, position = 0, number;
    char word[7];
    FILE* input = fopen("../input.txt", "r");
    if (input == NULL)
	return 1;

    while (fscanf(input, "%s %d", word, &number))
    {
	if (feof(input))
	    break;

	switch (word[0])
	{
	    case 'f':
		position += number;
		break;
	    case 'd':
		depth += number;
		break;
	    case 'u':
		depth -= number;
		break;
	}
    }

    fclose(input);

    printf("%d\n", position * depth);
    return 0;
}
