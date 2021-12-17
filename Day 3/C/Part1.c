#include <stdio.h>
#include <math.h>

int main()
{
    int codes[12][2] = {0}, gamma = 0, epsilon = 0;
    char line[12];
    FILE* input = fopen("../input.txt", "r");
    if (input == NULL)
	return 1;

    while (fscanf(input, "%s", line))
    {
	if (feof(input))
	    break;

	for (int i=0; i<12; i++)
	    (line[i] - '0') ? codes[i][1]++ : codes[i][0]++;
    }
    
    fclose(input);

    for (int i=0; i<12; i++)
	gamma += ((codes[i][0] > codes[i][1]) ? 0 : 1) * (int)pow(2, 11-i);	

    for (int i=0; i<12; i++)
	epsilon += ((codes[i][0] > codes[i][1]) ? 1 : 0) * (int)pow(2, 11-i);
    printf("Gamma:\t\t%d\nEpsilon:\t%d\nPower Cons.:\t%d\n", gamma, epsilon, gamma * epsilon);

    return 0;
}
