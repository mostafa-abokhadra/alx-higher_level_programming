#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
listint_t *insert_node(listint_t **head, int number)
{
		listint_t *temp = *(head);
		listint_t *new_node = NULL;

		if (!head)
			return (NULL);
		while(temp->next->n <  number && temp != NULL)
			temp = temp->next;
		new_node = malloc(sizeof(listint_t));
		if (!new_node)
			return (NULL);
		new_node->n = number;
		new_node->next = temp->next;
		temp->next = new_node;
		return (new_node);
}
