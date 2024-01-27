# WordleSolver README

## Introduction
This repository contains a Python script designed to solve Wordle puzzles in hard or normal mode. Wordle is a popular word puzzle game where the player has to guess a hidden five-letter word within six attempts.
The default strategy used for both game modes is an entropy maximization algorithm that implements a list of all valid wordle guesses and a common-word list. More information in the 'Results.txt' file under 'Tests' directory

## Getting Started
Follow the steps below to run the WordleSolver Python script and start solving Wordle puzzles.

### Prerequisites
Make sure you have the following installed on your machine:

- Python 3.x

### Installation
1. Download the ZIP of this repo:


2. Unzip and open a terminal
3. Navigate to the project directory:

    ```bash
    cd WordleSolver-main
    ```

### Usage
1. Open your Wordle game in your desired browser
  
2. Run the WordleSolver main.py script:

   Here's an example of running the WordleSolver script in solve mode and hard wordle game mode:

   macOS:
    ```bash
    python3 main.py solve HARD
    ```
    WINDOWS:
    ```bash
    python main.py solve HARD
    ```

   Replace `HARD` or `NORMAL` with the desired game mode.

4. Retrieve the Wordle guess and guess with that word in your game browser
5. Input your 5-digit guess result in the console
   
   Here's an example of inputting a valid result:
   ```bash
   01120
    ```
   '0' stands for a grey colored result
   '1' stands for a yellow colored result
   '2' stands for a green colored result
7. Repeat steps 3-4 until you solve the wordle game in your browser

### Command Line Arguments
- `benchmark`: Run WordleSolver in benchmark mode.
- `solve`: Run WordleSolver in solve mode.
- `HARD`: Set the game mode to HARD.
- `NORMAL`: Set the game mode to NORMAL.

The default strategy for HARD mode uses the HMODEMaximizeEntropyCommon.py script
The default strategy for NORMAL mode uses the NMODEMaximizeEntropyCommon.py script


