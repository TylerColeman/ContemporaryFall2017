import java.util.Scanner;

public class main {
	public static void main(String[] args) {
		//scanner for input
		Scanner playerInput = new Scanner(System.in);
		//make a new gameboard
		gameBoard ticTacToe = new gameBoard();
		//bools
		boolean game, victory, player1Turn, validMove;
		//player input coordinates
		int input1, input2;
		
		game = true;
		while(game) {
			//header message
			System.out.println("Tyler Coleman");
			System.out.println("Tyler Coleman");
			System.out.println("Tyler Coleman");
			System.out.println("Tyler Coleman");
			
			System.out.println("Welcome to TicTacToe!");
			System.out.println("Player 1 is X's and player 2 is O's.");
			System.out.println("To make a move just enter 2 integers between 1 and 3 (inclusive) seperated by a space.");
			//start a match
			victory = false;
			player1Turn = true;
			while(!victory) {
				//player1's turn
				ticTacToe.printBoard();
				if(player1Turn) {
					System.out.println("It is player 1's turn! Please make your move.");
					validMove = false;
					while(!validMove){
						input1 = playerInput.nextInt();
						input2 = playerInput.nextInt();
						if(ticTacToe.makeMove(input1, input2, 'X')) {
							System.out.println("Valid Move!");
							validMove = true;
						}
						else {
							System.out.println("Invalid Move! Try again!");
							ticTacToe.printBoard();
						}
					}
					player1Turn = false;
				}
				else {
					System.out.println("It is player 2's turn! Please make your move.");
					validMove = false;
					while(!validMove){
						
						input1 = playerInput.nextInt();
						input2 = playerInput.nextInt();
						if(ticTacToe.makeMove(input1, input2, 'O')) {
							System.out.println("Valid Move!");
							validMove = true;
						}
						else {
							System.out.println("Invalid Move! Try again!");
							ticTacToe.printBoard();
						}
					}
					player1Turn = true;
				}
			}
		}
	}


}

