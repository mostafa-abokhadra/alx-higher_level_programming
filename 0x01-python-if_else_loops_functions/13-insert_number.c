#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
listint_t *add(int number)
{
		listint_t *new_node = malloc(sizeof(listint_t));
		
		if(!new_node)
			return (NULL);
		new_node->n = number;
		new_node->next = NULL;
		return (new_node);
}
listint_t *check_first(listint_t **head, int number)
{
		listint_t *new_node = malloc(sizeof(listint_t));
		listint_t *temp = *(head);

		if (!new_node)
			return (NULL);
		new_node->n = number;
		if (number >= temp->n)
		{
			new_node->next = NULL;
			temp->next = new_node;
		}
		else
		{
			new_node->next = temp;
			temp = new_node;
		}
		return (temp);
}
listint_t *insert_node(listint_t **head, int number)
{
		listint_t *temp = *(head);
		listint_t *new_node = NULL;

		if (!head)
			return add(number);
		if (temp->next == NULL || temp->n <= number)
			return (check_first(head, number));
		while(temp->next->n <  number && temp->next != NULL)
			temp = temp->next;
		new_node = malloc(sizeof(listint_t));
		if (!new_node)
			return (NULL);
		new_node->n = number;
		new_node->next = temp->next;
		temp->next = new_node;
		return (new_node);
}
