# ai50-Tic-Tac-Toe

#### Implementation of an AI to play Tic-Tac-Toe optimally

This is a Tic-Tac-Toe game that I made for the CS50-AI course. It is a two player game, where the first player is X and the second player is O. The game is played on a 3x3 board. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner. If all 9 squares are filled and neither player has 3 marks in a row, the game is a draw.

<img src="https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/images/game.png" width="800" />

https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/

## Algorithm

### Adversarial Search
In artificial intelligence, deep learning, machine learning, and computer vision, adversarial search is basically a kind of search in which one can trace the movement of an enemy or opponent. The step which arises the problem for the user or the user or the agent doesn't want that specific step task to be carried out.

### Minimax
Minimax is a decision rule used in artificial intelligence, decision theory, game theory, statistics, and philosophy for minimizing the possible loss for a worst case (maximum loss) scenario. When dealing with gains, it is referred to as "maximin"—to maximize the minimum gain. Originally formulated for two-player zero-sum game theory, covering both the cases where players take alternate moves and those where they make simultaneous moves, it has also been extended to more complex games and to general decision-making in the presence of uncertainty.

<img src="https://static.javatpoint.com/tutorial/ai/images/ai-adversarial-search.png" width="800" />

> image source: https://static.javatpoint.com/tutorial/ai/images/ai-adversarial-search.png

## Specification
Complete the implementations of player, actions, result, winner, terminal, utility, and minimax.

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The <code class="language-plaintext highlighter-rouge">player</code> function should take a <code class="language-plaintext highlighter-rouge">board</code> state as input, and return which player’s turn it is (either <code class="language-plaintext highlighter-rouge">X</code> or <code class="language-plaintext highlighter-rouge">O</code>).
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>In the initial game state, <code class="language-plaintext highlighter-rouge">X</code> gets the first move. Subsequently, the player alternates with each additional move.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The <code class="language-plaintext highlighter-rouge">actions</code> function should return a <code class="language-plaintext highlighter-rouge">set</code> of all of the possible actions that can be taken on a given board.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Each action should be represented as a tuple <code class="language-plaintext highlighter-rouge">(i, j)</code> where <code class="language-plaintext highlighter-rouge">i</code> corresponds to the row of the move (<code class="language-plaintext highlighter-rouge">0</code>, <code class="language-plaintext highlighter-rouge">1</code>, or <code class="language-plaintext highlighter-rouge">2</code>) and <code class="language-plaintext highlighter-rouge">j</code> corresponds to which cell in the row corresponds to the move (also <code class="language-plaintext highlighter-rouge">0</code>, <code class="language-plaintext highlighter-rouge">1</code>, or <code class="language-plaintext highlighter-rouge">2</code>).</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Possible moves are any cells on the board that do not already have an <code class="language-plaintext highlighter-rouge">X</code> or an <code class="language-plaintext highlighter-rouge">O</code> in them.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Any return value is acceptable if a terminal board is provided as input.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The <code class="language-plaintext highlighter-rouge">result</code> function takes a <code class="language-plaintext highlighter-rouge">board</code> and an <code class="language-plaintext highlighter-rouge">action</code> as input, and should return a new board state, without modifying the original board.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If <code class="language-plaintext highlighter-rouge">action</code> is not a valid action for the board, your program should <a href="https://docs.python.org/3/tutorial/errors.html#raising-exceptions">raise an exception</a>.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The returned board state should be the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in <code class="language-plaintext highlighter-rouge">board</code> itself is not a correct implementation of the <code class="language-plaintext highlighter-rouge">result</code> function. You’ll likely want to make a <a href="https://docs.python.org/3/library/copy.html#copy.deepcopy">deep copy</a> of the board first before making any changes.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The <code class="language-plaintext highlighter-rouge">winner</code> function should accept a <code class="language-plaintext highlighter-rouge">board</code> as input, and return the winner of the board if there is one.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If the X player has won the game, your function should return <code class="language-plaintext highlighter-rouge">X</code>. If the O player has won the game, your function should return <code class="language-plaintext highlighter-rouge">O</code>.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>One can win the game with three of their moves in a row horizontally, vertically, or diagonally.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return <code class="language-plaintext highlighter-rouge">None</code>.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The <code class="language-plaintext highlighter-rouge">terminal</code> function should accept a <code class="language-plaintext highlighter-rouge">board</code> as input, and return a boolean value indicating whether the game is over.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return <code class="language-plaintext highlighter-rouge">True</code>.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Otherwise, the function should return <code class="language-plaintext highlighter-rouge">False</code> if the game is still in progress.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The <code class="language-plaintext highlighter-rouge">utility</code> function should accept a terminal <code class="language-plaintext highlighter-rouge">board</code> as input and output the utility of the board.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If X has won the game, the utility is <code class="language-plaintext highlighter-rouge">1</code>. If O has won the game, the utility is <code class="language-plaintext highlighter-rouge">-1</code>. If the game has ended in a tie, the utility is <code class="language-plaintext highlighter-rouge">0</code>.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>You may assume <code class="language-plaintext highlighter-rouge">utility</code> will only be called on a <code class="language-plaintext highlighter-rouge">board</code> if <code class="language-plaintext highlighter-rouge">terminal(board)</code> is <code class="language-plaintext highlighter-rouge">True</code>.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The <code class="language-plaintext highlighter-rouge">minimax</code> function should take a <code class="language-plaintext highlighter-rouge">board</code> as input, and return the optimal move for the player to move on that board.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The move returned should be the optimal action <code class="language-plaintext highlighter-rouge">(i, j)</code> that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If the <code class="language-plaintext highlighter-rouge">board</code> is a terminal board, the <code class="language-plaintext highlighter-rouge">minimax</code> function should return <code class="language-plaintext highlighter-rouge">None</code>.</li>
    </ul>
  </li>
</ul>

Once all functions are implemented correctly, you should be able to run python runner.py and play against your AI. And, since Tic-Tac-Toe is a tie given optimal play by both sides, you should never be able to beat the AI (though if you don’t play optimally as well, it may beat you!)