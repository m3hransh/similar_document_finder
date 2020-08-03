#include <bits/stdc++.h>
#include <stdio.h>

using namespace std;

int Matrix[8][8];

bool isThisPlacePossible(int n,int row,int col)
{


  for(int i=row-1;i>=0;i--)
    {
        if(Matrix[i][col] == 1)
        {
        return false;
        }
    }

  for(int i=row-1,j=col-1;i>=0 && j>=0 ; i--,j--)
    {
        if(Matrix[i][j] ==1)
        {
        return false;
        }
    }

    for(int i=row-1,j=col+1;i>=0 && j<n ; i--,j++)
  {
        if(Matrix[i][j] == 1)
        {
        return false;
        }
  }

  return true;
}
void NQueen(int n,int row)
{
  if(row==n)
  {
    
    for(int i=0;i<n;i++)
    {
      for(int j=0;j<n;j++)
      {
        cout << Matrix[i][j] << " ";
      }
      cout << endl;
    }
    cout<<endl;
    return;

  }


  for(int j=0;j<n;j++)
  {

    if(isThisPlacePossible(n,row,j))
    {
      Matrix[row][j] = 1;
      NQueen(n,row+1);

    }

     Matrix[row][j] = 0;
  }
  return;

}
void placeNQueens(int n)
{

    for (int i=0 ; i<8 ; i++){
      for (int j=0 ; j<8 ; j++) {
          Matrix[i][j] = 0;
      }
  }


  NQueen(n,0);
}

int main()
{
    placeNQueens(8);
    return 0;
}
