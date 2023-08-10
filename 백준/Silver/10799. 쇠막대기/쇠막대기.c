#include <stdio.h>
#include <string.h>

int top=-1;

char stack[100001];
char PS[100001];
void push(char temp)
{
	top++;
	stack[top] = temp;
}

void pop()
{
	top--;
}

int main(void)
{
	int i,len;
	scanf("%s",PS);
	len = strlen(PS);
	int n=0;
	int cut=0;
	
	for(i=0;i<len;i++)
	{
		if(PS[i]=='(' && PS[i+1]==')')
		{
			if(i!=0)
			{
				cut += n;
			}
			i++;
		}
		else if(PS[i]==')' && stack[top]=='(')
		{
			pop();
			n--;
			cut++;
		}
		else
		{
			push(PS[i]);
			n++;
		}
	}
	printf("%d",cut);
	
	return 0;
}