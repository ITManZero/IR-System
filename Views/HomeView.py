from tkinter import Label, Entry, Tk, Canvas, PhotoImage, RIGHT, VERTICAL, Scrollbar, NW, NE, Button, HORIZONTAL
import Views.ArticleView as articleView
from Utils.search import match


def searchQuery(canvas, token_entry, vectorizerX, doc_vector, articles):
    canvass = Canvas(canvas, bg="#212020", width=400, height=300, bd=0,
                     highlightthickness=0, )

    canvass.place(x=400 / 3 + 20, y=150)
    query = token_entry.get()
    indices = match(vectorizerX, doc_vector, query)

    def callbacks(event):
        print(event.widget.cget("text").split("-")[0])
        article = articles[int(event.widget.cget("text").split("-")[0])]
        articleView.show(article)

    y = 0
    for i in indices[0:25]:
        label = Label(canvass, text=str(i) + "-" + articles[i].title, font=("ComicSansMS", 12), compound=RIGHT,
                      cursor="hand2", background="#212020", fg="white")
        label.bind("<Button-1>", callbacks)
        label.pack(anchor="w")
        canvass.create_window(0, y, window=label, anchor=NW)
        y += 25

    scrollbar = Scrollbar(canvass, orient=VERTICAL, command=canvass.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
    canvass.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, y))

    # scrollbarr = Scrollbar(canvass, orient=HORIZONTAL, command=canvass.xview)
    # scrollbarr.place(relx=0, rely=1, relwidth=1)
    #
    # canvass.config(xscrollcommand=scrollbarr.set, scrollregion=(0, 0, y, 0))


def show(articles, vectorizerX, doc_vector):
    window = Tk()

    window.configure(bg="#313335")
    window.wm_title("Search Engine")
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    w = 600
    h = 450
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.update()

    canvas = Canvas(window, bg="#212020", width=window.winfo_width(), height=window.winfo_height(), bd=0,
                    highlightthickness=0, )

    canvas.place(x=0, y=0)

    ASSETS_PATH = "resources/assets"
    text_box_bg = PhotoImage(file=ASSETS_PATH + "/python (3).png")
    canvas.create_image(50, 100, image=text_box_bg)

    token_entry = Entry(bd=0, bg="#AFB1B3", highlightthickness=1, highlightcolor="#2B2B2B")
    token_entry.place(x=400 / 3 + 20, y=90, width=380, height=35)

    text_box_bbg = PhotoImage(file=ASSETS_PATH + "/search.png")
    b1 = Button(canvas, background="#212020", image=text_box_bbg, highlightthickness=0, bd=0,
                command=lambda: searchQuery(canvas, token_entry, vectorizerX, doc_vector, articles))
    b1.place(x=550, y=90)

    # canvas.create_image(560, 105, image=text_box_bbg)

    window.resizable(False, False)
    window.mainloop()


def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()
