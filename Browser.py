from PilhaEncadeada import Pilha


class BrowserException(Exception):
    pass


class Browser:

    OPTIONS = {
        '1': '#back',
        '2': '#sair',
        '3': '#showhist',
        '4': '#add'
    }
    SITES = {
        '1': 'www.ifpb.edu.br',
        '2': 'www.ifpb.edu.br/tsi',
        '3': 'www.ifpb.edu.br/tsi/professores',
        '4': 'www.ifpb.edu.br/tsi/alunos',
        '5': 'www.google.com.br',
        '6': 'www.examples.com.br',
        '7': 'www.examples.com.br/register',
        '8': 'www.estruturasdedados.com.br',
        '9': 'www.estruturasdedados.com.br/ed'
    }

    def __init__(self):
        self.history = Pilha()
        self.__home = ''
        self.__url = ''
        self.__counter = 0
        self.__status = True

    @property
    def url(self):
        return self.__url

    @property
    def home(self):
        return self.__home

    @property
    def counter(self):
        return self.__counter

    @property
    def status(self):
        return self.__status

    @url.setter
    def url(self, url):
        self.__url = url

    @home.setter
    def home(self, url):
        self.__home = url

    @counter.setter
    def counter(self, valor):
        self.__counter = valor

    @status.setter
    def status(self, valor):
        self.__status = valor

    def browse(self, url: str):  # read url/options and execute them
        if url[0].isalpha():
            self.updateHistory(url, True)
        else:
            url_array = url.split()
            # option = self.OPTIONS.get(url_array[0], False)
            option = url_array[0]
            if option == '#back':
                self.home = self.goBackHistory()
            elif option == '#sair':
                self.shutdown()
            elif option == '#showhist':
                self.showHistoryFromHome()
            elif option == '#add':
                self.addUrl(url_array[1])
            elif option[0] == '/':
                url = self.home + option
                self.updateHistory(url, True)
            else:
                raise BrowserException("Invalid option")

    def addUrl(self, url: str):
        self.SITES[str(len(self.SITES)+1)] = url

    def checkUrl(self, url: str):
        return url in self.SITES.values()

    def updateHistory(self, url: str, add: bool):
        if self.checkUrl(url):
            if self.counter == 0:
                self.home = url
                self.counter += 1
            elif add:
                self.goForwardHistory(self.home)
                self.home = url
        else:
            raise BrowserException("Invalid url")

    def showHistory(self):
        if self.history.estaVazia():
            print('history: []')
        else:
            print(f'history: {self.history}')
            # return history

    def showHistoryFromHome(self):
        if self.history.estaVazia():
            print('history: []')
        else:
            print(f'[{self.home}]->' + self.history.imprimeInverso())
            # print(history)

    def goForwardHistory(self, url):
        self.history.empilha(url)
        self.counter += 1

    def goBackHistory(self):
        self.counter -= 1
        return self.history.desempilha()

    def shutdown(self):
        self.status = False

    def run(self):
        print('\n====================================================================================\n')
        while self.status:
            self.showHistory()
            print(f'home: [{self.home}]')
            url = input('url: ')
            self.browse(url)
            print('\n====================================================================================\n')
