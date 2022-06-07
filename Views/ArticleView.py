from tkinter import Canvas, ttk, Label, LEFT, PhotoImage, Toplevel


def show(article):
    top = Toplevel()

    top.geometry("800x600")
    top.configure(bg="#313335")
    top.wm_title("Article")

    sub_canvas = Canvas(
        top,
        bg="#212020",
        width=800,
        height=600,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    sub_canvas.place(x=0, y=0)
    ASSETS_PATH = "resources/assets"
    text_box_bg = PhotoImage(file=ASSETS_PATH + "/no-author.png")

    # print(article.content)

    title = Label(sub_canvas, text="Title", background="#7D7F80", fg="#212020", font=("Arial-BoldMT", int(13.0)))
    title.place(x=800 / 4, y=50.0)

    title_content = Label(sub_canvas, text=article.title, bg="#212020", fg="#E7E7E8",
                          font=("Arial-BoldMT", int(13.0)))
    title_content.place(x=800 / 4, y=100.0)

    sub_canvas.create_line(800 / 4 - 20, 150, 700, 150, fill="#7D7F80")

    sub_canvas.create_image(800 / 4 + 50, 250.5, image=text_box_bg)

    publish_date = Label(sub_canvas, text="Publish Date", background="#7D7F80", fg="#212020",
                         font=("Arial-BoldMT", int(13.0)))
    publish_date.place(x=350, y=200)

    publish_date_content = Label(sub_canvas, text=article.publishDate, bg="#212020", fg="#E7E7E8",
                                 font=("Arial-BoldMT", int(13.0)))
    publish_date_content.place(x=460, y=200.0)

    author = Label(sub_canvas, text="Authors", background="#7D7F80", fg="#212020",
                   font=("Arial-BoldMT", int(13.0)))
    author.place(x=350, y=250)

    author_content = Label(sub_canvas, text=",".join(article.authors), bg="#212020", fg="#E7E7E8",
                           font=("Arial-BoldMT", int(13.0)))
    author_content.place(x=350, y=280.0)

    # abstract = Label(sub_canvas, text="Abstract", background="#7D7F80", fg="#212020",
    #                  font=("Arial-BoldMT", int(13.0)))
    # abstract.place(x=350, y=320)

    container = ttk.Frame(top, width=500)

    container.place(x=800 / 4 - 20, y=350)

    canvas = Canvas(container, width=500)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)

    scrollable_frame = ttk.Frame(canvas, width=600)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, width=500)

    canvas.configure(yscrollcommand=scrollbar.set)

    abstract_content = Label(scrollable_frame, text=article.content, bg="#212020", fg="#E7E7E8",
                             font=("Arial-BoldMT", int(13.0)), width=500, anchor="w", justify=LEFT)
    abstract_content.pack()

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=True)

    sub_canvas.create_line(800 / 4 - 20, 570, 700, 570, fill="#7D7F80")
    top.resizable(False, False)
    top.mainloop()
