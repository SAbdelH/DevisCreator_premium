class Update:
    def on_page_changed(self, text):
        if text == '_p_login':
            self.maindialog.switchPageConnexion(0, self.checkLicence)
        elif text == '_p_user_management':
            self.populateUserList()
        elif text == '_p_info_company':
            if self.WorkspaceExist() : self.populateInfoCompany()
        elif text == '_p_dashboard':
            self.populateAgenda()

    def on_menu_clicked(self, text):
        if text == 'logout':
            self.disconnect()