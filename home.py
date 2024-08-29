from app import *

def page():
    caption = "'Real' web development shouldn't be this hard..."
    # fig = Image('/assets/webdev.jpg', alt='Web Development', caption=caption, left=False)

    h2s = 'Getting Started', 'Background', 'Current Status'
    txts = [
        Markdown(s1),
        Div (Markdown(s2)), # fig <- add
        Markdown(s3)
    ]
    secs = Sections(h2s, txts)

    return BstPage(0, 'Home - FastHTML', *secs)

s1 = """ FastHTML is a new way to create modern interactive web apps. It scales down to a 6-line python file, and scales up to complex production apps. Auth, DBs, caching, styling, etc are all built-in, and replaceable and extensible. 1-click deploy is available to Railway, Vercel, Huggingface, and more---or deploy to any Python server or VPS, including Azure, GCP, and AWS. You're using a FastHTML app right now. We didn't create a separate blog system for this site, because building apps with FastHTML is so easy there's no need for it! Here is the [source code](https://github.com/AnswerDotAI/fh-about/blob/main/overview.py) for the current page, for instance. You'll see that the code is very simple, relying on Python components like `Markdown` to build the page. The components are simple Python functions---here is the [source code for `Markdown`](https://github.com/AnswerDotAI/fh-about/blob/main/app.py#L6), taking just one line of code! Out of the box FastHTML provides authentication, [database](/tech#sec5) access, styles (via [PicoCSS](https://picocss.com/)), and more. Every part of the system is extensible and replacable using pip-installable Python modules. The site you're reading right now provides background information about the key concepts and ideas behind FastHTML. The [documentation](https://docs.fastht.ml/) focuses on the code. Because FastHTML brings together many different web technologies, it's worth investing some time to understand how it all fits together. Have a look through the five sections in the green navbar (or hamburger menu if you're on mobile) above to deepen your understanding. """

s2 = """ FastHTML is a system for writing web applications in Python. It is designed to be simple, powerful, and flexible. It is also designed to be easy to learn and use. The project is inspired by technologies such as React JSX, Hotwire, Astro, FastAPI, and Phoenix LiveView. FastHTML is small and simple---at the time of writing, it's under 1000 lines of code. That's because it's built on top of powerful and flexible foundations: Python, Starlette, Uvicorn, and HTMX. """

s3 = """ FastHTML works well right now, but it is still young. We are using it for nearly every part of the FastHTML project itself. We're working on a number of things to make FastHTML even better. Not everything is ready "out of the box" yet. If you see something missing that you need, please let us know by [creating an issue](https://github.com/AnswerDotAI/fasthtml/issues). """