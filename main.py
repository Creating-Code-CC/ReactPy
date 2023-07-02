from reactpy import component, html
from reactpy.backend.starlette import configure
from starlette.applications import Starlette

@component
def HelloWorld():
    return html.div(
            html.h1("My Todo List"),
            html.ul(
                html.li("Design a cool new app"),
                html.li("Build it"),
                html.li("Share it with the world!"),
            )
        )


app = Starlette()
configure(app, HelloWorld)