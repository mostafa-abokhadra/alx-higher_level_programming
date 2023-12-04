#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

int is_palindrome(listint_t **head)
{
		listint_t *h = *(head);
		int pal = 1, size = 0;
		int *rev = NULL;

		if (!head || !((*head)->next))
			return (1);
		while (h != NULL)
		{
			rev = realloc(rev, sizeof(int) * (++size));
			if (!rev)
				return (0);
			if (h->next == NULL)
			{
				rev[size - 1] = h->n;
				h->next = *(head);
				h = h->next;
				for (;h->next != *(head); h = h->next)
				{
					if (h->n == rev[--size])
						continue;
					pal = 0;
				}
				if (h->n != rev[--size])
					pal = 0;
				h->next = NULL;
				break;
			}
			rev[size - 1] = h->n;
			h = h->next;
		}
		free(rev);
		return pal;
}
