#include "lists.h"
/**
 * insert_node - add node to sorted linked list.
 * @head: double pointer to list start
 * @number: data
 *
 * Return: Always 0.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = malloc(sizeof(listint_t)), *temp = NULL;

	temp = *head;
	if (!newnode)
		return (NULL);
	newnode->n = number;
	if (!temp || newnode->n < temp->n)
	{
		newnode->next = temp;
		*head = newnode;
	}
	while (temp != NULL)
	{
		if (newnode->n == 0 || newnode->n < temp->next->n)
		{
			newnode->next = temp->next;
			temp->next = newnode;
			return (temp);
		}
		temp = temp->next;
	}
	return (NULL);
}
