import java.util.Scanner;

public class main 
{
	public static void main(String[] args) 
	{
		//scanner for input
		Scanner playerInput = new Scanner(System.in);
		//make a new gameboard
		gameBoard ticTacToe = new gameBoard();
		//bools
		boolean game, victory, tie, player1Turn, validMove;
		//player input coordinates
		int input1, input2;
		
		game = true;
		while(game) 
		{
			//header message
			System.out.println("Tyler Coleman");
			System.out.println("CMPS 4143 Contemporary Programming Languages: Fall 2017");
			System.out.println("This is a simple game of TicTacToe between 2 players.");
			System.out.println("The first player to get 3 X's or O's in a row/column/diagonal wins!\n");
			
			//welcome message
			System.out.println("Welcome to TicTacToe!");
			System.out.println("Player 1 is X's and player 2 is O's.");
			System.out.println("To make a move just enter 2 integers between 1 and 3 (inclusive) seperated by a space.\n");
			
			//start a match
			victory = false;
			tie = false;
			player1Turn = true;
			while(!victory && !tie) 
			{
				//player1's turn
				ticTacToe.printBoard();
				if(player1Turn) 
				{
					System.out.println("It is player 1's turn! Please make your move.");
					validMove = false;
					//player 1 goes until they enter a valid move
					while(!validMove)
					{
						input1 = playerInput.nextInt();
						input2 = playerInput.nextInt();
						if(ticTacToe.makeMove(input1, input2, 'X')) 
						{
							System.out.println("Valid Move!");
							validMove = true;
							if(ticTacToe.winCondition()) { victory = true; }
							else if(ticTacToe.tieCondition()) { tie = true; }
						}
						else 
						{
							System.out.println("Invalid Move! Try again!");
							ticTacToe.printBoard();
						}
					}
					player1Turn = false;
				}
				//player 2's turn
				else 
				{
					System.out.println("It is player 2's turn! Please make your move.");
					validMove = false;
					//player 2 goes until they enter a valid move
					while(!validMove)
					{
						input1 = playerInput.nextInt();
						input2 = playerInput.nextInt();
						if(ticTacToe.makeMove(input1, input2, 'O')) 
						{
							System.out.println("Valid Move!");
							validMove = true;
							if(ticTacToe.winCondition()) { victory = true; }
							else if(ticTacToe.tieCondition()) { tie = true; }
						}
						else 
						{
							System.out.println("Invalid Move! Try again!");
							ticTacToe.printBoard();
						}
					}
					//change turns
					player1Turn = true;
				}
			}
			ticTacToe.printBoard();
			//tie game
			if(tie)
			{
				System.out.println("Tie game!");
			}
			//there is a winner
			else
			{
				//player1 made the final move
				if(!player1Turn)
				{
					System.out.println("Player 1 wins!");
				}
				//player2 made the final move
				else
				{
					System.out.println("Player 2 wins!");
				}
			}
			game = false;

		}
	}


}

