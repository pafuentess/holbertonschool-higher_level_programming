#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: head of linked list
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *tmp1;
	int str[1000], i, j;

	tmp1 = *head;
	i = 0;
	while (tmp1)
	{
		str[i] = tmp1->n;
		tmp1 = tmp1->next;
		i++;
	}
	if (i == 0)
		return (1);

	j = 0;
	while (i >= 0)
	{
		if (str[j] == str[i - 1])
		{
			i--;
			j++;
		}
		else
			return (0);
	}
	return (1);
}
