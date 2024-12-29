from flask import Flask,render_template,request,jsonify

app = Flask(__name__)



questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        "answer": "A",
        "50_50": ["A) Paris", "C) Rome"]
    },
    {
        "question": "Who wrote 'Harry potter'?",
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Leo Tolstoy"],
        "answer": "B",
        "50_50": ["B) William Shakespeare", "C) Mark Twain"]
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B",
        "50_50": ["B) Mars", "D) Venus"]
    },
    {
        "question": "In which year did India gain independence?",
        "options": ["A) 1945", "B) 1947", "C) 1950", "D) 1960"],
        "answer": "B",
        "50_50": ["B) 1947", "C) 1950"]
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A) O2", "B) H2O", "C) CO2", "D) NaCl"],
        "answer": "B",
        "50_50": ["B) H2O", "D) NaCl"]
    },
    {
        "question": "Who was the first President of India?",
        "options": ["A) Jawaharlal Nehru", "B) Mahatma Gandhi", "C) Rajendra Prasad", "D) Sardar Patel"],
        "answer": "C",
        "50_50": ["C) Rajendra Prasad", "D) Sardar Patel"]
    },
    {
        "question": "What is the longest river in the world?",
        "options": ["A) Nile", "B) Amazon", "C) Ganges", "D) Mississippi"],
        "answer": "A",
        "50_50": ["A) Nile", "B) Amazon"]
    },
    {
        "question": "Which is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "C",
        "50_50": ["C) Jupiter", "D) Saturn"]
    },
    {
        "question": "Which Indian city is also known as the Silicon Valley of India?",
        "options": ["A) Mumbai", "B) Hyderabad", "C) Bangalore", "D) Chennai"],
        "answer": "C",
        "50_50": ["B) Hyderabad", "C) Bangalore"]
    },
    {
        "question": "Who is the author of the book 'The God of Small Things'?",
        "options": ["A) Arundhati Roy", "B) Jhumpa Lahiri", "C) Salman Rushdie", "D) Vikram Seth"],
        "answer": "A",
        "50_50": ["A) Arundhati Roy", "D) Vikram Seth"]
    },
    {
        "question": "Which element is needed for combustion to take place?",
        "options": ["A) Nitrogen", "B) Oxygen", "C) Hydrogen", "D) Helium"],
        "answer": "B",
        "50_50": ["B) Oxygen", "D) Hydrogen"]
    },
    {
        "question": "Which country won the FIFA World Cup in 2018?",
        "options": ["A) Brazil", "B) Germany", "C) France", "D) Argentina"],
        "answer": "C",
        "50_50": ["C) France", "A) Brazil"]
    },
    {
        "question": "Who is known as the 'Iron Man of India'?",
        "options": ["A) Bhagat Singh", "B) Sardar Patel", "C) Subhas Chandra Bose", "D) Lal Bahadur Shastri"],
        "answer": "B",
        "50_50": ["B) Sardar Patel", "C) Subhas Chandra Bose"]
    },
    {
        "question": "In which year did man land on the moon for the first time?",
        "options": ["A) 1965", "B) 1969", "C) 1971", "D) 1975"],
        "answer": "B",
        "50_50": ["B) 1969", "C) 1971"]
    }
]


lifelines_used = {"50_50": False}



prize_money = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 70000000]

@app.route("/")
def home():
    return render_template("game.html")


    def ask_question(q, level):
       
        print(f"\n{q['question']}")
        for option in q['options']:
            print(option)


    
    
    use_lifeline = input("Do you want to use the 50:50 lifeline? (yes/no): ").strip().lower()
    
    if use_lifeline == "yes" and not lifelines_used["50_50"]:
        lifelines_used["50_50"] = True
        print("\n50:50 Lifeline activated! Your options are:")
        for option in q['50_50']:
            print(option)
    elif use_lifeline == "yes":
        print("Sorry, you've already used the 50:50 lifeline.")




    
    answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    
    if answer == q["answer"]:
        print(f"Correct! You won ₹{prize_money[level]}!\n")
        return True
    else:
        
        guaranteed_amount = 0
        if level >= 4: 
            guaranteed_amount = prize_money[4]
        elif level >= 9: 
            guaranteed_amount = prize_money[9]
        print(f"Wrong! The correct answer was {q['answer']}. You leave with ₹{guaranteed_amount}.\n")
        return False

def kbc_game():
   
    print("Welcome to Kaun Banega Crorepati!\n")
    
    for i, question in enumerate(questions):
        print(f"Question {i+1} for ₹{prize_money[i]}:")
        if not ask_question(question, i):
            print("\nGame over! Better luck next time.")
            break
    else:
        print("\nCongratulations! You are a Crorepati! You won ₹7 Crore!")
    
kbc_game()
