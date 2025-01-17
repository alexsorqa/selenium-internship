from behave import given, when, then


@then('Log in to the page with {email} and {password}')
def login_to_the_page(context, email, password):
    context.app.sign_in_page.login_sign_in_page(email, password)