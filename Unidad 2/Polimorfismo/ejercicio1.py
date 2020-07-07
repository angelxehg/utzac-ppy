class Film:

    def __init__(self, title, length=60.0):
        self.title = title
        self.length = length

    def __str__(self, show_type=True):
        start = '(' + self.__class__.__name__ + ') ' if show_type else ''
        return start + self.title + " | " + str(self.length) + " min"


class Drama(Film):

    def __init__(self, title, length=60.0, drama_charge=5):
        super(Drama, self).__init__(title, length)
        self.drama_charge = drama_charge

    def __str__(self, show_type=True):
        fragment = super(Drama, self).__str__(show_type)
        return fragment + " | " + str(self.length) + " min"


class Comedy(Film):

    def __init__(self, title, length=60.0, comedy_level=5):
        super(Comedy, self).__init__(title, length)
        self.comedy_level = comedy_level

    def __str__(self, show_type=True):
        fragment = super(Comedy, self).__str__(show_type)
        return fragment + " | " + str(self.comedy_level) + " level"


class Suspense(Film):

    def __init__(self, title, length=60.0, suspense_level=5):
        super(Suspense, self).__init__(title, length)
        self.suspense_level = suspense_level

    def __str__(self, show_type=True):
        fragment = super(Suspense, self).__str__(show_type)
        return fragment + " | " + str(self.suspense_level) + " level"


films = [
    Film("Generic Film"),
    Drama("Generic Drama", 90.0, 3),
    Comedy("Funny Comedy", 120.0),
    Suspense("Scary Suspense", 180.0, 5)
]

for film in films:
    print(film)
