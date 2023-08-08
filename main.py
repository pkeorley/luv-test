from reactpy import component, html, use_location, use_state
from reactpy.backend.flask import configure, Options
from reactpy_router import route, simple

from calculator import Calculator
from client import FlaskApplication
from modules.errors import MissingLink
from modules.labels import Labels

app = FlaskApplication()


@component
def Main():
    boy_name, set_boy_name = use_state("")
    girl_name, set_girl_name = use_state("")

    amour, set_amour = use_state(Labels.UNDEFINED)

    def clicked_love_calculator_button(e):
        set_amour(str(Labels.CALCULATED).format(
            boy_name=boy_name,
            girl_name=girl_name,
            percent=Calculator.calculate(
                boy_name=boy_name,
                girl_name=girl_name
            )
        ))

    return html.div(
        {"class_name": "application"},
        html.div(
            {"class_name": "parent"},
            html.div(
                html.p(amour)
            ),
            html.div(
                {"class_name": "block"},
                html.label({"for": "girl-name"}, Labels.GIRL_NAME),
                html.input({"id": "girl-name", "on_change": lambda e: set_girl_name(e["target"]["value"])})
            ),
            html.div(
                {"class_name": "block"},
                html.label({"for": "boy-name"}, Labels.BOY_NAME),
                html.input({"id": "boy-name", "on_change": lambda e: set_boy_name(e["target"]["value"])})
            ),
            html.button({"on_click": clicked_love_calculator_button}, Labels.CALCULATE_LOVE)
        )
    )


@component
def root():
    use_location()
    return simple.router(
        route("/", Main()),
        route("*", MissingLink()),
    )


configure(app, root, options=Options(
    head=(
        html.title("luv-test"),
        html.link({"rel": "stylesheet", "href": "static/styles.css"}),
        html.link({"href": "static/favicon.ico", "rel": "shortcut icon", "type": "image/x-icon"})
    ),
    url_prefix="/"
))


app.run(
    debug=True,
    port=8080
)

