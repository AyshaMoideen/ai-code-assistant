# import Tkinter for GUI creation
import tkinter as tk
# import os module to env
import os
# import dotenv to load API Key from .env file
from dotenv import load_dotenv
# import Groq library
from groq import Groq
# load env from .env file
load_dotenv()

# create Groq using API Key stored in env
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
    )

# create main application window
root = tk.Tk()
# set application title
root.title("AI Code Assistant")
# set window size
root.geometry("600x450")
# set bg clr
root.configure(bg="#1e1e1e")

# create title label
title = tk.Label(root, text="AI Code Assistant",font=("Arial",18,"bold"),bg="#1e1e1e",fg="white")
# display title on window
title.pack(pady=10)

# create entry box for user qstns
entry = tk.Entry(root, width=60,font=("Arial",12))
# display entry box
entry.pack(pady=10)

# create output box to display output
output = tk.Text(root, height=15, width=70, font=("Consolas",10))
# display output box
output.pack(pady=10)

# function to send qsn to AI model
def ask_ai(question):
    try:
        # send user input to Groq AI model
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": question}
            ]
        )
        # return AI response text
        return response.choices[0].message.content

    except Exception as e:
        # return error if something goes wrong
        return f"Error: {e}"

# function executed when Ask Question button is clicked
def ask_question():
    # get text from entry box
    question = entry.get()
    # get AI  response
    answer = ask_ai(question)

    # clear previous output
    output.delete("1.0", tk.END)
    # insert new output
    output.insert(tk.END, answer)

# function to debug common prgrmming errors
def debug_error():
    # get user input and convert to lowercase
    error = entry.get().lower()
    # clear previous output
    output.delete("1.0", tk.END)
    
    # check for division by zero error
    if "division" in error or "zero" in error:
        output.insert(tk.END, "Cannot divide by zero\n")
    
    # check for index out of range
    elif "index" in error or "range" in error:
        output.insert(tk.END, "Check list index\n")
    
    # check for syntax errors
    elif "syntax" in error:
        output.insert(tk.END, "Check brackets or missing colon\n")
    
    # default message if error is unknown
    else:
        output.insert(tk.END, "Error not recognised\n")

# create frame for buttons
btn_frame = tk.Frame(root)
# display button frame
btn_frame.pack(pady=10)

# create Ask Question button
tk.Button(btn_frame, text="Ask Question", width=15, command=ask_question, bg="#007acc", fg="white").grid(row=0, column=0, padx=10)

# create Debug Error button
tk.Button(btn_frame, text="Debug Error", width=15, command=debug_error, bg="#e67e22", fg="white").grid(row=0, column=1, padx=10)

# run the Tkinter application
root.mainloop()