class Women:
    women_id = "this is women id"
    women_name = "this is woman name"
    women_age = "this is woman age"

    def __init__(self, login, pasw):
        self.login = login
        self.pasw = pasw
        self.meta = self.Meta(login + "@" + pasw)

    class Meta:
        def __init__(self, access):
            self._access = access


w = Women(login="root", pasw="1234")
print(w.__dict__)
print(w.meta.__dict__)            



