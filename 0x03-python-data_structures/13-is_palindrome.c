#include "lists.h"
/**
 * is_palindrome - check if singly linked list is palindrome
 * @head: head of list
 * Return: 1 if yes, 0 if no
 */
int is_palindrome(listint_t **head)
{
	listint_t *top, *bottom, *nullnext;
	int i, len, b_len;

	len = 0;
	b_len = 0;

	if (!head || !*head)
		return (1);

	top = *head;
	bottom = *head;
	nullnext = *head;
	while (bottom->next != NULL)
	{
		bottom = bottom->next;
		len++;
		b_len++;
	}
	nullnext = bottom;
	bottom->next = *head;
	for (i = 0; i < len / 2; i++)
	{
		if (top->n == bottom->n)
		{
			top = top->next;
			while (b_len > 0)
			{
				bottom = bottom->next;
				b_len--;
			}
		}
		else
		{
			nullnext->next = NULL;
			return (0);
		}
		b_len = len;
	}
	nullnext->next = NULL;
	return (1);
}
