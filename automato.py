from typing import List, Dict, Set



class Automato:
    SIMBOLOS_EPSILON = {''}

    def __init__(self, automato: Dict):
        self.alfabeto = automato['Sigma']
        self.estado_inicial = automato['q0']
        self.estados_finais = automato['F']
        self.transicoes = automato['delta']
        self.tipo_automato = self.classificar_automato()

    def _tem_transicao_epsilon(self) -> bool:
        for estado, trans in self.transicoes.items():
            for situacao in trans:
                if situacao in self.SIMBOLOS_EPSILON:
                    return True
        return False

    def classificar_automato(self) -> str:
        if self._tem_transicao_epsilon():
            return 'AFN'

        for estado, trans in self.transicoes.items():
            for situacao, destinos in trans.items():
                if len(destinos) !=1:
                    return 'AFN'
        return 'AFD'


    def processar_palavra(self, palavra: str) -> bool:
        if(self.tipo_automato == 'AFD'):
            return self.__processar_afd(palavra)
        else:
            return self.__processar_afn(palavra)

    def __processar_afd(self,palavra)-> bool:
        estado_atual  = self.estado_inicial
        print(f"[*] Testando a palavra no AFD {palavra}")
        print('[*] o estado inicial é: ', estado_atual)
        for caractere in palavra:
            if caractere not in self.alfabeto:
                return False

            transicoes_estado = self.transicoes.get(estado_atual, {})

            if caractere not in transicoes_estado:
                return False
            estado_atual = transicoes_estado[caractere][0]
            print(f"[*] Leu {caractere} e foi pro estado: {estado_atual}")
        print('[*] teste finalizado')
        resultado_teste= True if estado_atual in self.estados_finais else False
        return resultado_teste

    def _fecho_epsilon(self, estados: Set[str]) -> Set[str]:
        fecho: Set[str] = set(estados)
        pilha = list(estados)

        while pilha:
            estado = pilha.pop()
            transicoes_estado = self.transicoes.get(estado, {})
            for simbolo in self.SIMBOLOS_EPSILON:
                for destino in transicoes_estado.get(simbolo, []):
                    if destino not in fecho:
                        fecho.add(destino)
                        pilha.append(destino)

        return fecho

    def __processar_afn(self, palavra: str) -> bool:
        estados_atuais: Set[str] = self._fecho_epsilon({self.estado_inicial})

        print(f"[*] Testando a palavra no AFN: '{palavra}'")
        print(f"[*] Os estados iniciais (com fecho-épsilon) são: {estados_atuais}")

        for caractere in palavra:
            if caractere not in self.alfabeto:
                print(f"[-] Caractere '{caractere}' não pertence ao alfabeto. Palavra rejeitada.")
                return False

            proximos_estados: Set[str] = set()

            for estado in estados_atuais:
                transicoes_estado = self.transicoes.get(estado, {})
                if caractere in transicoes_estado:
                    proximos_estados.update(transicoes_estado[caractere])

            estados_atuais = self._fecho_epsilon(proximos_estados)
            print(f"[*] Leu '{caractere}' e ramificou para os estados (com fecho-épsilon): {estados_atuais}")

            if not estados_atuais:
                print("[-] Caminho sem saída encontrado (conjunto de estados vazio). Palavra rejeitada.")
                return False

        print('[*] Teste finalizado')
        resultado_teste = any(estado in self.estados_finais for estado in estados_atuais)

        return resultado_teste

    def rodar_testes(self, palavrasTestes: List[str]):
        print('[*] Testando palavras testes')
        for palavra in palavrasTestes:
            resultado = self.processar_palavra(palavra)
            print(f"[*] {palavra}: {resultado}")
            print('-----------------------------------------------------')
