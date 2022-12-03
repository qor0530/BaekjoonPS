#include <stdio.h>

int main(void)
{
  int a, b, N, num = 1;
  scanf("%d", &N);

  for(int i = 0; i <N; i++)
    {
      scanf("%d %d", &a, &b);
      for(int j = 0; j < b; j++)
        {
          num *= a;
          num %= 10;
        }
      if(num == 0)
        printf("10\n");
      else
        printf("%d\n", num);
      num = 1;
    }
  return 0;
}