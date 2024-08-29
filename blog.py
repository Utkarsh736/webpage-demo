from app import *

def page():
    h2s = 'Blog Post 1', 'Blog Post 2'
    txts = [
        Markdown("This is the content of the first blog post."),
        Markdown("This is the content of the second blog post.")
    ]
    secs = Sections(h2s, txts)

    return BstPage(1, 'Blog - FastHTML', *secs)