#include "hash_tables.h"

void free_table(hash_table_t *t)
{
		unsigned long int i;

		if (!t)
			return;
		if (t->array)
			for (i = 0; i < t->size; i++)
				free(t->array[i]);
		free(t);
}
hash_table_t *add_first_node(hash_table_t *ht, const char *key,
		const char *value, unsigned long int idx)
{
		ht->array[idx] = malloc(sizeof(hash_node_t));

		if (!ht->array[idx])
		{
			free_table(ht);
			return (NULL);
		}
		ht->array[idx]->key = strdup(key);
		ht->array[idx]->value = strdup(value);
		ht->array[idx]->next = NULL;
		return (ht);
}

hash_table_t *add_front_node(hash_table_t *ht, const char *key,
		const char *value, unsigned long int idx)
{
		hash_node_t *new_node = malloc(sizeof(new_node));

		if (!new_node)
			return (NULL);
		new_node->key = strdup(key);
		new_node->value = strdup(value);
		new_node->next = ht->array[idx];
		ht->array[idx] = new_node;
		return (ht);
}
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
		unsigned long int idx = key_index(
				(const unsigned char *)key, ht->size);

		if (ht->array[idx] == NULL)
		{
			ht = add_first_node(ht, key, value, idx);
			if (!ht)
				return (0);
		}
		else
		{	ht = add_front_node(ht, key, value, idx);
			if (!ht)
				return (0);
		}
		return (1);
}
