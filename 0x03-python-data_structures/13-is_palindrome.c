#include "list.h"
#include <stdlib.h>
int is_palindrome(listint_t **head)
{
		listint_t *h = *(head), *last = NULL;
		int pal = 1;

		if (!head || !(*(head)->next))
			return (1);
		while (h->next != NULL)
			h = h->next;
		last = h;
		h = *(head);
		while(h != last || last > h)
		{
			if (h->data == last->data)
				continue;
			h = h->next;
			last = 
			pal = 0;
		}
		return (pal);
}
