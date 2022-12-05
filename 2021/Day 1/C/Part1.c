#include <stdio.h>

int main()
{
    int num, previous = -1, counter = 0;
    FILE* input = fopen("../input.txt", "r");
    if (input == NULL)
	return 1;

    while (fscanf(input, "%d", &num))
    {
	if (feof(input))
	    break;
        if (num > previous && previous != -1)
            counter++;
        
        previous = num;
    }

    fclose(input);

    printf("%d\n", counter);
    return 0;
}
