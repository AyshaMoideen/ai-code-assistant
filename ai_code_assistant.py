import tkinter as tk
import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
    )

#window
root = tk.Tk()
root.title("AI Code Assistant")
root.geometry("600x450")
root.configure(bg="#1e1e1e")

#title
title = tk.Label(root, text="AI Code Assistant",font=("Arial",18,"bold"),bg="#1e1e1e",fg="white")
title.pack(pady=10)

#entry box
entry = tk.Entry(root, width=60,font=("Arial",12))
entry.pack(pady=10)

#output box
output = tk.Text(root, height=15, width=70, font=("Consolas",10))
output.pack(pady=10)

def ask_ai(question):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"

def ask_question():
    question = entry.get()
    answer = ask_ai(question)

    output.delete("1.0", tk.END)
    output.insert(tk.END, answer)

def debug_error():
    error = entry.get().lower()
    output.delete("1.0", tk.END)

    if "division" in error or "zero" in error:
        output.insert(tk.END, "Cannot divide by zero\n")

    elif "index" in error or "range" in error:
        output.insert(tk.END, "Check list index\n")

    elif "syntax" in error:
        output.insert(tk.END, "Check brackets or missing colon\n")

    else:
        output.insert(tk.END, "Error not recognised\n")

#buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Ask Question", width=15, command=ask_question, bg="#007acc", fg="white").grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Debug Error", width=15, command=debug_error, bg="#e67e22", fg="white").grid(row=0, column=1, padx=10)

root.mainloop()