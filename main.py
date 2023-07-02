from reactpy import component, html, run
from reactpy.backend.starlette import configure
from starlette.applications import Starlette

@component
def Photo():
    return html.img(
        {
            "src": "https://picsum.photos/id/237/500/300",
            "style": {"width": "50%"},
            "alt": "Puppy",
        }
    )


run(Photo)


app = Starlette()
configure(app, HelloWorld)