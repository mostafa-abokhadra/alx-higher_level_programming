#include "hash_tables.h"

void hash_table_print(const hash_table_t *ht)
{
		unsigned long int i;

		if (!ht || ht->size == 0)
			return;
		printf("{");
		for (i = 0; i < ht->size; i++)
		{
			printf("why");
			printf("/'%s/': ", ht->array[i]->key);
			printf("/'%s/'", ht->array[i]->value);
		}
		printf("}");
		
}
