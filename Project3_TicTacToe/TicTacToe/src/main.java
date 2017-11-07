/*
 * Tyler Coleman
 * 
 * CMPS 4143 Contemporary Programming Languages: Fall 2017
 * 
 * Data Structure(s) Used: Array []
 * 
 * Description: This is a simple game of TicTacToe the users will enter
 * 				Coordinates on the 3x3 gameboard of where they would like
 * 				their symbol to be placed. The first player to get their
 * 				symbol in 3 consecutive places on the rows, columns, or 
 * 				diagonals will win!.
 * */
import java.util.Scanner;

public class main 
{
	public static void main(String[] args) 
	{
		//header message
		System.out.println("Tyler Coleman");
		System.out.println("CMPS 4143 Contemporary Programming Languages: Fall 2017");
		System.out.println("This is a simple game of TicTacToe between 2 players.");
		System.out.println("The first player to get 3 X's or O's in a row/column/diagonal wins!\n");
		//welcome and how to play!
		System.out.println("Welcome to TicTacToe!");
		System.out.println("Player 1 is X's and player 2 is O's.");
		System.out.println("To make a move just enter a row number and a column number seperated by a space.");
		System.out.println("The row and column numbers must be integers between 1 and 3 (inclusive).");
		System.out.println("Here is an example of where each command will place your symbol.");
		System.out.println("1 1 | 1 2 | 1 3");
		System.out.println("- - - - - - - - ");
		System.out.println("2 1 | 2 2 | 2 3");
		System.out.println("- - - - - - - - ");
		System.out.println("3 1 | 3 2 | 3 3\n\n");
		
		//scanner for input
		Scanner playerInput = new Scanner(System.in);
		//make a new gameboard
		gameBoard ticTacToe = new gameBoard();
		//bools to control the game
		boolean game, victory, tie, player1Turn, validMove, goodInput;
		//player input coordinates
		int input1, input2;
		
		//start game
		game = true;
		while(game) 
		{
			//start a match
			victory = false;
			tie = false;
			player1Turn = true;
			
			while(!victory && !tie) 
			{
				
				ticTacToe.printBoard();
				//player1's turn
				if(player1Turn) 
				{
					System.out.println("It is player 1's turn! Please make your move.");
					validMove = false;
					//player 1 goes until they enter a valid move
					while(!validMove)
					{
						//assume bad input >_<
						goodInput = false;
						//Initialize these 2 because java gets mad if you don't
						input1 = input2 = 0;
						//input checking!
						while(!goodInput)
						{
							try
							{
								input1 = playerInput.nextInt();
								input2 = playerInput.nextInt();
								goodInput = true;
							}
							catch(java.util.InputMismatchException err)
							{
								System.out.println("Invalid Move! Try again!");
								ticTacToe.printBoard();
								//move to the next line and let the user try again
								playerInput.nextLine();
							}
						}
						//now that we know we have 2 numbers from the user
						//attempt to make the move on the board
						if(ticTacToe.makeMove(input1, input2, 'X')) 
						{
							validMove = true;
							//check for a winner or a tie game
							if(ticTacToe.winCondition()) { victory = true; }
							else if(ticTacToe.tieCondition()) { tie = true; }
						}
						//they chose coordinates that were already taken
						else 
						{
							System.out.println("Invalid Move! Try again!");
							ticTacToe.printBoard();
						}
					}
					//swap turns
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
						//assume bad input >_<
						goodInput = false;
						//Initialize these 2 because java gets mad if you don't
						input1 = input2 = 0;
						//input checking!
						while(!goodInput)
						{
							try
							{
								input1 = playerInput.nextInt();
								input2 = playerInput.nextInt();
								goodInput = true;
							}
							catch(java.util.InputMismatchException err)
							{
								System.out.println("Invalid Move! Try again!");
								ticTacToe.printBoard();
								playerInput.nextLine();
							}
						}
						//now that we know we have 2 numbers from the user
						//attempt to make the move on the board
						if(ticTacToe.makeMove(input1, input2, 'O')) 
						{
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
			if(tie) { System.out.println("Tie game!"); }
			//there is a winner
			else
			{
				//player1 made the final move
				if(!player1Turn) { System.out.println("Player 1 wins!"); }
				//player2 made the final move
				else { System.out.println("Player 2 wins!"); }
			}
			
			//reset the game board
			ticTacToe.boardReset();
			
			//check if the users would like to play again
			String cont;
			System.out.println("Press [enter] to play again!\nType [q] if you would like to quit.");
			cont = playerInput.nextLine();
			System.out.println(cont);
			if (playerInput.hasNextLine())
				cont = playerInput.nextLine();
			//if they enter 'q' the game ends
			if(cont.equals("q") || cont.equals("Q")) { game = false;}
		}
		//exit message
		System.out.println("Thank you for playing TicTacToe!");
		playerInput.close();
	}

	
}

