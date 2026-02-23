from tkinter import *
from tkinter import messagebox
import random


# -------------------------
# Global Variables
# -------------------------
names = []
asked = []
score = 0
qnum = 0


BG_COLOR = "#d591ff"  # Wheat background


# -------------------------
# ALL Questions (5)
# Format:
# id: [question, option1, option2, option3, option4, correct_text, correct_option_number]
# -------------------------
questions_answers = {
   1: ["At night, what must a towed vehicle have at the back of it?",
       "A white flag", "Reflective tape", "A white light", "A red light",
       "A red light", 4],


   2: ["You are waiting at a railway level crossing and the red lights continue to flash after the train has passed. What should you do?",
       "Drive on carefully",
       "Stay stopped until the lights stop flashing",
       "Check both ways and then drive on quickly",
       "Count to 15 and then drive on",
       "Stay stopped until the lights stop flashing", 2],


   3: ["What is the maximum legal speed for a car towing a trailer on the open road?",
       "70km/h", "80km/h", "90km/h", "100km/h",
       "90km/h", 3],


   4: ["When passing a horse and rider, what should you do?",
       "Sound your horn on approach",
       "Slow down and give plenty of room",
       "Increase speed to pass quickly",
       "Cross the centreline to pass",
       "Slow down and give plenty of room", 2],


   5: ["What is the safest way to carry goods inside a vehicle?",
       "On the passenger seat",
       "On the floor",
       "On the back seat",
       "Somewhere secure",
       "Somewhere secure", 4],

   6: ["How close can you park your vehicle to the approach side of a pedestrian crossing where no broken yellow lines have been marked?",
       "Ten metres",
       "Three metres",
       "One metre",
       "Six metres",
       "Six metres", 4],

   7: ["When are you allowed to pass another vehicle?",
       "When a vehicle has stopped at a pedestrian crossing",
       "When you are less than ten metres away from a railway crossing",
       "When can you see at least 100 metres of clear road in front of you once you have finished passing",
       "When you are passing a blind curve or blind bend",
       "When can you see at least 100 metres of clear road in front of you once you have finished passing", 3]
}


# -------------------------
# Random Question Selector
# -------------------------
def randomiser():
   """Select a random question that hasn't been asked yet."""
   global qnum
   qnum = random.randint(1, len(questions_answers))
   if qnum not in asked:
       asked.append(qnum)
   else:
       randomiser()


# -------------------------
# Starter Screen
# -------------------------
class QuizStarter:
   def __init__(self, parent):
       self.parent = parent
       self.frame = Frame(parent, bg=BG_COLOR)
       self.frame.pack(fill="both", expand=True)


       # Title
       Label(self.frame,
             text="NZ Road Rules Quiz",
             font=("Comic Sans MS", 30, "bold"),
             bg=BG_COLOR).pack(pady=30)


       Label(self.frame,
             text="Enter your name:",
             font=("Comic Sans MS", 14),
             bg=BG_COLOR).pack(pady=10)


       self.entry = Entry(self.frame, font=("Comic Sans MS", 14))
       self.entry.pack(pady=10)


       Button(self.frame,
              text="Start Quiz",
              font=("Comic Sans MS", 14),
              bg="#a591ff",
              command=self.start_quiz).pack(pady=10)


       Button(self.frame,
              text="Exit",
              font=("Comic Sans MS", 14),
              bg="#91ccff", fg="white",
              command=self.parent.destroy).pack(pady=10)


   def start_quiz(self):
       name = self.entry.get().strip()
       if name:
           names.append(name)
           self.frame.destroy()
           Quiz(self.parent)
       else:
           messagebox.showerror("Error", "Please enter your name.")


# -------------------------
# Quiz Screen (Title + Wrapped + 2x2 Options)
# -------------------------
class Quiz:
   def __init__(self, parent):
       self.parent = parent
       self.frame = Frame(parent, bg=BG_COLOR)
       self.frame.pack(fill="both", expand=True)


       # Container to keep layout centred nicely
       container = Frame(self.frame, bg=BG_COLOR)
       container.pack(expand=True, fill="x")


       container.columnconfigure(0, weight=1)
       container.columnconfigure(1, weight=1)


       # Title on quiz screen
       Label(container,
             text="NZ Road Rules Quiz",
             font=("Comic Sans MS", 26, "bold"),
             bg=BG_COLOR).grid(row=0, column=0, columnspan=2, pady=(10, 15))


       # Progress label (Question X of Y)
       self.progress_label = Label(container,
                                   text=f"Question {len(asked) + 1} of {len(questions_answers)}",
                                   font=("Comic Sans MS", 12),
                                   bg=BG_COLOR)
       self.progress_label.grid(row=1, column=0, columnspan=2, pady=(0, 15))


       randomiser()
       self.var = IntVar(value=0)


       # Update progress after randomiser has selected a new question
       # (asked already includes this question, so len(asked) is current question number)
       self.progress_label.config(text=f"Question {len(asked)} of {len(questions_answers)}")


       # Question text (wrap long text)
       Label(container,
             text=questions_answers[qnum][0],
             font=("Comic Sans MS", 18, "bold"),
             wraplength=900,
             justify="left",
             bg=BG_COLOR).grid(row=2, column=0, columnspan=2, sticky="w", padx=20, pady=(0, 25))


       # Answer options (wrap so nothing gets cut off)
       answer_wrap = 420


       Radiobutton(container,
                   text=questions_answers[qnum][1],
                   variable=self.var, value=1,
                   font=("Comic Sans MS", 14),
                   bg=BG_COLOR,
                   wraplength=answer_wrap,
                   justify="left",
                   anchor="w").grid(row=3, column=0, sticky="w", padx=20, pady=10)


       Radiobutton(container,
                   text=questions_answers[qnum][2],
                   variable=self.var, value=2,
                   font=("Comic Sans MS", 14),
                   bg=BG_COLOR,
                   wraplength=answer_wrap,
                   justify="left",
                   anchor="w").grid(row=3, column=1, sticky="w", padx=20, pady=10)


       Radiobutton(container,
                   text=questions_answers[qnum][3],
                   variable=self.var, value=3,
                   font=("Comic Sans MS", 14),
                   bg=BG_COLOR,
                   wraplength=answer_wrap,
                   justify="left",
                   anchor="w").grid(row=4, column=0, sticky="w", padx=20, pady=10)


       Radiobutton(container,
                   text=questions_answers[qnum][4],
                   variable=self.var, value=4,
                   font=("Comic Sans MS", 14),
                   bg=BG_COLOR,
                   wraplength=answer_wrap,
                   justify="left",
                   anchor="w").grid(row=4, column=1, sticky="w", padx=20, pady=10)


       Button(container,
              text="Confirm",
              font=("Comic Sans MS", 14),
              bg="#a591ff",
              command=self.check_answer).grid(row=5, column=0, columnspan=2, pady=25)


       Button(container,
              text="Quit",
              font=("Comic Sans MS", 14),
              bg="#91ccff", fg="white",
              command=self.parent.destroy).grid(row=6, column=0, columnspan=2, pady=(0, 15))


   def check_answer(self):
       global score


       if self.var.get() == 0:
           messagebox.showerror("Error", "Select an answer first.")
           return


       # Correct option number stored at index 6
       if self.var.get() == questions_answers[qnum][6]:
           score += 1


       # Next screen logic
       if len(asked) == len(questions_answers):
           self.frame.destroy()
           End(self.parent)
       else:
           self.frame.destroy()
           Quiz(self.parent)


# -------------------------
# End Screen
# -------------------------
class End:
   def __init__(self, parent):
       self.parent = parent
       self.frame = Frame(parent, bg=BG_COLOR)
       self.frame.pack(fill="both", expand=True)


       # Title
       Label(self.frame,
             text="NZ Road Rules Quiz",
             font=("Comic Sans MS", 30, "bold"),
             bg=BG_COLOR).pack(pady=25)


       # Simple pass rule (3/5 or more)
       total = len(questions_answers)
       result = "Passed" if score >= 5 else "Failed"


       Label(self.frame,
             text="Quiz Completed!",
             font=("Comic Sans MS", 22, "bold"),
             bg=BG_COLOR).pack(pady=10)


       Label(self.frame,
             text=f"Score: {score}/{total} — {result}",
             font=("Comic Sans MS", 18),
             bg=BG_COLOR).pack(pady=15)


       Button(self.frame,
              text="Play Again",
              font=("Comic Sans MS", 14),
              bg="blue", fg="white",
              command=self.restart).pack(pady=10)


       Button(self.frame,
              text="Quit",
              font=("Comic Sans MS", 14),
              bg="red", fg="white",
              command=self.parent.destroy).pack(pady=10)


   def restart(self):
       global asked, score
       asked = []
       score = 0
       self.frame.destroy()
       QuizStarter(self.parent)


# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
   root = Tk()
   root.title("NZ Road Rules Quiz")
   root.geometry("1000x700")
   root.configure(bg=BG_COLOR)
   root.resizable(False, False)


   QuizStarter(root)
   root.mainloop()
