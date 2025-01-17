from behave import given, when, then


@then('Select {option} in Sales status menu')
def click_on_sales_status(context, option):
    context.app.off_plan_page.select_sales_status(option)


@then('Verify each product contains {option}')
def verify_contains_option(context, option):
    context.app.off_plan_page.verify_contains_option(option)