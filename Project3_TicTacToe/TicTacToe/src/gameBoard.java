/*
 * */
public class gameBoard 
{
	//private vars
	private char[][] board;
	private int boardSize = 3;
	private int moves;
	
	//default constructor
	gameBoard()
	{
		moves = 0;
		//make a new 2D array 5x5
		board = new char[boardSize][boardSize];
		//create the board
		for(int i = 0; i < boardSize; i++) 
		{
			for(int j = 0; j < boardSize; j++) { board[i][j] = '*'; }
		}
	}
	/*
	 * @Method: makeMove
	 * @Parameters: integers i,j and char value
	 * @Returns: Boolean
	 * @Description: This function takes a row and column and places the passed in
	 * 				 character(value) to that position (if Possible) and returns true if
	 * 				 it could make the move and false if not.
	 * 
	 */
	public boolean makeMove(int i, int j, char value) 
	{
		//make sure the input keeps us inbounds
		if(i > boardSize || j > boardSize || i < 1 || j < 1) { return false; }
		else 
		{
			//set row and column to the proper offset
			i = i - 1;
			j = j - 1;
			//if the chosen spot is not already taken then set it
			if(board[i][j] == '*') 
			{
				board[i][j] = value;
				moves++;
				return true;
			}
			//it was already taken
			else { return false; }
		}
	}
	/*
	 * @Method: winCondition
	 * @Parameters: None
	 * @Returns: Boolean
	 * @Description: This method checks the rows/columns/diagonals 
	 * 				 for 3 matching symbols to see if the game has 
	 * 				 winner. it returns true if so and false if not.
	 * 
	 */
	public boolean winCondition() 
	{
		if(moves < 3) { return false; }
		else
		{
			//row check
			for(int i = 0; i < boardSize; i++)
			{
				if(board[i][0] != '*')
				{
					if(board[i][0] == board[i][1] && board[i][1] == board[i][2]) { return true; }
				}
			}
			//column check
			for(int i = 0; i < boardSize; i++)
			{
				if(board[0][i] != '*')
				{
					if(board[0][i] == board[1][i] && board[1][i] == board[2][i]) { return true; }
				}
			}
			
			//first diagonal check
			int i = 0;
			if(board[i][i] != '*')
			{
				if(board[i][i] == board[i+1][i+1] && board[i+1][i+1] == board[i+2][i+2]) { return true; }
			}
			//second diagonal check
			if(board[i+2][i] != '*')
			{
				if(board[i+2][i] == board[i+1][i+1] && board[i+1][i+1] == board[i][i+2]) { return true; }
			}

			//no win
			return false;
		}
	}
	/*
	 * @Method: tieCondition
	 * @Parameters: None
	 * @Returns: Boolean
	 * @Description: Checks the board for a tie game.
	 * 
	 */
	public boolean tieCondition() 
	{
		if(moves == 9 && !winCondition()) { return true; }
		else { return false; }
	}
	/*
	 * @Method: boardReset
	 * @Parameters:None
	 * @Returns: None
	 * @Description: Resets all the positions of the board back to '*'s
	 * 
	 */
	public void boardReset() 
	{
		moves = 0;
		for(int i = 0; i < boardSize; i++) 
		{
			for(int j = 0; j < boardSize; j++) { board[i][j] = '*'; }
		}
	}
	/*
	 * @Method: printBoard
	 * @Parameters: None
	 * @Returns: None
	 * @Description: Prints the gameboard that the users will see in a formatted manner.
	 * 
	 */
	public void printBoard() 
	{
		for(int i = 0; i < boardSize; i++) 
		{
			for(int j = 0; j < boardSize;j++) 
			{
				System.out.print(board[i][j]);
				System.out.print(' ');
				//column separators
				if(j < 2) { System.out.print('|'); }
				System.out.print(' ');
			}
			System.out.print('\n');
			if(i < 2) 
			{ 
				//row separators
				for(int k = 0; k < 5; k++) 
				{ 
					System.out.print('-'); 
					System.out.print(' ');
				}
				System.out.print('\n');
			}
		}
	}
}
