# -*- coding: utf-8 -*-
import pdftotext

import PyPDF2


class ManipulandoPDF:

    def novoPDF(self, arquivo_pdf):
        try:
            pdf_1 = open(arquivo_pdf, 'rb')
            ler_pdf = PyPDF2.PdfFileReader(pdf_1)
            qntidade_paginas = ler_pdf.numPages
            escrever = PyPDF2.PdfFileWriter()
            for ind in range(qntidade_paginas):
                print("[ x ] ", (qntidade_paginas - ind))
                conteudoAdd = ler_pdf.getPage(ind)
            print("[ > ] Novo Arquivo >> ", arquivo_pdf)

            pdf_1.close()
        except FileNotFoundError as diretorio_arquivo:
            print(diretorio_arquivo, "Arquivo nao encontrado")

        def todosPDF(**pdfs):
            for i, w in sorted(pdfs.items()):
                try:
                    todos_pdfs = w
                    pdf = open(todos_pdfs, 'rb')

                    ler_todos_pdf = PyPDF2.PdfFileReader(todos_pdfs)
                    qntidade_por_paginas = ler_todos_pdf.numPages
                    for indx in range(qntidade_por_paginas):
                        print("[ x ] ", i, " - ", (qntidade_por_paginas - indx))
                        todos_conteudo = ler_todos_pdf.getPage(indx)

                        todos_conteudo.extractText()
                        escrever.addPage(todos_conteudo)

                    pdf.close()
                except FileNotFoundError as diretorio_arquivo:
                    print(diretorio_arquivo, "Arquivo nao encontrado")

                def juntando_todos_pdf():
                    juntado_pdf = open('/home/jfc-me/Desktop/novo.pdf', 'wb')
                    escrever.write(juntado_pdf)
                    juntado_pdf.close()

                juntando_todos_pdf()

        pdfs = {

            '1': '/home/jfc-me/Desktop/part1.pdf',
            '2': '/home/jfc-me/Desktop/part2.pdf',
            '3': '/home/jfc-me/Desktop/part3.pdf',
            '4': '/home/jfc-me/Desktop/part4.pdf',
            '5': '/home/jfc-me/Desktop/part5.pdf',
            '6': '/home/jfc-me/Desktop/part6.pdf',
            '7': '/home/jfc-me/Desktop/part7.pdf',
            '8': '/home/jfc-me/Desktop/part8.pdf',
            '9': '/home/jfc-me/Desktop/part9.pdf',
            '10': '/home/jfc-me/Desktop/part10.pdf',
            '11': '/home/jfc-me/Desktop/part11.pdf',
            '12': '/home/jfc-me/Desktop/part12.pdf',
            '13': '/home/jfc-me/Desktop/part13.pdf',
            '14': '/home/jfc-me/Desktop/part14.pdf',
            '15': '/home/jfc-me/Desktop/part15.pdf',
            '16': '/home/jfc-me/Desktop/part16.pdf',
            '17': '/home/jfc-me/Desktop/part17.pdf',
            '18': '/home/jfc-me/Desktop/part18.pdf',
            '19': '/home/jfc-me/Desktop/part19.pdf',
            '20': '/home/jfc-me/Desktop/part20.pdf',
            '21': '/home/jfc-me/Desktop/part21.pdf',
            '22': '/home/jfc-me/Desktop/part22.pdf',
            '23': '/home/jfc-me/Desktop/part23.pdf',
            '24': '/home/jfc-me/Desktop/part24.pdf',
        }
        todosPDF(**pdfs)


ManipulandoPDF().novoPDF('/home/jfc-me/Desktop/novo.pdf')
