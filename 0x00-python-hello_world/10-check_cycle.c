#include "lists.h"
#include <stdio.h>
int check_cycle(listint_t *list)
{
		listint_t *temp1  __attribute__((unused)) = NULL, *temp2  __attribute__((unused))= NULL;
		listint_t **arr= NULL;
		int size = 2, i = 0, circular = 0;

		if (!list || !list->next)
			return (0);
		if (list->next == list)
			return (1);
		arr = malloc(sizeof(listint_t *) * size);
		if (!arr)
			return (0);
		(*arr) = malloc(sizeof(listint_t *));
		temp1 = temp2 = (list);
		(*arr) = list;
		*(arr + 1) = NULL;

		while (temp2->next != list && temp2 != NULL)
		{
			for (i = 0; arr[i]; i++)
			{
				if (temp2->next == arr[i])
				{
					circular = 1;
					break;
				}
			}
			if (circular)
				return (circular);
			size++;
			arr = realloc(arr, (size * sizeof(listint_t *)));
			*(arr + size - 2) = malloc(sizeof(listint_t));
			*(arr + size - 2) = temp2->next;
			*(arr + (size - 1)) = NULL;
			temp2 = temp2->next;
			if (temp2 == NULL)
				break;
			if (temp2->next == list)
				circular = 1;
		}
		return circular;

}
