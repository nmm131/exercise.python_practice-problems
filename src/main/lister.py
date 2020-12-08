# Created by Leon Hunter at 12:10 PM 12/08/2020
class Lister(object):
    def get_integer_list(self, start, stop, step):
        if step != 0:
            result = []
            for value in range(start, stop + 1, step):
                result.append(value)
            return result
        return [0]

    def get_even_list(self, start, stop, step):
        if step != 0:
            result = []
            for value in range(start, stop + 1, step):
                if value % 2 == 0:
                    result.append(value)
            return result
        return [0]

    def get_odd_list(self, start, stop, step):
        if step != 0:
            return [value for value in range(start, stop + 1, step) if value % 2 != 0]
        return []
