import stateNum
import math
import finalStates
import numpy
import convert
import dict
import dfaMermaid
import os
import json
import itertools
def load_strings_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['strings']

import json
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
            print("la transicion es: ", transition)
            if transition is None:
            # Si no hay transición, la cadena no es reconocida
                return False
            else:
            # Si hay una transición, pasa al siguiente estado
                current_state = transition[2]
                print("current", current_state)
    # Si el estado final está en la lista de estados finales, la cadena es reconocida
        return current_state in self.final_states

def generateDfa(dfaNumber, alphabetSize):
    diccionario = dict.get_unicode_letters(alphabetSize)
    #print(f"Generating the dfa number {dfaNumber} with Sigma Size of {alphabetSize}")
    startingValues = stateNum.determine_number_of_states(dfaNumber,alphabetSize)
    Qlen = startingValues[0]
    # print(rangeQlen1)
    topInd = 0
    botInd = None
    Flen = None
    dfaNumber -= startingValues[2]
    for i in (range(Qlen+1)):
        topInd += math.comb(Qlen,i)*(Qlen+1)**(alphabetSize*Qlen)
        # print(topInd)
        if topInd >= dfaNumber:
            botInd = topInd - math.comb(Qlen,i)*(Qlen+1)**(alphabetSize*Qlen)
            #print(f"{dfaNumber} in between {botInd} and {topInd}")
            #print(f"Therefore the dfa has {i} final states")
            Flen = i
            break
    dfaNumber -= botInd
    topInd = 0
    botInd = 0
    rangeLen = stateNum.determine_amount_of_dfas_without_final(Qlen,alphabetSize)
    fStateIndex = None
    for i in range(math.comb(Qlen,Flen)):
        topInd += rangeLen
        if topInd >= dfaNumber:
            botInd = topInd - rangeLen
            #print(f"{dfaNumber} in between {botInd} and {topInd}")
            #print(f"Therefore the final state index is {i}")
            fStateIndex = i
            break #XD
    dfaNumber -= botInd + 1
    fStates = finalStates.estados_finales_tamano_n(Qlen,Flen)[fStateIndex]
    allStates = finalStates.estados_finales_tamano_n(Qlen,Qlen)[-1]
    #print(f"The states of the DFA are {allStates}")
    #print(f"The final states are {fStates}")
    # dfaNumber = numpy.base_repr(dfaNumber,Qlen+1)
    # print(dfaNumber)
    dfaNumber = convert.int_to_base(dfaNumber,Qlen+1)
    dfaNumber = dfaNumber.zfill(Qlen*alphabetSize)
    # print(dfaNumber)
    count = 0
    transitions = []
    for i in range(Qlen):
        for j in range(alphabetSize):
            if dfaNumber[count%len(dfaNumber)] != '0':
                transitions.append([f"q{i}",diccionario[j],f"q{int(dfaNumber[count%len(dfaNumber)],base=Qlen+1)-1}"])
            count += 1
    print(fStates, transitions, allStates)
    return DFA(fStates, transitions, allStates)


def load_strings_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['strings']

def generate_and_check_dfas(alphabet_size, strings):
    for i in range(1, 1000000):  # Genera los primeros 1000 DFAs
        dfa = generateDfa(i, alphabet_size)
        for string in strings:
            if dfa.recognizes(string):
                print(f"El DFA número {i} reconoce la cadena: {string}")
            #else:
            
            #    print(f"El DFA número {i} no reconoce la cadena: {string}")
def check_string(strings, numDfa, alphabet_size):
    dfa = generateDfa(numDfa, alphabet_size)
    for string in strings:
        if dfa.recognizes(string):
            print(f"El DFA número {numDfa} reconoce la cadena: {string}")
        else:
            print(f"El DFA número {numDfa} no reconoce la cadena: {string}")

def generate_strings(alphabet, max_length):
    # Inicializa la lista de cadenas vacía
    strings = []
    
    # Para cada longitud de 1 hasta max_length
    for length in range(1, max_length + 1):
        # Genera todas las cadenas de esa longitud
        for string_tuple in itertools.product(alphabet, repeat=length):
            # Convierte la tupla a una cadena y añádela a la lista
            strings.append(''.join(string_tuple))
    return strings

def generar_alfabeto(n):
    return [chr(i) for i in range(65, 65+n)]

if __name__ == "__main__":
    alphSize = int(input("Inserte el tamaño del alfabeto:"))
    numberDfa = int(input("Inserte el número del DFA:"))
    file_path = input("Inserte la ruta del archivo .json:")
    strings = load_strings_from_json(file_path)
    check_string(strings, numberDfa, alphSize)
    ask = str(input("Probar los primeras N cadenas? y/n:"))
    if ask == "y":
        maxLength = int(input("Inserte la longitud maxima de la cadena:"))
        alpString = generar_alfabeto(alphSize)
        testStrings = generate_strings(alpString, maxLength)
        check_string(testStrings, numberDfa, alphSize)
    
    #check_test("AAA")
    #check_test("C")
    #generate_and_check_dfas(alphSize, strings)


