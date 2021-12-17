#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int filter(int codes[], int func, int bit);

int main()
{
    int codes[1000], codes_copy[1000], i = 0, j = 0, one = 0, zero = 0;
    char line[12], *p ;
    FILE* input = fopen("../input.txt", "r");
    if (input == NULL)
	return 1;

    while (fscanf(input, "%s", line))
    {
	if (feof(input))
	    break;
	
	codes[i] = codes_copy[i++] = strtol(line, &p, 2);
    }
    printf("%d %d\n", filter(codes, 0, 0), filter(codes_copy, 1, 0));
    return 0;
}

// Finds the most common digit recursively
int filter(int codes[], int func, int bit)
{
    int ones = 0, zeroes = 0, temp;
    
    if (bit > 11)
	return -1;

    for (int i=0; i<1000; ++i)
	if (codes[i] != -1)
	    (codes[i] & (int)pow(2, 11 - bit)) ? ones++ : zeroes++;

    if (func)  // Changes the functionality to search for the least common digit
    {
	temp = ones;
	ones = zeroes;
	zeroes = temp;
    }

    if ((zeroes == 1 && ones == 0) || (ones == 1 && zeroes == 0))
	for (int i=0; i<1000; i++)
	    if (codes[i] != -1)
		return codes[i];

    if (zeroes == 1 && ones == 1)
	for (int i=0; i<1000; i++)
	    if (codes[i] != -1 && (codes[i] & (int)pow(2, 11 - bit)))
		return codes[i];

    for (int i=0; i<1000; ++i)
	if (codes[i] != -1 && (ones >= zeroes) ? !(codes[i] & (int)pow(2, 11 - bit)) : (codes[i] & (int)pow(2, 11 - bit)))
	    codes[i] = -1;

    return filter(codes, func, bit + 1);
}	
