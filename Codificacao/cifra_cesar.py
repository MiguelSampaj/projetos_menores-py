def main(text, key=1, dir=True):
    """
    Função que automatiza a criptografia usando a cifra de césar
    :param text: Texto str que será codificado
    :param key: Chave int da criptografia. Naturalmente definido como 1.
    :param dir: Parametro bool que define se a chave será aplicada da direita para esquerda ou visse versa.
    True significa da esquerda para direita e False o oposto. Naturalmente, o parametro é True.
    :return:
    """
    letras = 'abcdefghijklmnopqrstuvwxyz'
    texto_codificado = ''

    if not dir:
        key *= -1

    for letra in text.lower():
        if letra != ' ':
            letra_codificada = ''
            letra_corrigida = letra

            match letra:
                case letra if letra == 'ç':
                    letra_corrigida = 'c'
                case letra if letra in 'áàãâ':
                    letra_corrigida = 'a'
                case letra if letra in 'éèê':
                    letra_corrigida = 'e'
                case letra if letra in 'íìî':
                    letra_corrigida = 'i'
                case letra if letra in 'óòõô':
                    letra_corrigida = 'o'
                case letra if letra in 'úùû':
                    letra_corrigida = 'u'

            try:
                try:
                    letra_codificada = letras[letras.index(letra_corrigida) + key]
                except ValueError:
                    letra_codificada = letra_corrigida
            except IndexError:
                diferenca_indexs = key - (len(letras) - letras.index(letra_corrigida))
                letra_codificada = letras[diferenca_indexs]

            texto_codificado += f'{letra_codificada} '
        else:
            texto_codificado += '| '

    for letra in text:
        maiusculo = False

        if letra.upper() == letra:
            maiusculo = True
        else:
            maiusculo = False

        if maiusculo:
            texto_cod_temp = ''

            for caracter in texto_codificado:
                if caracter == ' ':
                    pass
                elif caracter == '|':
                    texto_cod_temp += ' '
                else:
                    texto_cod_temp += caracter

            texto_cod_temp = texto_cod_temp.capitalize()

    return texto_cod_temp.strip()

print(main('Bom dia! Eu gosto de maçã.', 1, False))
