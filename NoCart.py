import tkinter as tk
import random

# Useless responses
search_responses = [
    "Searching is exhausting. Try again never.",
    "The search button is decorative only.",
    "I'm just a button. I do nothing.",
    "Search denied. No reason.",
    "Search? No thanks."
]

enter_key_responses = [
    "That item doesn't exist. Try air instead.",
    "Searched. Still found nothing useful.",
    "Oops! Our imaginary stock is empty.",
    "We found 0 results and 1 excuse.",
    "Good news: Your item is lost forever."
]

add_to_cart_responses = [
    "Cart is emotionally unavailable.",
    "Adding failed. Item said no.",
    "Try later. Or don’t.",
    "Our cart is full of disappointment.",
    "That item rejected your request."
]

checkout_responses = [
    "Checkout is having an identity crisis.",
    "Do you *really* need those snacks?",
    "Payment gateway is watching cat videos.",
    "Not today. The cart union is protesting.",
    "Your money deserves better."
]

# Colors and font
bg_color = "#e0fff9"
button_color = "#00c2a8"
text_color = "#064e45"
font_main = ("Helvetica", 13)
font_title = ("Helvetica", 20, "bold")

# App window
root = tk.Tk()
root.title("NoCart - The Grocery App That Refuses")
root.geometry("460x500")
root.config(bg=bg_color)

# Title
title = tk.Label(root, text="🛒 NoCart", font=font_title, bg=bg_color, fg=text_color)
title.pack(pady=20)

# Frame for search bar + button
search_frame = tk.Frame(root, bg=bg_color)
search_frame.pack(pady=10)

# Search entry
search_entry = tk.Entry(search_frame, font=font_main, width=25, bd=2, relief="flat",
                        highlightthickness=2, highlightbackground=button_color)
search_entry.grid(row=0, column=0, padx=(0, 10))

# Result display label
result_label = tk.Label(root, text="", wraplength=360, font=font_main, bg=bg_color,
                        fg=text_color, justify="center")
result_label.pack(pady=30)

# Search button that refuses to work
def useless_search_button():
    result_label.config(text=random.choice(search_responses))

search_button = tk.Button(
    search_frame, text="🔍", font=("Helvetica", 12),
    bg=button_color, fg="white", activebackground="#009988",
    relief="flat", bd=0, width=3, cursor="hand2",
    command=useless_search_button
)
search_button.grid(row=0, column=1)

# Actual working function triggered by Enter key
def actual_search(event=None):
    query = search_entry.get().strip()
    if not query:
        result_label.config(text="Searching nothing returned nothing. Impressive.")
    else:
        result_label.config(text=random.choice(enter_key_responses))

# Bind Enter key to actual search function
search_entry.bind("<Return>", actual_search)

# Rounded button helper
def round_button(master, text, command, width=160):
    return tk.Button(
        master,
        text=text,
        command=command,
        font=font_main,
        bg=button_color,
        fg="white",
        activebackground="#009988",
        activeforeground="white",
        relief="flat",
        width=int(width / 10),
        height=2,
        bd=0,
        cursor="hand2"
    )

# Add to cart button (rounded)
add_button = round_button(root, "Add to Cart", lambda: result_label.config(text=random.choice(add_to_cart_responses)))
add_button.pack(pady=10)

# Checkout button at bottom-right
def place_checkout():
    checkout_button = round_button(root, "Checkout", lambda: result_label.config(text=random.choice(checkout_responses)), width=120)
    checkout_button.place(relx=1.0, rely=1.0, x=-20, y=-20, anchor="se")

place_checkout()

# Run the app
root.mainloop()

