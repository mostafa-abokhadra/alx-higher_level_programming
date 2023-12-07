#include <stdio.h>
#include "lists.h"
size_t print_dlistint(const dlistint_t *h)
{
		size_t size = 0;
		const dlistint_t *t = h;

		if (!h)
			return (0);
		for (; t != NULL ; t = t->next, size++)
			printf("%d\n", t->n);
		return (size);
}
