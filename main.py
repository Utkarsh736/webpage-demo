from fh_bootstrap import *
from app import *
from home import page as home_page
from blog import page as blog_page

hdrs = (
    Link(href='/assets/hl-styles.css', rel='stylesheet'),
    Link(href='/assets/styles.css', rel='stylesheet'),
    *Socials(title='About FastHTML', description='Learn the foundations of FastHTML', site_name='about.fastht.ml',
             twitter_site='@answerdotai', image=f'/assets/og-sq.png', url='')
)


app, rt = fast_app()

app.get('/')(home_page)
app.get('/blog')(blog_page)

serve()