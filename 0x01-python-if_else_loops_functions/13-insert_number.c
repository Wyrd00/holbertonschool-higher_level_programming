#include "lists.h"
/**
 * 
 * @head: linked list
 * @number: num to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *vagabond, *new;

        if (head == NULL)
                return (NULL);

        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->n = number;

        if (*head == NULL || (*head)->n > number)
        {
                new->next = *head;
                *head = new;
                return (new);
        }

        vagabond = *head;
        while (vagabond->next != NULL)
        {
                if ((vagabond->next)->n > number)
                {
                        new->next = vagabond->next;
                        vagabond->next = new;
                        return (new);
                }
                vagabond = vagabond->next;
        }
        vagabond->next = new;
        new->next = NULL;
        return (new);
}

