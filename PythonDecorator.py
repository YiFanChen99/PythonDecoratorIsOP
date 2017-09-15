
class Ekko(object):
    @property
    def variable(self):
        return self._variable

    @variable.setter
    def variable(self, value):
        self._variable = value if isinstance(value, str) else ""

ekko = Ekko()
ekko.variable = [1,2,3]
print('ekko array:', type(ekko.variable))
ekko.variable = int(1)
print('ekko int:', type(ekko.variable))
ekko.variable = None
print('ekko None:', type(ekko.variable))
ekko.variable = 'WTF'
print('ekko str:', type(ekko.variable))
