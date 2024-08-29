from fh_bootstrap import *
from itertools import chain
from markdown import markdown


md_exts='codehilite', 'smarty', 'extra', 'sane_lists'
def Markdown(s, exts=md_exts, **kw): return Div(NotStr(markdown(s, extensions=exts)), **kw)

def BstPage(selidx, title, *c):
    navitems = [('Home', '/'), ('Blog', '/blog')]
    # logo = 'assets/logo_tmp.jpg'
    ra_items = (A('Docs', href='https://docs.fastht.ml', cls="nav-link"),
                Icon('fab fa-github', dark=False, sz='lg', href='https://github.com/AnswerDotAI/fasthtml', cls='ms-2 px-2'))
    
    return (
        Title(title),
        Container(
            Navbar('nav', selidx, items=navitems, ra_items=ra_items, cls='navbar-light bg-secondary rounded-lg'),
                # image=f'/{logo}'),
            Toc(Container(H1(title), *c)),
            # BstFooter('© 2024 FastHTML', File(logo), img_href='https://fastht.ml'),
            typ=ContainerT.Xl, cls='mt-3', data_bs_spy='scroll', data_bs_target='#toc'
        )
    )

def Sections(h2s, texts):
    colors = 'yellow', 'pink', 'teal', 'blue'
    div_cls = 'py-2 px-3 mt-4 bg-light-{} rounded-tl-lg'
    return chain([Div(H2(h2, id=f'sec{i+1}', cls=div_cls.format(colors[i%4])), Div(txt, cls='px-2'))
                  for i,(h2,txt) in enumerate(zip(h2s, texts))])