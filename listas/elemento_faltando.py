""" 
Dado diversos vetores como string, retorne qual valor está ausente para completar a sequência númerica interna.

exemplo: 
[4,2,3,1,6] // primeiro vetor -> valor esperado 5
[10,12,14,11,15] // segundo vetor -> valor esperadoo 13
[12032,12030,12031,12034,12036,12035] // terceiro vetor -> valor esperado 12033
"""
import re


def verifica(lista):
    vetor  = re.findall(r'\d+', lista)
    # print(vetor)
    vetor = [int(i) for i in vetor]
    out = [n for n in range(min(vetor), max(vetor)+1) if n not in vetor]
    return out[0]
    


assert verifica('[4,2,3,1,6]') == 5
assert verifica('[10,12,14,11,15]') == 13
assert verifica('[12032,12030,12031,12034,12036,12035]') == 12033