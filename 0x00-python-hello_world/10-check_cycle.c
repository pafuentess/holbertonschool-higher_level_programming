#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it.
* @list: head pointer of the linked list
* Return: 0 no loop, 1 loop
*/

int check_cycle(listint_t *list)
{
	listint_t *tortoi, *hare;

	tortoi = list;
	hare = list;

	while (tortoi && hare && hare->next)
	{
		tortoi = tortoi->next;
		hare = hare->next->next;

		if (tortoi == hare)
			return (1);
	}
	return (0);
}
