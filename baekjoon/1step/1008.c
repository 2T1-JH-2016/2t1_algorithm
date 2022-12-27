#include <stdio.h>
int main()
{
	double A, B;
	scanf("%lf %lf", &A, &B);
	while (B <= 0)
		scanf("%lf", &B);
	printf("%0.9lf\n", A/B);
    
    return 0;
}