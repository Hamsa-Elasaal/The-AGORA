import tkinter as tk
from tkinter import font as tkfont
from random import shuffle

# ===================== DATA =====================
python = [
    {"Question": "print('hello'[3])", "choices": ["A) h", "B) o", "C) l", "D) Error"], "answer": "C", "points": 1, "Link": "https://youtu.be/KAXvMbD1Zac?si=1507laJEZro0RiFD"},
    {"Question": "print('hello'[::-1])", "choices": ["A) hello", "B) olleh", "C) hlo", "D) olh"], "answer": "B", "points": 1, "Link": "https://youtu.be/6205vqFp7JI?si=Iz4LC7oMx4b997Vg"},
    {"Question": "print(11%3)", "choices": ["A) 3.6", "B) 0", "C) 1", "D) 2"], "answer": "D", "points": 1, "Link": "https://youtu.be/qv-Qdi212X4?si=NYXmCbPMZWhA7Pac"},
    {"Question": "print([1,2,3]*2)", "choices": ["A) [1, 2, 3]", "B) [2, 4, 6]", "C) [1, 2, 3, 1, 2, 3]", "D) Error"], "answer": "C", "points": 2, "Link": "https://www.youtube.com/results?search_query=python+list+multiplication"},
    {"Question": "print(sorted('italy'))", "choices": ["A) None", "B) 'ytlia'", "C) 'ailty'", "D) ['a', 'i', 'l', 't', 'y']"], "answer": "D", "points": 2, "Link": "https://youtu.be/t3Ot06TRspg?si=zuGPtau3oME6Drq3"},
    {"Question": "print([2,1,3].sort())", "choices": ["A) None", "B) [1, 2, 3]", "C) [3, 2, 1]", "D) Errro"], "answer": "A", "points": 2, "Link": "https://youtu.be/pJYnSEZ5p00?si=iWULt70mw3Z46j46"},
    {"Question": "print(type(int('1.9')))", "choices": ["A) 1.9", "B) 2", "C) 1", "D) Error"], "answer": "D", "points": 2, "Link": "https://youtu.be/wGu_L6O1X4A?si=Qju1z1tOOk5fhdnh"},
    {"Question": "print([i for i in range(5) if i % 2 == 1])", "choices": ["A) [1, 3]", "B) [0, 2, 4]", "C) [1, 3, 5]", "D) [2, 4]"], "answer": "A", "points": 3, "Link": "https://youtu.be/FP9ZuA6tX3g?si=y44V2XUwxh-OWUzq"},
    {"Question": "print(bool('False'))", "choices": ["A) True", "B) False", "C) 'False'", "D) Error"], "answer": "A", "points": 3, "Link": "https://youtube.com/shorts/y7KiKj3-hps?si=BNQozdGsvVvg-CAW"},
]

capital = [
    {"Question": "What is the capital of the UK?", "choices": ["A) Manchester", "B) Edinburgh", "C) London", "D) Birmingham"], "answer": "C", "points": 1, "Link": "https://www.youtube.com/results?search_query=London+city+guide+uk"},
    {"Question": "What is the capital of France?", "choices": ["A) Paris", "B) Marseille", "C) Lyon", "D) Nice"], "answer": "A", "points": 1, "Link": "https://www.youtube.com/results?search_query=Paris+city+guide+france"},
    {"Question": "What is the capital of Germany?", "choices": ["A) Hamburg", "B) Berlin", "C) Munich", "D) Frankfurt"], "answer": "B", "points": 1, "Link": "https://www.youtube.com/results?search_query=Berlin+city+guide+germany"},
    {"Question": "What is the capital of Spain?", "choices": ["A) Barcelona", "B) Madrid", "C) Seville", "D) Valencia"], "answer": "B", "points": 2, "Link": "https://www.youtube.com/results?search_query=Madrid+city+guide+spain"},
    {"Question": "What is the capital of Italy?", "choices": ["A) Rome", "B) Venice", "C) Milan", "D) Florence"], "answer": "A", "points": 2, "Link": "https://www.youtube.com/results?search_query=Rome+city+guide+italy"},
    {"Question": "What is the capital of Japan?", "choices": ["A) Osaka", "B) Kyoto", "C) Tokyo", "D) Yokohama"], "answer": "C", "points": 2, "Link": "https://www.youtube.com/results?search_query=Tokyo+city+guide+japan"},
    {"Question": "What is the capital of South Korea?", "choices": ["A) Daegu", "B) Incheon", "C) Busan", "D) Seoul"], "answer": "D", "points": 2, "Link": "https://www.youtube.com/results?search_query=Seoul+city+guide+south+korea"},
    {"Question": "What is the capital of Switzerland?", "choices": ["A) Zurich", "B) Geneva", "C) Basel", "D) Bern"], "answer": "D", "points": 3, "Link": "https://www.youtube.com/results?search_query=Bern+city+guide+switzerland"},
    {"Question": "What is the capital of Poland?", "choices": ["A) Warsaw", "B) Kraków", "C) Gdańsk", "D) Wrocław"], "answer": "A", "points": 3, "Link": "https://www.youtube.com/results?search_query=Warsaw+city+guide+poland"},
]

# ===================== COLORS =====================
BG       = "#0a0a14"
SURFACE  = "#12121f"
SURFACE2 = "#1a1a2e"
GOLD     = "#c9a84c"
GOLD2    = "#f0d080"
GOLD_DIM = "#6a5020"
TEXT     = "#e8e0d0"
TEXT_DIM = "#6a6055"
GREEN    = "#4caf74"
RED      = "#c94c4c"
BLUE     = "#4c7bc9"

# ===================== APP =====================
class AgoraQuiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("THE AGORA QU")
        self.geometry("750x560")
        self.minsize(650, 500)
        self.configure(bg=BG)
        self.resizable(True, True)

        # State
        self.player_name   = ""
        self.quiz_type     = ""
        self.questions     = []
        self.current_idx   = 0
        self.score         = 0
        self.max_score     = 0
        self.correct_count = 0
        self.answered      = False

        self._build_fonts()
        self._show_welcome()

    def _build_fonts(self):
        self.f_title    = tkfont.Font(family="Georgia", size=26, weight="bold")
        self.f_subtitle = tkfont.Font(family="Georgia", size=11)
        self.f_label    = tkfont.Font(family="Courier New", size=11)
        self.f_question = tkfont.Font(family="Courier New", size=13, weight="bold")
        self.f_choice   = tkfont.Font(family="Courier New", size=12)
        self.f_btn      = tkfont.Font(family="Georgia", size=12, weight="bold")
        self.f_small    = tkfont.Font(family="Courier New", size=9)
        self.f_big      = tkfont.Font(family="Georgia", size=34, weight="bold")
        self.f_medium   = tkfont.Font(family="Georgia", size=16, weight="bold")

    def _clear(self):
        for w in self.winfo_children():
            w.destroy()

    def _header(self, parent):
        tk.Label(parent, text="THE AGORA QU", font=self.f_title, bg=BG, fg=GOLD).pack(pady=(28, 2))
        tk.Label(parent, text="Logic  ·  Knowledge  ·  Programming", font=self.f_subtitle, bg=BG, fg=TEXT_DIM).pack()
        tk.Frame(parent, height=1, bg=GOLD_DIM).pack(fill="x", padx=100, pady=10)

    def _gold_btn(self, parent, text, cmd, width=20):
        return tk.Button(parent, text=text, command=cmd, font=self.f_btn, width=width,
                         bg=GOLD, fg=BG, activebackground=GOLD2, activeforeground=BG,
                         relief="flat", cursor="hand2", pady=8)

    def _outline_btn(self, parent, text, cmd, width=18):
        return tk.Button(parent, text=text, command=cmd, font=self.f_btn, width=width,
                         bg=SURFACE2, fg=GOLD, activebackground=SURFACE, activeforeground=GOLD2,
                         relief="flat", cursor="hand2", pady=6,
                         highlightthickness=1, highlightbackground=GOLD_DIM)

    # ══════════════════════════════
    # SCREEN 1 — WELCOME
    # ══════════════════════════════
    def _show_welcome(self):
        self._clear()
        self._header(self)

        card = tk.Frame(self, bg=SURFACE2, padx=40, pady=30,
                        highlightthickness=1, highlightbackground=GOLD_DIM)
        card.pack(pady=10, padx=120)

        tk.Label(card, text="Enter your name:", font=self.f_label, bg=SURFACE2, fg=TEXT_DIM).pack(pady=(0, 8))

        self.name_var = tk.StringVar()
        entry = tk.Entry(card, textvariable=self.name_var, font=self.f_question,
                         width=24, bg=BG, fg=TEXT, insertbackground=GOLD,
                         relief="flat", justify="center",
                         highlightthickness=1, highlightbackground=GOLD_DIM)
        entry.pack(ipady=8)
        entry.focus()
        entry.bind("<Return>", lambda e: self._enter_name())

        self.name_err = tk.Label(card, text="", font=self.f_small, bg=SURFACE2, fg=RED)
        self.name_err.pack(pady=(4, 0))

        self._gold_btn(card, "BEGIN YOUR QUEST  →", self._enter_name, width=26).pack(pady=(14, 0))

    def _enter_name(self):
        name = self.name_var.get().strip().title()
        if not name:
            self.name_err.config(text="⚠  Please enter your name!")
            return
        self.player_name = name
        self._show_select()

    # ══════════════════════════════
    # SCREEN 2 — SELECT QUIZ
    # ══════════════════════════════
    def _show_select(self):
        self._clear()
        self._header(self)

        tk.Label(self, text=f"Welcome, {self.player_name}!  Choose your quiz:",
                 font=self.f_label, bg=BG, fg=TEXT_DIM).pack(pady=(0, 16))

        cards_frame = tk.Frame(self, bg=BG)
        cards_frame.pack()

        self._quiz_card(cards_frame, "python",  "⌨️  Python",  "Code Challenges",  BLUE).pack(side="left", padx=16)
        self._quiz_card(cards_frame, "capital", "🌍  Capitals", "World Geography", GOLD).pack(side="left", padx=16)

        self.select_err = tk.Label(self, text="", font=self.f_small, bg=BG, fg=RED)
        self.select_err.pack(pady=(10, 0))

        self._gold_btn(self, "ENTER ARENA  →", self._launch_quiz).pack(pady=6)
        self._outline_btn(self, "← Back", self._show_welcome, width=12).pack()

    def _quiz_card(self, parent, value, title, desc, accent):
        f = tk.Frame(parent, bg=SURFACE2, width=220, height=180,
                     highlightthickness=2, highlightbackground=SURFACE2, cursor="hand2")
        f.pack_propagate(False)

        def select():
            self.quiz_type = value
            for w in parent.winfo_children():
                w.config(highlightbackground=SURFACE2)
            f.config(highlightbackground=accent)
            self.select_err.config(text="")

        f.bind("<Button-1>", lambda e: select())

        tk.Label(f, text=title, font=self.f_medium, bg=SURFACE2, fg=accent).pack(pady=(24, 4))
        tk.Label(f, text=desc,  font=self.f_small,  bg=SURFACE2, fg=TEXT_DIM).pack()
        tk.Frame(f, height=1, bg=GOLD_DIM).pack(fill="x", padx=24, pady=8)
        tk.Button(f, text="SELECT", font=self.f_small, bg=accent, fg=BG,
                  relief="flat", cursor="hand2", command=select).pack()
        return f

    def _launch_quiz(self):
        if not self.quiz_type:
            self.select_err.config(text="⚠  Please select a quiz first!")
            return
        data = python if self.quiz_type == "python" else capital
        self.questions     = data[:]
        shuffle(self.questions)
        self.current_idx   = 0
        self.score         = 0
        self.max_score     = 0
        self.correct_count = 0
        self._show_quiz()

    # ══════════════════════════════
    # SCREEN 3 — QUIZ
    # ══════════════════════════════
    def _show_quiz(self):
        self._clear()

        # Top bar
        top = tk.Frame(self, bg=BG)
        top.pack(fill="x", padx=28, pady=(16, 0))

        mode = "⌨️  PYTHON" if self.quiz_type == "python" else "🌍  CAPITALS"
        tk.Label(top, text=mode, font=self.f_label, bg=BG, fg=GOLD).pack(side="left")

        self.score_lbl = tk.Label(top, text="SCORE: 0", font=self.f_label, bg=BG, fg=TEXT_DIM)
        self.score_lbl.pack(side="right")

        # Progress bar
        prog_bg = tk.Frame(self, bg=SURFACE2, height=4)
        prog_bg.pack(fill="x", padx=28, pady=4)
        prog_bg.pack_propagate(False)
        self.prog_fill = tk.Frame(prog_bg, bg=GOLD, height=4)
        self.prog_fill.place(x=0, y=0, relheight=1, relwidth=0)

        self.q_counter = tk.Label(self, text="", font=self.f_small, bg=BG, fg=TEXT_DIM)
        self.q_counter.pack()

        # Card
        self.card = tk.Frame(self, bg=SURFACE2, padx=26, pady=20,
                             highlightthickness=1, highlightbackground=GOLD_DIM)
        self.card.pack(fill="both", padx=28, pady=6)

        self.pts_lbl = tk.Label(self.card, text="", font=self.f_small, bg=SURFACE2, fg=GOLD_DIM)
        self.pts_lbl.pack(anchor="w")

        self.q_lbl = tk.Label(self.card, text="", font=self.f_question,
                              bg=BG, fg=TEXT, wraplength=650,
                              justify="left", padx=12, pady=10,
                              highlightthickness=1, highlightbackground=GOLD_DIM)
        self.q_lbl.pack(fill="x", pady=(6, 14))

        # Choices grid
        self.choice_frame = tk.Frame(self.card, bg=SURFACE2)
        self.choice_frame.pack(fill="x")
        self.choice_btns = []

        for i in range(4):
            row, col = divmod(i, 2)
            btn = tk.Button(self.choice_frame, text="", font=self.f_choice,
                            bg=SURFACE, fg=TEXT, activebackground=GOLD_DIM,
                            relief="flat", cursor="hand2", anchor="w",
                            padx=12, pady=9, wraplength=280,
                            highlightthickness=1, highlightbackground="#2a2a3a")
            btn.grid(row=row, column=col, padx=5, pady=4, sticky="ew")
            self.choice_btns.append(btn)

        self.choice_frame.columnconfigure(0, weight=1)
        self.choice_frame.columnconfigure(1, weight=1)

        # Feedback
        self.feedback_lbl = tk.Label(self.card, text="", font=self.f_label,
                                     bg=SURFACE2, fg=TEXT, pady=4, wraplength=660)
        self.feedback_lbl.pack(fill="x", pady=(10, 0))

        # Link label
        self.link_lbl = tk.Label(self.card, text="", font=self.f_small,
                                 bg=SURFACE2, fg=BLUE, cursor="hand2", wraplength=660)
        self.link_lbl.pack()

        # Next button
        self.next_btn = self._gold_btn(self.card, "NEXT QUESTION  →", self._next_question, width=22)
        self.next_btn.pack(pady=(8, 0))
        self.next_btn.pack_forget()

        self._load_question()

    def _load_question(self):
        self.answered = False
        q     = self.questions[self.current_idx]
        total = len(self.questions)

        self.q_counter.config(text=f"Question  {self.current_idx + 1}  /  {total}")
        self.pts_lbl.config(text=f"⬡  {q['points']} POINT{'S' if q['points'] > 1 else ''}")
        self.q_lbl.config(text=f"  {q['Question']}")
        self.feedback_lbl.config(text="", bg=SURFACE2, fg=TEXT)
        self.link_lbl.config(text="")
        self.link_lbl.unbind("<Button-1>")
        self.next_btn.pack_forget()

        pct = self.current_idx / total
        self.prog_fill.place(relwidth=pct)

        for i, btn in enumerate(self.choice_btns):
            letter = q['choices'][i][0]
            text   = q['choices'][i]
            btn.config(text=f"  {text}", bg=SURFACE, fg=TEXT,
                       highlightbackground="#2a2a3a", state="normal",
                       command=lambda l=letter: self._handle_answer(l))

    def _handle_answer(self, letter):
        if self.answered:
            return
        self.answered = True

        q       = self.questions[self.current_idx]
        correct = letter == q['answer']

        for btn in self.choice_btns:
            btn.config(state="disabled")
            btn_letter = btn.cget("text").strip()[0]
            if btn_letter == q['answer']:
                btn.config(bg="#1a3320", fg=GREEN, highlightbackground=GREEN)
            elif btn_letter == letter and not correct:
                btn.config(bg="#331515", fg=RED, highlightbackground=RED)

        if correct:
            self.score         += q['points']
            self.correct_count += 1
            self.feedback_lbl.config(
                text=f"✅  Correct!  +{q['points']} point{'s' if q['points'] > 1 else ''}",
                fg=GREEN)
        else:
            self.feedback_lbl.config(
                text=f"❌  Wrong!  Correct answer: {q['answer']}",
                fg=RED)
            link = q['Link']
            self.link_lbl.config(text=f"▶  Watch explanation: {link}", fg=BLUE)
            self.link_lbl.bind("<Button-1>", lambda e: __import__('webbrowser').open(link))

        self.max_score += q['points']
        self.score_lbl.config(text=f"SCORE: {self.score}")

        label = "SEE RESULTS  →" if self.current_idx == len(self.questions) - 1 else "NEXT QUESTION  →"
        self.next_btn.config(text=label)
        self.next_btn.pack(pady=(8, 0))

    def _next_question(self):
        self.current_idx += 1
        if self.current_idx >= len(self.questions):
            self._show_results()
        else:
            self._load_question()

    # ══════════════════════════════
    # SCREEN 4 — RESULTS
    # ══════════════════════════════
    def _show_results(self):
        self._clear()

        pct    = round((self.score / self.max_score) * 100) if self.max_score else 0
        passed = pct >= 50
        wrong  = len(self.questions) - self.correct_count

        tk.Label(self, text="🏆" if passed else "💪",
                 font=tkfont.Font(size=44), bg=BG).pack(pady=(24, 4))

        tk.Label(self, text=f"Well Done,  {self.player_name}!",
                 font=self.f_medium, bg=BG, fg=GOLD).pack()
        tk.Label(self, text="QUEST COMPLETE",
                 font=self.f_small, bg=BG, fg=TEXT_DIM).pack(pady=(2, 10))

        card = tk.Frame(self, bg=SURFACE2, padx=50, pady=24,
                        highlightthickness=1, highlightbackground=GOLD_DIM)
        card.pack(padx=100, pady=4)

        tk.Label(card, text=f"{self.score}", font=self.f_big, bg=SURFACE2, fg=GOLD).pack()
        tk.Label(card, text=f"out of  {self.max_score}  points",
                 font=self.f_label, bg=SURFACE2, fg=TEXT_DIM).pack()

        badge_text = "✅  PASSED" if passed else "❌  FAILED"
        badge_col  = GREEN if passed else RED
        tk.Label(card, text=badge_text, font=self.f_subtitle,
                 bg=SURFACE2, fg=badge_col).pack(pady=10)

        stats = tk.Frame(card, bg=BG, pady=10, padx=10)
        stats.pack(fill="x", pady=(0, 10))

        for val, lbl, col in [(f"{pct}%", "Accuracy", GOLD),
                               (self.correct_count, "Correct", GREEN),
                               (wrong, "Wrong", RED)]:
            f = tk.Frame(stats, bg=BG)
            f.pack(side="left", expand=True)
            tk.Label(f, text=str(val), font=self.f_medium, bg=BG, fg=col).pack()
            tk.Label(f, text=lbl, font=self.f_small, bg=BG, fg=TEXT_DIM).pack()

        btns = tk.Frame(self, bg=BG)
        btns.pack(pady=10)
        self._gold_btn(btns,    "PLAY AGAIN",    self._play_again,   width=14).pack(side="left", padx=8)
        self._outline_btn(btns, "CHANGE ARENA",  self._show_select,  width=14).pack(side="left", padx=8)
        self._outline_btn(btns, "HOME",           self._show_welcome, width=8 ).pack(side="left", padx=8)

    def _play_again(self):
        data = python if self.quiz_type == "python" else capital
        self.questions     = data[:]
        shuffle(self.questions)
        self.current_idx   = 0
        self.score         = 0
        self.max_score     = 0
        self.correct_count = 0
        self._show_quiz()


# ===================== RUN =====================
if __name__ == "__main__":
    app = AgoraQuiz()
    app.mainloop()