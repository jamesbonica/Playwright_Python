from playwright.sync_api import Page

class HomePage:

    def __init__(self,page:Page):
        self.page = page
        self.upgrade_button = page.get_by_role('button', name='Upgrade')
        self.performance_link = page.get_by_role('link', name='Performance')
        self.dashboard_link = page.get_by_role('link', name='Dashboard')


    def click_performance(self):
        self.performance_link.click()

    def click_dashboard(self):
        self.dashboard_link.click()
