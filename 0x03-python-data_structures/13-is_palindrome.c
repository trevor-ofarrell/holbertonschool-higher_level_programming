#include "lists.h"
/**
 * ispalin - checks to see if ll is a palindrome.
 * @left: left-ward pointer
 * @right: pointer to the right
 *
 * Return: Always 0.
 */
_Bool ispalin(listint_t **left, listint_t *right)
{
	int check;

	if (right == NULL)
		return (1);
	check = ispalin(left, right->next);
	if (check == 0)
		return (0);
	if (right->n == (*left)->n)
	{
		(*left) = (*left)->next;
		return (1);
	}
	return (0);
}
/**
 * is_palindrome - recursively call the function ispalin
 * @head: head node
 *
 * Return: Always 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;

	return (ispalin(&temp, temp));
}
