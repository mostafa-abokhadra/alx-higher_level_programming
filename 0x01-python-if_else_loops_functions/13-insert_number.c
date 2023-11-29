#include <stdlib.h>
#include "lists.h"

listint_t *add_empty(int number)
{
		listint_t *node = malloc(sizeof(listint_t));
		
		if (!node)
			return (NULL);
		node->n = number;
		node->next = NULL;
		return (node);
}
listint_t *add_front(listint_t **head, int number)
{
		listint_t *node = malloc(sizeof(listint_t));

		if (!node)
			return (NULL);
		node->n = number;
		node->next = *(head);
		*(head) = node;
		return *(head);
}

listint_t *insert_node(listint_t **head, int number)
{
		listint_t *temp = *(head);
		listint_t *node;

		if (!head)
			return ((head) = add_empty(number));
		else if (temp->n >= number)
			return (*(head) = add_front(head, number));
		while(temp->next->n <= number && temp->next != NULL)
			temp = temp->next;
		node = malloc(sizeof(listint_t));
		if(!node)
			return (NULL);
		node->n = number;
		node->next = temp->next;
		temp->next = node;
		return (node);
}
