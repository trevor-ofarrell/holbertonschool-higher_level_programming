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
	listint_t *newnode = malloc(sizeof(listint_t)), *temp = newnode;

	if (!newnode || !head)
		return (NULL);
	newnode->n = number;
	temp = *head;
	if (!temp)
	{
		*head = newnode;
	}
	while (temp->next != NULL && temp->next->n < newnode->n)
	{
		temp = temp->next;
	}
	newnode->next = temp->next;
	temp->next = newnode;
	return (newnode);
}
