import random

class AlgoritmoGenetico:

    def __init__(self, dados, tamPopulacao = 10, limGeracoes = 50, probMutacao=5, funcaoFitness = None, maiorFitness = True):
        #Atributos
        self.dados = dados
        self.tamPopulacao = tamPopulacao
        self.limGeracoes = limGeracoes
        self.funcaoFitness = funcaoFitness
        self.maiorFitness = maiorFitness
        self.probMutacao = probMutacao
        self.populacao = []
        self.geracao = 1
        
        #Funções que podem ser alteradas
        self.funMutacao = self.mutacao
        self.funSelecao = self.selecao
        self.funCrossover = self.crossover
        self.funCriaIndividuo = self.criaIndividuo
        

    def executa(self):
        """ Executa o código """
        self.criaPopulacaoInicial()

        #Criando nova geração
        while (self.geracao < self.limGeracoes):
            #Inicia uma nova população vazia
            novaPopulacao = []
            for _ in range(int(self.tamPopulacao/2)):
                pai1 = self.funSelecao(self.populacao)
                pai2 = self.funSelecao(self.populacao)

                #Crossover e genes dos filhos
                genes1, genes2 = self.funCrossover(pai1['genes'], pai2['genes'])

                #Realiza mutação
                probMut1 = random.randint(0, 100)
                if (probMut1 <= self.probMutacao): genes1 = self.funMutacao(genes1)
                
                probMut2 = random.randint(0, 100)
                if (probMut2 <= self.probMutacao): genes2 = self.funMutacao(genes2)

                #Adiciona filho 1 e 2
                novaPopulacao.append({'genes': genes1, 'fitness': self.funcaoFitness(genes1, self.dados)})
                novaPopulacao.append({'genes': genes2, 'fitness': self.funcaoFitness(genes2, self.dados) })
            
            #Junta e Elimina os mais fracos
            self.populacao += novaPopulacao
            self.populacao.sort(key=lambda c:c['fitness'], reverse=self.maiorFitness)
            self.populacao = self.populacao[:self.tamPopulacao]
            self.geracao += 1 #Incrementa geração

    def criaPopulacaoInicial(self):
        """ Cria a primeira população """
        for _ in range(self.tamPopulacao):
            cromossomo = {'fitness': 0, 'genes': self.funCriaIndividuo(self.dados)}
            cromossomo['fitness'] = self.funcaoFitness(cromossomo['genes'], self.dados)
            self.populacao.append(cromossomo)
            

    def criaIndividuo(self, dados):
        """ Cria um novo individuo """
        gene = []
        for _ in range(len(dados)):
            gene.append(random.randint(0,1))
        return gene

    def crossover(self, pai1, pai2):
        """ Cruza os genes dos pais gerando 2 filhos """
        posicaoCorte = random.randint(0, len(pai1)-1)
        #Corta os genes dos pais
        pai1_1 = pai1[:posicaoCorte] #Do inicio a posição de corte
        pai1_2 = pai1[posicaoCorte:] #Da posição de corte ao fim

        pai2_1 = pai2[:posicaoCorte] #Do inicio a posição de corte
        pai2_2 = pai2[posicaoCorte:] #Da posição de corte ao fim
        
        #Recombina
        filho1 = pai1_1 + pai2_2
        filho2 = pai2_1 + pai1_2
        
        return filho1, filho2

    def selecao(self, populacao):
        """ Realiza a escolha de um elemento para cruzar """
        indiceSorteado = random.randint(0, len(populacao)-1)
        return populacao[indiceSorteado]

    def mutacao(self, genes):
        """ Realiza a mutação de um item """
        indiceSorteado = random.randint(0, len(genes)-1)
        genes[indiceSorteado] = 1 if genes[indiceSorteado] == 0 else 0  
        return genes

    def melhorResultado(self):
        """ Retorna o melhor resultado """
        return self.populacao[0]