import json
import itertools


class DFA:
    def __init__(self, final_states, transitions, all_states):
        self.final_states = final_states
        self.transitions = transitions
        self.all_states = all_states

    def recognizes(self, string):
        current_state = 'q0'  # Asume que el estado inicial es 'q0'
        for char in string:
        # Busca la transición para el estado actual y el carácter actual
            transition = next((t for t in self.transitions if t[0] == current_state and t[1] == char), None)
            if transition is None:
            # Si no hay transición, la cadena no es reconocida
                return False
            else:
            # Si hay una transición, pasa al siguiente estado
                current_state = transition[2]
    # Si el estado final está en la lista de estados finales, la cadena es reconocida
        return current_state in self.final_states


def load_strings_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def check_string(strings, dfa):
    for i, string in enumerate(strings):
        if dfa.recognizes(string):
            print(f"El DFA reconoce la cadena número {i+1}: {string}")
        else:
            print(f"El DFA no reconoce la cadena número {i+1}: {string}")


def generate_strings(alphabet, x):
    # Inicializa la lista de cadenas vacía
    strings = []
    
    # Inicializa la longitud de la cadena en 1
    length = 1

    # Mientras no se hayan generado suficientes cadenas
    while len(strings) < x:
        # Genera todas las cadenas de la longitud actual
        for string_tuple in itertools.product(alphabet, repeat=length):
            # Si ya se han generado suficientes cadenas, termina el bucle
            if len(strings) >= x:
                break
            # Convierte la tupla a una cadena y añádela a la lista
            strings.append(''.join(string_tuple))
        # Incrementa la longitud para la próxima iteración
        length += 1

    return strings


def generar_alfabeto(n):
    return [chr(i) for i in range(65, 65+n)]


if __name__ == "__main__":
    file_path_dfa = input("Inserte la ruta del archivo .json con las transiciones del dfa:")
    file_path_cadenas = input("Inserte la ruta del archivo .json para el reconocimiento de cadenas:")
    """with open(file_path_dfa) as f:
    # Carga el contenido del archivo y crea un diccionario
        data = json.load(f)
    # Crea una instancia de la clase DFA usando el diccionario"""
    dfa = load_strings_from_json(file_path_dfa)
    dfac = DFA(dfa["fStates"], dfa["transitions"], dfa["allStates"])
    stringsj = load_strings_from_json(file_path_cadenas)
    ##acceder a los datos de stringsj
    strings = stringsj["strings"]
    check_string(strings, dfac)
    ask = str(input("Probar las primeras N cadenas? y/n:"))
    if ask == "y":
        #maxLength = int(input("Inserte la longitud maxima de la cadena:"))
        alphSize = int(input("Inserte el tamaño del alfabeto:"))
        stringNum = int(input("Inserte la cantidad de cadenas a generar:"))
        alpString = generar_alfabeto(alphSize)
        testStrings = generate_strings(alpString, stringNum)
        check_string(testStrings, dfac)
    


