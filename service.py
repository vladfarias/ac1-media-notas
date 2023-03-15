def check_aprovacao(nota1, nota2):
    if nota1 is None or nota2 is None:
            return 'Informe as notas 😶‍🌫️'
    
    nota1 = float(nota1)
    nota2 = float(nota2)
    med = round((nota1+ nota2)/2, 2)

    return f'Aprovado, média {med} 🍻🎉🥂' if med >= 7.00 else f'Reprovado, média {med}💣💥'