from fasthtml.common import *

app, rt = fast_app()


@rt("/")
def get():
    return Div(P("Hello Worldddd!"), hx_get="/change")


serve()
