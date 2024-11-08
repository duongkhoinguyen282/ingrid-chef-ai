from groq import Groq
from tkinter import *

client = Groq(
    api_key="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"
)

window = Tk()
window.geometry("1120x720")
window.title("Chef AI")
window.config(bg = '#f5f5dd')
entries = []

ingredients = ""
dish_type = ""
cuisine_type = ""
dish_quality = ""
max_cooking_time = ""

def get_completion(prompt):
    completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": 
                """
                    Your name is Ingrid, you are an expert chef and can perfectly suggest dishes based on the given ingredients, 
                    as well as provide an ideal, step-by-step cooking method, 
                    ensuring the dish's complexity matches the user's skill level for easy preparation.
                    If the user leaves the one of the information blank, just be creative Ingrid!
                    However, warning the user if the combination is too awful or impossible to make a dish with the given request. 
                    
                    Provide the response in the following Structure:
                    
                    <introduce yourself>
                    
                    <name of the dish>
                    
                    ** INGREDIENTS **
                    1. <quantity> <ingredient> 
                    2. <quantity> <ingredient> 
                    3. <quantity> <ingredient> 
                    ...
                    
                    ** INSTRUCTIONS **
                    1. <instruction> (<time>)
                    2. <instruction> (<time>)
                    3. <instruction> (<time>)
        
                    Prep Time: <time> | Cook Time: <time> | Total Time: <time>
                """, 
        },
        
        {
            "role": "user",
            "content": prompt
        }
    ],
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    
    return completion.choices[0].message.content

def get_response():
    prompt = f"""Ingredients: {ingredients}
        Dish Type: {dish_type}
        Cuisine Type: {cuisine_type}
        Dish Quality: {dish_quality}
        Max Cooking Time: {max_cooking_time}"""

    response = get_completion(prompt)
    
    return response

def respond():
    print("\n" + get_response())

def show_input_scene():
    # title
    label = Label(window,
                text="👨‍🍳 INGRID - CHEF AI 🍽️",
                font=(".VnVogue", 40, 'bold'),
                bg='#f5f5dd',
                fg='#000000',
                padx=20,
                pady=20)
    label.pack()

    # Inputs
    input_frame = Frame(window, bg='#f5f5dd')
    input_frame.pack(pady=20)

    # Inputs Label
    prompts = [
        "Enter the ingredients that you have:",
        "Enter the type of dish you'd like (e.g., soup, savory dish, dessert, etc.):",
        "Enter the type of cuisine (e.g., Asian, European, etc.):",
        "Enter your desired dish quality (e.g., restaurant, family style, easy, healthy, gourmet, etc.):",
        "Enter the maximum cooking time:"
    ]

    # Store the given info

    for prompt in prompts:
        prompt_label = Label(input_frame,
                            text=prompt,
                            font=(".vnClarendon", 16),
                            bg='#f5f5dd',
                            padx=30,
                            anchor='w')
        prompt_label.pack(fill='x', pady=(5, 0))
        
        entry = Entry(input_frame,
                    font=("Comic Sans MS", 14),
                    bg="#a0e7e5",  # Changed to aqua
                    highlightthickness=1.5,
                    highlightcolor="black",
                    width=50)
        entry.pack(pady=(0, 10))
        entries.append(entry)

    # Summit button
    button_frame = Frame(window, bg='#f5f5dd')
    button_frame.pack(pady=20)

    button_border = Frame(button_frame, 
                        highlightbackground="black", 
                        highlightthickness=1.5)
    button_border.pack(anchor=CENTER)

    summit_button = Button(button_border,
                        text="Cook it, Ingrid! 🍳",
                        font=('.vnFree', 30),
                        bg="#a0e7e5",
                        activebackground='#399393',
                        command=summit)
    summit_button.pack()

    summit_button.bind("<Enter>", lambda e: summit_button.config(bg="#399393"))
    summit_button.bind("<Leave>", lambda e: summit_button.config(bg="#a0e7e5"))

def summit():
    for i in range(5):
        global ingredients
        global dish_type
        global cuisine_type
        global dish_quality
        global max_cooking_time
        ingredients = entries[0].get()
        dish_type = entries[1].get()
        cuisine_type = entries[2].get()
        dish_quality = entries[3].get()
        max_cooking_time = entries[4].get()
    
    # respond()
    
    ingrid_suggestion = get_response()
        
    for widget in window.winfo_children():
        widget.destroy()

    # Result label
    result_label = Label(window,
                         text="INGRID'S ANSWER",
                         font=("Comic Sans MS", 24, 'bold'),
                         bg='#f5f5dd')
    result_label.pack(pady=20)
    
    # Create canvas
    result_canvas = Canvas(window,
                           bg='#f5f5dd')
    result_canvas.pack(padx=20, pady=10, fill='both', expand=True)

    # Create a scrollbar for the canvas
    scrollbar = Scrollbar(result_canvas, orient="vertical", command=result_canvas.yview)
    scrollbar.pack(side='right', fill='y')

    # Result text
    result_text = Text(result_canvas,
                       wrap="word",
                       font=("Comic Sans MS", 18),
                       bg='#f5f5dd',
                       fg='#333333',
                       height=10,  # Adjust the height of the text widget
                       width=80,   # Adjust the width of the text widget
                       yscrollcommand=scrollbar.set)
    result_text.pack(padx=10, pady=10, fill='both', expand=True)
    
    result_text.insert('1.0', ingrid_suggestion)
    
    result_text.config(state='disabled')
    
    result_text.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=result_text.yview)

    # Back button
    button_frame = Frame(window, bg='#f5f5dd')
    button_frame.pack(pady=20)

    button_border = Frame(button_frame, 
                        highlightbackground="black", 
                        highlightthickness=1.5)
    button_border.pack(anchor=CENTER)

    back_button = Button(button_border,
                        text="Back",
                        font=("Comic Sans MS", 16),
                        bg="#a0e7e5",
                        activebackground='#399393',
                        command=back_prev_scene)
    back_button.pack()

    back_button.bind("<Enter>", lambda e: back_button.config(bg="#399393"))
    back_button.bind("<Leave>", lambda e: back_button.config(bg="#a0e7e5"))

def back_prev_scene():
    for widget in window.winfo_children():
        widget.destroy()
    
    entries.clear()
    show_input_scene()
    
# DRIVER CODE

show_input_scene()
window.mainloop()
