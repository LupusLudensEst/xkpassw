from behave import *

@given("Loginpage")
def open_homepage(context):
    """
    Loginpage
    """
    context.app.main_page.open_page()

@then('Verify text 1 "{txt}" is here')
def vrfy_this_srvs_here(context, txt):
    """
    Verify text "XKPasswd - A Secure Memorable Password Generator" is here
    """
    context.app.main_page.vrfy_this_srvs_here(txt)


@then('Verify text 2 "{txt}" is here')
def vrfy_brt_bssch_here(context, txt):
    """
    Verify text 2 "Bart Busschots" is here
    """
    context.app.main_page.vrfy_brt_bssch_here(txt)


@step('Verify text 3 "{txt}" is here')
def vrfy_url_brtb_here(context, txt):
    """
    Verify text 3 "www.bartb.ie/xkpasswd" is here
    """
    context.app.main_page.vrfy_url_brtb_here(txt)