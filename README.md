# Collaborative-Coding
A simple number guessing game developed using Test-Driven Development
______________________

This project is a simple number guessing game written in Python where the player tries to guess a randomly generated number between 1 and 100. The main focus was to use Test-Driven Development (TDD) to build the program step by step and simulate a pair programming experience, even though I worked alone.

I started the process by writing the unit tests before writing any actual game logic. These tests checked the main behaviors I wanted the game to have: responding if the guess was too low, too high, correct, or out of bounds. Once the tests were in place, I wrote the GuessGame class and made changes until all the tests passed. This approach made it easier to keep track of what I was trying to achieve and helped catch mistakes early.

Since I worked alone, I simulated pair programming by switching between two roles. At times I focused on writing code like a driver, and at other times I stepped back to review it and think about the overall logic like a navigator. Doing this helped me notice small issues I might have missed and pushed me to write clearer, more organized code.

One of the small challenges I ran into was making sure the test file could properly run and import the main game file. At first, the test module wasn’t being detected, but I solved it by checking the file names, keeping them in the same folder, and naming the test file correctly. Once that was fixed, everything ran smoothly.

Overall, this project showed me the benefits of writing tests first and thinking about the structure of my code before jumping straight into it. Even without a real partner. 

UML:

         ┌────────────────────┐
         │   Start Game       │
         └───────┬────────────┘
                 │
                 ▼
      ┌────────────────────┐
      │ Generate random    │
      │ number (1–100)     │
      └───────┬────────────┘
                 │
                 ▼
      ┌────────────────────┐
      │ Player inputs      │
      │ a guess            │
      └───────┬────────────┘
                 │
     ┌──────────┼──────────┐
     ▼          ▼          ▼
     Too Low   Too High   Correct
     │          │          │
     └────┐ ┌───┘          │
          ▼ ▼              │
     ┌────────────────────┐
     │ Prompt new guess   │
     └────────────────────┘
