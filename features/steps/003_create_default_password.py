from behave import *

@then('Click on all 7 buttons APPLEID, DEFAULT, NTLM, SECURITYQ, WEB16, WEB32, WIFI')
def clck_svn_btns(context):
    """
    Click on all 7 buttons APPLEID, DEFAULT, NTLM, SECURITYQ, WEB16, WEB32, WIFI
    """
    context.app.main_page.clck_svn_btns()


@step("Click on Generate 3 Passwords button")
def clck_thr_pswd_btn(context):
    """
    Click on Generate 3 Passwords button
    """
    context.app.main_page.clck_thr_pswd_btn()


@then('Verify Passwords Field is not empty and has a content "{rows}" rows and "{cols}" cols')
def pswd_fld_hs_cntnt(context, rows, cols):
    """
    Verify Passwords Field is not empty and has a content "3" rows and "64" cols
    """
    context.app.main_page.pswd_fld_hs_cntnt(rows, cols)


@step('Verify STRENGTH Field is not empty and has a content "{strngth_pswd}"')
def strngth_fld_hs_cntnt(context, strngth_pswd):
    """
    Verify STRENGTH Field is not empty and has a content "Good"
    """
    context.app.main_page.strngth_fld_hs_cntnt(strngth_pswd)