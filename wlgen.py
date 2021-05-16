import os
import sys
import time
import string
import argparse
import itertools



def createWordList(chrs, min_length, max_length, output):
    """
    :param `chrs` são os caracteres usados.
    :param `min_length` é o tamanho mínimo que a palavra tem que ter.
    :param `max_length` é o tamanho máximo que a palavra tem que ter.
    :param `output` é o caminho pra saída do arquivo .txt.
    """
    if min_length > max_length:
        print ("[!] ERRO: o parametro `min_length` deve ser menor ou igual ao paramentro `max_length`")
        sys.exit()

    if os.path.exists(os.path.dirname(output)) == False:
        os.makedirs(os.path.dirname(output))

    print ('[+] Criando wordlist em `%s`...' % output)
    print ('[i] Início: %s' % time.strftime('%H:%M:%S'))

    output = open(output, 'w')

    for n in range(min_length, max_length + 1):
        for xs in itertools.product(chrs, repeat=n):
            chars = ''.join(xs)
            output.write("%s\n" % chars)
            sys.stdout.write('\r[+] Salvando caracteres.. `%s`' % chars)
            sys.stdout.flush()
    output.close()

    print ('\n[i] Término: %s' % time.strftime('%H:%M:%S'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Estagiário de Elite - Gerador de wordlist')
    parser.add_argument(
        '-chr', '--chars',
        default=None, help='são os caracteres usados')
    parser.add_argument(
        '-min', '--min_length', type=int,
        default=1, help='é o tamanho mínimo que a palavra tem que ter')
    parser.add_argument(
        '-max', '--max_length', type=int,
        default=2, help='é o tamanho máximo que a palavra tem que ter')
    parser.add_argument(
        '-out', '--output',
        default='output/wordlist.txt', help='é o caminho pra saída do arquivo .txt')

    args = parser.parse_args()
    if args.chars is None:
        args.chars = string.printable.replace(' \t\n\r\x0b\x0c', '')
        print('\nWLGEN - Gerador de Wordlist\n')
        print('===========================================================================================\nARGUMENTOS VÁLIDOS\nwlgen.py [-h] [-chr CHARS] [-min MIN_LENGTH] [-max MAX_LENGTH] [-out OUTPUT]')
        print('===========================================================================================\nEXEMPLO DE USO:\n---python wlgen.py -chr=abc -min=1 -max=4 -out=output/wordlist.txt \nou\n---python3 wlgen.py --chars=abc --min_length=1 --max_length=4 --output=output/wordlist.txt\n===========================================================================================')
    createWordList(args.chars, args.min_length, args.max_length, args.output)
        

 