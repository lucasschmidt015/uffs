def prod():
    carrinho_de_compras=[]
    mercearia = ['[1]-feijão 1kg',7.99, '[2]-arroz 5kg', 19.99, '[3]-sal 1kg', 3.99,'[4]-açucar 5kg', 10.99,'[5]-farinha 5kg',14.99 ,'[6]-fermento 200g', 4.99]
    eletronico = ['Fone de ouvido', 79.99, 'mouse', 99.99,'teclado', 139.99, 'carregador', 29.99, 'webcam', 99.99]
    bebidas = ['cerveja 350ml', 2.49, 'agua de coco 1l', 5.99, 'Refrigerante 2l', 7.99, 'Suco 1l', 4.99]
    segmento = int(input('Segmetno:\n[1] mercearia\n[2] Bebidas\n[3] Eletronicos\nOpcao: '))
    while segmento > 3 or segmento < 1:
        print()
        print("OPÇÃO INVALIDA")
        print()
        segmento = int(input('Segmetno:\n[1] mercearia\n[2] Bebidas\n[3] Eletronicos\nOpcao: '))
    if segmento == 1:
        for i in mercearia:
            print(i)
        contiuar="n"
        while True:
            qual=int(input("Qual produto vc deseja adicionar ao carrinho ?" ))
            print("certo, produto adicionado com sucesso!")
            for g in range(len(mercearia)):
                print(g)
                
ifa=prod()
print(ifa)