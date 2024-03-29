import tkinter as tk
import pyshorteners as ps

# Shortens url using TinyURL
def shorten():
    s = ps.Shortener()
    short_url = s.tinyurl.short(long_url_entry.get()) # Gets url from entry
    short_url_entry.insert(0, short_url) # Inserts shortened url in second entry to be copied

# Window settings
root = tk.Tk()
root.title('Python URL Shortner')
root.geometry('400x250')
root.iconbitmap('./icon.ico')
root.configure(background= '#141414', border= 15)

# Widgets
long_url_label = tk.Label(root, text= 'Enter the long URL below', bg= '#141414', fg= '#FFFFFF', 
                          font=('Arial', 10, 'bold'))
long_url_entry = tk.Entry(root)
short_url_label = tk.Label(root, text= 'Shortened URL', bg= '#141414', fg= '#FFFFFF', font=('Arial', 10, 'bold'))
short_url_entry = tk.Entry(root)
shorten_button = tk.Button(root, text= 'Shorten URL', command= shorten, bg= '#011638', fg= '#FFFFFF', 
                           font=('Arial', 10, 'bold'))
foot_note = tk.Label(root, text= 'Made with ♥ by Kayler Moura', pady= 15, bg= '#141414', fg= '#FFFFFF')

# Widgets placement
long_url_label.pack(pady= 10)
long_url_entry.pack(pady= 5)
short_url_label.pack(pady= 10)
short_url_entry.pack(pady= 5)
shorten_button.pack(pady= 15)
foot_note.pack()

# App control
root.mainloop()
print('Window closed by user')