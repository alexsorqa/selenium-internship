from behave import given, when, then


@given('Open Main Page')
def open_main_page(context):
    context.app.main_page.open_main()
