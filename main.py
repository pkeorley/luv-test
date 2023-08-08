from reactpy import component, html, use_location, use_state
from reactpy.backend.flask import configure, Options
from reactpy_router import route, simple

from modules.calculator import Calculator
from client import FlaskApplication
from modules.errors import MissingLink
from modules.labels import Labels, Languages

app = FlaskApplication()


@component
def Main():
    _ = Labels()
    language, set_language = use_state(Languages.EN)

    boy_name, set_boy_name = use_state("")
    girl_name, set_girl_name = use_state("")

    def change_page_language(e):
        set_language(e["target"]["value"])

    return html.div(
        {"class_name": "application"},

        html.select({"class_name": "language-selector", "on_change": change_page_language}, (
            html.option({"value": language}, language)
            for language in _.available_languages
        )),

        html.div(
            {"class_name": "parent"},
            html.div(
                html.p(
                    (_.get(language, "CALCULATED").format(
                        boy_name=boy_name,
                        girl_name=girl_name,
                        percent=Calculator.calculate(
                            boy_name=boy_name,
                            girl_name=girl_name
                        )
                    )) if all((boy_name, girl_name)) else _.get(language, "UNDEFINED")
                )
            ),
            html.div(
                {"class_name": "block"},
                html.label({"for": "girl-name"}, _.get(language, "GIRL_NAME")),
                html.input({"id": "girl-name", "on_change": lambda e: set_girl_name(e["target"]["value"])})
            ),
            html.div(
                {"class_name": "block"},
                html.label({"for": "boy-name"}, _.get(language, "BOY_NAME")),
                html.input({"id": "boy-name", "on_change": lambda e: set_boy_name(e["target"]["value"])})
            )
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)

