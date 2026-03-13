"""
Rock Paper Scissors (Tkinter GUI)

Requirements:
- Python 3.x with Tkinter available

What it does:
- Lets the player pick rock, paper, or scissors using GUI buttons.
- Randomly selects a computer move each round.
- Displays round outcome and updates score counters (player, computer, ties).
- Includes Reset and Quit controls.

Run:
- python rock_paper_scissors.py
"""
import random
import tkinter as tk

CHOICES = ['rock', 'paper', 'scissors']
EMOJI = {'rock': '\U0001faa8', 'paper': '\U0001f4c4', 'scissors': '\u2702\ufe0f'}
BEATS = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}


def get_computer_choice() -> str:
    return random.choice(CHOICES)


def determine_winner(player: str, computer: str) -> str:
    if player == computer:
        return 'tie'
    return 'player' if BEATS[player] == computer else 'computer'


class RockPaperScissorsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Rock Paper Scissors')
        self.resizable(False, False)
        self.configure(bg='#1e1e2e')
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self._build_ui()

    def _build_ui(self):
        tk.Label(self, text='Rock  Paper  Scissors',
                 font=('Segoe UI', 22, 'bold'),
                 fg='#cdd6f4', bg='#1e1e2e').pack(pady=(20, 4))

        tk.Label(self, text='Choose your weapon:',
                 font=('Segoe UI', 12),
                 fg='#a6adc8', bg='#1e1e2e').pack(pady=(0, 12))

        btn_frame = tk.Frame(self, bg='#1e1e2e')
        btn_frame.pack()

        btn_style = dict(font=('Segoe UI', 28), width=4, height=2,
                         relief='flat', cursor='hand2',
                         bg='#313244', fg='#cdd6f4',
                         activebackground='#45475a', activeforeground='#cdd6f4', bd=0)

        for choice in CHOICES:
            tk.Button(btn_frame, text=EMOJI[choice],
                      command=lambda c=choice: self._play(c),
                      **btn_style).pack(side='left', padx=10)

        tk.Frame(self, height=2, bg='#313244').pack(fill='x', padx=20, pady=16)

        self.vs_label = tk.Label(self, text='', font=('Segoe UI', 36),
                                 fg='#cdd6f4', bg='#1e1e2e')
        self.vs_label.pack()

        self.result_label = tk.Label(self, text='Pick a move to start!',
                                     font=('Segoe UI', 16, 'bold'),
                                     fg='#89b4fa', bg='#1e1e2e')
        self.result_label.pack(pady=(4, 0))

        self.detail_label = tk.Label(self, text='', font=('Segoe UI', 11),
                                     fg='#a6adc8', bg='#1e1e2e')
        self.detail_label.pack(pady=(2, 0))

        tk.Frame(self, height=2, bg='#313244').pack(fill='x', padx=20, pady=16)

        score_frame = tk.Frame(self, bg='#1e1e2e')
        score_frame.pack()
        self._score_block(score_frame, 'You',  0, '#a6e3a1')
        self._score_block(score_frame, 'Ties', 1, '#f9e2af')
        self._score_block(score_frame, 'CPU',  2, '#f38ba8')

        bottom = tk.Frame(self, bg='#1e1e2e')
        bottom.pack(pady=(16, 20))

        tk.Button(bottom, text='Reset Scores', font=('Segoe UI', 10),
                  relief='flat', cursor='hand2',
                  bg='#313244', fg='#cdd6f4',
                  activebackground='#45475a', activeforeground='#cdd6f4',
                  command=self._reset).pack(side='left', padx=8, ipady=4, ipadx=8)

        tk.Button(bottom, text='Quit', font=('Segoe UI', 10),
                  relief='flat', cursor='hand2',
                  bg='#f38ba8', fg='#1e1e2e',
                  activebackground='#eba0ac', activeforeground='#1e1e2e',
                  command=self.destroy).pack(side='left', padx=8, ipady=4, ipadx=8)

    def _score_block(self, parent, label, col, color):
        frame = tk.Frame(parent, bg='#313244', padx=20, pady=10)
        frame.grid(row=0, column=col, padx=8)
        tk.Label(frame, text=label, font=('Segoe UI', 11, 'bold'),
                 fg=color, bg='#313244').pack()
        var = tk.StringVar(value='0')
        tk.Label(frame, textvariable=var, font=('Segoe UI', 28, 'bold'),
                 fg='#cdd6f4', bg='#313244').pack()
        if label == 'You':
            self._player_var = var
        elif label == 'Ties':
            self._ties_var = var
        else:
            self._cpu_var = var

    def _play(self, player_choice: str):
        computer_choice = get_computer_choice()
        outcome = determine_winner(player_choice, computer_choice)
        self.vs_label.config(
            text=f'{EMOJI[player_choice]}  vs  {EMOJI[computer_choice]}'
        )
        self.detail_label.config(
            text=f'You chose {player_choice}   Computer chose {computer_choice}'
        )
        if outcome == 'player':
            self.player_score += 1
            self.result_label.config(text='\U0001f389  You win!', fg='#a6e3a1')
        elif outcome == 'computer':
            self.computer_score += 1
            self.result_label.config(text='\U0001f4bb  Computer wins!', fg='#f38ba8')
        else:
            self.ties += 1
            self.result_label.config(text='\U0001f91d  It\'s a tie!', fg='#f9e2af')
        self._player_var.set(str(self.player_score))
        self._cpu_var.set(str(self.computer_score))
        self._ties_var.set(str(self.ties))

    def _reset(self):
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self._player_var.set('0')
        self._cpu_var.set('0')
        self._ties_var.set('0')
        self.vs_label.config(text='')
        self.result_label.config(text='Pick a move to start!', fg='#89b4fa')
        self.detail_label.config(text='')


if __name__ == '__main__':
    app = RockPaperScissorsApp()
    app.mainloop()
