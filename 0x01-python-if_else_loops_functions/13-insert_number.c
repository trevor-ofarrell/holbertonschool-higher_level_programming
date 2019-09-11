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
	listint_t *newnode = malloc(sizeof(listint_t)), *temp = *head;

	if (!newnode || !head)
		return (NULL);

	newnode->n = number;
	newnode->next = NULL;
	if (!*head)
		*head = newnode;
	else if (number < temp->n)
	{
		newnode->next = temp;
		*head = newnode;
	}
	while (temp->next->n)
	{
		if (number > temp->next->n)
			temp = temp->next;
		else
			break;
	}
	newnode->next = temp->next;
	temp->next = newnode;
	return (newnode);
}
