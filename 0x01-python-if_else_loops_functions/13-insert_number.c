#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
* insert_node - insert a node in sorted
* @head: pointer head of linked listed
* @number: number to insert
* Return: the new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current1, *current2;

	current1 = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (number < current1->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
        	current2 = current1->next;
		while (current1)
		{
			if (number > current1->n && number < current2->n)
			{
				current1->next = new;
				new->next = current2;
				break;
			}
			current1 = current1->next;
			current2 = current2->next;
		}
	}
	return (new);
}
