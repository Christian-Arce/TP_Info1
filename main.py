import json
import itertools

# Definición de la clase DFA 
class DFA:
    def __init__(self, final_states, transitions, all_states):
        self.final_states = final_states  # Estados finales del DFA
        self.transitions = transitions  # Transiciones del DFA
        self.all_states = all_states  # Todos los estados del DFA

    # Método para determinar si el DFA reconoce una cadena dada
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

# Función para generar todas las posibles cadenas de un alfabeto dado hasta una longitud dada
def generate_strings(alphabet, x):
    strings = []  # Inicializa la lista de cadenas vacía
    length = 1  # Inicializa la longitud de la cadena en 1
    while len(strings) < x:  # Mientras no se hayan generado suficientes cadenas
        for string_tuple in itertools.product(alphabet, repeat=length):
            if len(strings) >= x:  # Si ya se han generado suficientes cadenas, termina el bucle
                break
            strings.append(''.join(string_tuple))  # Convierte la tupla a una cadena y añádela a la lista
        length += 1  # Incrementa la longitud para la próxima iteración
    return strings

# Función para cargar cadenas desde un archivo JSON
def load_strings_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Función para verificar si un DFA dado reconoce o no una lista de cadenas
def check_string(strings, dfa):
    for i, string in enumerate(strings):
        if dfa.recognizes(string):
            print(f"El DFA reconoce la cadena número {i+1}: {string}")
        else:
            print(f"El DFA no reconoce la cadena número {i+1}: {string}")

# Función para generar un alfabeto de un tamaño dado
def generar_alfabeto(n):
    return [chr(i) for i in range(65, 65+n)]

# Función para permitir al usuario probar las primeras N cadenas generadas
def run_strings(ask):
    if ask == "y":
        alphSize = int(input("Inserte el tamaño del alfabeto:"))
        stringNum = int(input("Inserte la cantidad de cadenas a generar:"))
        alpString = generar_alfabeto(alphSize)
        testStrings = generate_strings(alpString, stringNum)
        check_string(testStrings, dfac)

# Punto de entrada del programa
if __name__ == "__main__":
    while 1:
        file_path_dfa = input("Inserte la ruta del archivo .json con las transiciones del dfa:")
        file_path_cadenas = input("Inserte la ruta del archivo .json para el reconocimiento de cadenas:")
        dfa = load_strings_from_json(file_path_dfa)
        dfac = DFA(dfa["fStates"], dfa["transitions"], dfa["allStates"])
        stringsj = load_strings_from_json(file_path_cadenas)
        strings = stringsj["strings"]
        check_string(strings, dfac)
        ask = str(input("Quiere probar las primeras N cadenas? y/n:"))
        run_strings(ask)
        ask2 = str(input("Quiere salir? y/n:"))
        if ask2 == "y":
            break

    


