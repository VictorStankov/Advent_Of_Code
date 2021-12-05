#include <stdio.h>

int main()
{
    int numbers[3] = {0, 0, 0}, previous = 0, sum = 0, counter = 0;

    while (scanf("%d", &numbers[0]))
    {
        if (numbers[0] && numbers[1] && numbers[2])
            sum = numbers[0] + numbers[1] + numbers[2];
            
        if (previous && sum > previous)
            counter++;
        
        previous = sum;
        numbers[2] = numbers[1];
        numbers[1] = numbers[0];
    }

    printf("%d\n", counter);
}