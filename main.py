import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "d99fb2d4fdab485a8a2f496828185e33"

def get_news():
    query = entry.get()
    
    if query == "":
        messagebox.showwarning("Warning", "Enter a topic!")
        return
    
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={API_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        result_box.delete(1.0, tk.END)
        
        if data["status"] != "ok":
            result_box.insert(tk.END, "❌ Error fetching news")
            return
        
        articles = data["articles"]
        
        for i, article in enumerate(articles[:5], 1):
            result_box.insert(tk.END, f"{i}. {article['title']}\n", "title")
            result_box.insert(tk.END, f"{article['url']}\n\n", "link")
    
    except Exception as e:
        result_box.insert(tk.END, str(e))


# GUI Window
root = tk.Tk()
root.title("News App 📰")
root.geometry("650x450")
root.configure(bg="white")

# Title
title_label = tk.Label(root, text="📰 News Aggregator", 
                       font=("Arial", 16, "bold"),
                       bg="white", fg="red")
title_label.pack(pady=10)

# Entry box
entry = tk.Entry(root, width=40, font=("Arial", 12, "bold"),
                 bd=3, relief="solid")
entry.pack(pady=10)

# Button
btn = tk.Button(root, text="Get News", command=get_news,
                font=("Arial", 12, "bold"),
                bg="red", fg="white", padx=10, pady=5)
btn.pack(pady=5)

# Output box
result_box = tk.Text(root, wrap="word", width=75, height=15,
                     font=("Arial", 10),
                     bd=3, relief="solid")
result_box.pack(pady=10)

# Styling tags
result_box.tag_config("title", font=("Arial", 11, "bold"), foreground="black")
result_box.tag_config("link", foreground="blue")

# Run app
root.mainloop()

'''result box configuration ids:'''
# result_box.tag_config("title", font=("Arial", 11, "bold"), foreground="black")
