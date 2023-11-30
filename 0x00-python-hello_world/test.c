#include <stdio.h>
#include <stdlib.h>

struct node
{
	int n;
	struct node *next; 
};
int main(void)
{
	struct node **arr = malloc (sizeof(struct node *) * 2);
	int i = 0;
	struct node *new_one = malloc(sizeof(struct node));
	new_one->n = 66;
	new_one->next = NULL;
	*(arr) = new_one;
	
	while (arr[i])
	{
		printf("%d\n", arr[i]->n);
		i++;
	}
	arr = realloc(arr, (3 * sizeof(*arr)));
	printf("after\n");
	return (0);
}
