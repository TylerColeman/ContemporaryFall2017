
public class gameBoard {
	//private vars
	private char[][] board;
	private int boardSize = 5;
	private int trueSize = 3;
	
	//default constructor
	gameBoard(){
		//make a new 2D array 5x5
		board = new char[boardSize][boardSize];
		
		for(int i = 0; i < boardSize; i++) {
			for(int j = 0; j < boardSize; j++) {
				if(i % 2 == 0)
				{
					if(j % 2 == 0) {
						board[i][j] = '*';
					}
					else {
						board[i][j] = '|';
					}
				}
				else {
					board[i][j] = '-';
				}

			}
		}
	}
	/*
	 * @Method:
	 * @Parameters:
	 * @Returns:
	 * @Description:
	 * 
	 */
	boolean makeMove(int i, int j, char value) {
		if(i > trueSize || j > trueSize || i < 1 || j < 1) {
			return false;
			}
		else {
			if(i == 1) {i = 0;}
			else if(i == 3) {i = 4;}
			if(j == 1) {j = 0;}
			else if(j == 3) {j = 4;}
			if(board[i][j] == '*') {
				board[i][j] = value;
				return true;
			}
			else {
				return false;
			}
			
			
		}
		
	}
	/*
	 * @Method:
	 * @Parameters:
	 * @Returns:
	 * @Description:
	 * 
	 */
	boolean check() {
		int xCount;
		int yCount;
		return true;
	}
	/*
	 * @Method:
	 * @Parameters:
	 * @Returns:
	 * @Description:
	 * 
	 */
	void printBoard() {
		for(int i = 0; i < boardSize; i++) {
			for(int j = 0; j < boardSize;j++) {
				System.out.print(board[i][j]);
				System.out.print(' ');
			}
			System.out.print('\n');
		}
	}
}
