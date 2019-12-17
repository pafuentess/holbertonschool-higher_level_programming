#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* listint_len - count members of list
* @h: list to print
* Return: number of lenght list
*/

size_t listint_len(const listint_t *h)
{
	unsigned int i;

	i = 0;

	while (h)
	{
		h = h->next;
		i++;
	}
	return (i);
}

/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: head of linked list
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	int longi, i, j, str[1024];

	longi = listint_len(*head);

	for (i = 0; i <= longi - 1; i++)
	{
		str[i] = (*head)->n;
		(*head) = (*head)->next;
	}
	i--;
	for (j = 0 ; j < longi; j++)
	{
		if (str[j] != str[i])
			return (0);
		i--;
	}
	return (1);
}
