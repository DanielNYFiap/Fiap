cartao = ["4136090882175821","4647826500344048","4049849665383753","4079585425023320","4598977118107720","4506252231125228","4582873825660770","5574295985666263","5372078633380360","5574232623313271","5372071133422154","5574297428301656","5372076513336551","5372071147875645","5574841186727303","6011543310963981","347161677729222","4929753161780717","5355025056279596","5593520325352903","6011668950858306","373045667283844","4539135411248210","4716924139454027","5243160589185253","553753323461","341292820842434","4024007148300030","4532831030709650","6011951337390098","6011021941522252","5221754225548076","4539561031861381","4556591399352978","4916466982738203","4929142790716724","4485986193442676","5244767825143877","5269285430570855","5206684781757119","5306630542914746","5511839564624569","6011672895262194","6011695198277841","6011075815282351","6011849708032267"]


while True :
    ucard = input("Digite o numero do cartao que deseja verificar: ")

    for x in cartao:
        if x == ucard:
            print("SEU CARTAO FOI VAZADO ")
            continuar1 = input("Digite S para fazer outra verificação ou N para encerrar: ").upper()
            if continuar1 == "N":
                print("ENCERRADO")
                exit()
            elif continuar1 == "S":
                continuar1=continuar1      
            else:
                while continuar1 != "S" and "N":
                    continuar1 = input("Digite S ou N apenas: ").upper()
                if continuar1 == "N":
                    print("ENCERRADO")
                    exit()
                elif continuar1 == "S":
                    continuar1=continuar1  
    for x in cartao:                
        if x != ucard:            
            print("nao foi encontrado vazamneto deste numero de cartao")
            continuar2 = input("Digite S para fazer outra verificação ou N para encerrar: ").upper()
            if continuar2 == "N":
                print("ENCERRADO")
                exit()
            elif continuar2 == "S":
                continuar2=continuar2      
            else:
                while continuar2 != "S" and "N":
                    continuar2 = input("Digite S ou N apenas: ").upper()
                if continuar2 == "N":
                    print("ENCERRADO")
                    exit()
                elif continuar2 == "S":
                   continuar2=continuar2                        











