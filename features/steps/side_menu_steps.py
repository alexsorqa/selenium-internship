from behave import given, when, then


@when('Click on Off-Plan at side menu')
def click_off_plan_left_menu(context):
    context.app.side_menu.click_on_off_plan()