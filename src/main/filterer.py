# Created by Leon Hunter at 12:10 PM 12/08/2020
class Filterer(object):
    def remove_characters(self, string_to_remove_from, characters_to_remove):
        result = str(string_to_remove_from)
        for char in string_to_remove_from:
            if char in characters_to_remove:
                result = result.replace(char, '')

        return result


    def remove_vowels(self, string_to_remove_from):
        result = ""
        vowels = ["a", "e", "i", "o", "u"]
        for char in string_to_remove_from:
            if char.lower() not in vowels:
                result += char

        return result


    def remove_consonants(self, string_to_remove_from):
        result = ""
        constants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        for char in string_to_remove_from:
            if char.lower() not in constants:
                result += char

        return result

