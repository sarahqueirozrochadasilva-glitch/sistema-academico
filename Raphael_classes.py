# ==========================================================
# PROJETO A3 - SISTEMA ACADÊMICO
# Cadastros, notas, médias e aprovação
# ==========================================================


# ---------- 1. CLASSES ----------
# Atributos com dois underlines (__nome) são privados (encapsulamento).
# Para acessar de fora, usamos os métodos get_...

class Curso:
    def __init__(self, id, nome, semestres):  # construtor
        self.__id = id
        self.__nome = nome
        self.__semestres = semestres

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_semestres(self):
        return self.__semestres

    def exibir(self):
        print(self.__id, "-", self.__nome, "|", self.__semestres, "semestres")


class Professor:
    def __init__(self, id, nome, email):  # construtor
        self.__id = id
        self.__nome = nome
        self.__email = email

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def exibir(self):
        print(self.__id, "-", self.__nome, "|", self.__email)


class Disciplina:
    def __init__(self, id, nome, carga_horaria, curso, professor):  # construtor
        self.__id = id
        self.__nome = nome
        self.__carga_horaria = carga_horaria
        self.__curso = curso            # guarda um objeto Curso
        self.__professor = professor    # guarda um objeto Professor

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_carga_horaria(self):
        return self.__carga_horaria

    def get_curso(self):
        return self.__curso

    def get_professor(self):
        return self.__professor

    def exibir(self):
        print(self.__id, "-", self.__nome, "|", self.__carga_horaria, "h |",
              self.__curso.get_nome(), "| Prof.", self.__professor.get_nome())


class Aluno:
    def __init__(self, matricula, nome, idade, curso):  # construtor
        self.__matricula = matricula
        self.__nome = nome
        self.__idade = idade
        self.__curso = curso            # guarda um objeto Curso

    def get_matricula(self):
        return self.__matricula

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_curso(self):
        return self.__curso

    def exibir(self):
        print(self.__matricula, "-", self.__nome, "|", self.__idade,
              "anos |", self.__curso.get_nome())


MEDIA_MINIMA = 7.0


class Nota:
    def __init__(self, aluno, disciplina, nota1, nota2):  # construtor
        self.__aluno = aluno
        self.__disciplina = disciplina
        self.__nota1 = nota1
        self.__nota2 = nota2

    def get_aluno(self):
        return self.__aluno

    def get_disciplina(self):
        return self.__disciplina

    def get_nota1(self):
        return self.__nota1

    def get_nota2(self):
        return self.__nota2

    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2

    def get_situacao(self):
        if self.calcular_media() >= MEDIA_MINIMA:
            return "Aprovado"
        return "Reprovado"

    def esta_aprovado(self):
        return self.get_situacao() == "Aprovado"

    def exibir(self):
        print(self.__aluno.get_nome(), "|", self.__disciplina.get_nome(),
              "| N1:", self.__nota1, "| N2:", self.__nota2,
              "| Média: %.2f" % self.calcular_media(),
              "|", self.get_situacao())


# ---------- 2. LISTAS QUE GUARDAM OS OBJETOS ----------
cursos = []
disciplinas = []
professores = []
alunos = []
notas = []


# ---------- 3. FUNÇÕES DE APOIO ----------
def ler_texto(mensagem):
    """Pede um texto e só aceita se não estiver vazio."""
    while True:
        texto = input(mensagem).strip()
        if texto != "":
            return texto
        print("Erro: este campo não pode ficar vazio.")


def ler_inteiro(mensagem, minimo, maximo):
    """Pede um número inteiro dentro de um intervalo."""
    while True:
        valor = input(mensagem).strip()
        if valor.isdigit():
            numero = int(valor)
            if numero >= minimo and numero <= maximo:
                return numero
            print("Erro: digite um número entre", minimo, "e", maximo)
        else:
            print("Erro: digite apenas números.")


def ler_nota(mensagem):
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            numero = float(valor)
        except ValueError:
            print("Erro: digite um número (ex.: 7.5).")
            continue
        if numero >= 0 and numero <= 10:
            return numero
        print("Erro: a nota deve ficar entre 0 e 10.")


def escolher_item(lista, titulo):
    """Mostra uma lista numerada de objetos e devolve o escolhido."""
    print("\n" + titulo)
    for i in range(len(lista)):
        print(i + 1, "-", lista[i].get_nome())
    escolha = ler_inteiro("Escolha o número: ", 1, len(lista))
    return lista[escolha - 1]


def nome_ja_existe(lista, nome):
    """Verifica se já existe um objeto com esse nome na lista."""
    for item in lista:
        if item.get_nome().lower() == nome.lower():
            return True
    return False


def buscar_nota(aluno, disciplina):
    for n in notas:
        if (n.get_aluno().get_matricula() == aluno.get_matricula()
                and n.get_disciplina().get_id() == disciplina.get_id()):
            return n
    return None


def notas_do_aluno(aluno):
    resultado = []
    for n in notas:
        if n.get_aluno().get_matricula() == aluno.get_matricula():
            resultado.append(n)
    return resultado


def contar_aprovacoes(aluno):
    total = 0
    for n in notas_do_aluno(aluno):
        if n.esta_aprovado():
            total += 1
    return total


# ---------- 4. CADASTROS (criam os objetos) ----------
def cadastrar_curso():
    print("\n=== CADASTRO DE CURSO ===")
    nome = ler_texto("Nome do curso: ")

    if nome_ja_existe(cursos, nome):
        print("Esse curso já está cadastrado!")
        return

    semestres = ler_inteiro("Duração em semestres (1 a 12): ", 1, 12)

    curso = Curso(len(cursos) + 1, nome, semestres)  # cria o objeto
    cursos.append(curso)
    print("Curso cadastrado com sucesso! Código:", curso.get_id())


def cadastrar_professor():
    print("\n=== CADASTRO DE PROFESSOR ===")
    nome = ler_texto("Nome do professor: ")

    if nome_ja_existe(professores, nome):
        print("Esse professor já está cadastrado!")
        return

    email = ler_texto("E-mail do professor: ")
    while "@" not in email:
        print("E-mail inválido (precisa ter @).")
        email = ler_texto("E-mail do professor: ")

    professor = Professor(len(professores) + 1, nome, email)
    professores.append(professor)
    print("Professor cadastrado com sucesso! Código:", professor.get_id())


def cadastrar_disciplina():
    print("\n=== CADASTRO DE DISCIPLINA ===")

    if len(cursos) == 0:
        print("Cadastre um curso primeiro!")
        return
    if len(professores) == 0:
        print("Cadastre um professor primeiro!")
        return

    nome = ler_texto("Nome da disciplina: ")
    carga = ler_inteiro("Carga horária (20 a 200 horas): ", 20, 200)
    curso = escolher_item(cursos, "Escolha o curso da disciplina:")

    # Não repete disciplina com o mesmo nome no mesmo curso
    for d in disciplinas:
        if d.get_nome().lower() == nome.lower() and d.get_curso() == curso:
            print("Essa disciplina já existe nesse curso!")
            return

    professor = escolher_item(professores, "Escolha o professor responsável:")

    disciplina = Disciplina(len(disciplinas) + 1, nome, carga, curso, professor)
    disciplinas.append(disciplina)
    print("Disciplina cadastrada com sucesso! Código:", disciplina.get_id())


def cadastrar_aluno():
    print("\n=== CADASTRO DE ALUNO ===")

    if len(cursos) == 0:
        print("Cadastre um curso primeiro!")
        return

    nome = ler_texto("Nome do aluno: ")
    idade = ler_inteiro("Idade (14 a 100): ", 14, 100)
    curso = escolher_item(cursos, "Escolha o curso do aluno:")

    matricula = 1000 + len(alunos) + 1  # 1001, 1002, 1003...
    aluno = Aluno(matricula, nome, idade, curso)
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso! Matrícula:", aluno.get_matricula())


# ---------- 5. NOTAS ----------
def registrar_nota():
    print("\n=== REGISTRAR NOTAS ===")

    if len(alunos) == 0:
        print("Cadastre um aluno primeiro!")
        return
    if len(disciplinas) == 0:
        print("Cadastre uma disciplina primeiro!")
        return

    aluno = escolher_item(alunos, "Escolha o aluno:")

    disciplinas_do_curso = []
    for d in disciplinas:
        if d.get_curso().get_id() == aluno.get_curso().get_id():
            disciplinas_do_curso.append(d)

    if len(disciplinas_do_curso) == 0:
        print("Não há disciplinas cadastradas para o curso",
              aluno.get_curso().get_nome())
        return

    disciplina = escolher_item(disciplinas_do_curso, "Escolha a disciplina:")

    if buscar_nota(aluno, disciplina) is not None:
        print("Este aluno já tem nota registrada nessa disciplina!")
        return

    nota1 = ler_nota("Nota 1 (0 a 10): ")
    nota2 = ler_nota("Nota 2 (0 a 10): ")

    registro = Nota(aluno, disciplina, nota1, nota2)
    notas.append(registro)

    print("Notas registradas! Média: %.2f - %s"
          % (registro.calcular_media(), registro.get_situacao()))


def boletim_aluno():
    print("\n=== BOLETIM DO ALUNO ===")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    aluno = escolher_item(alunos, "Escolha o aluno:")
    notas_aluno = notas_do_aluno(aluno)

    print("\nAluno:", aluno.get_nome(), "| Curso:", aluno.get_curso().get_nome())

    if len(notas_aluno) == 0:
        print("Esse aluno ainda não tem notas registradas.")
        return

    soma = 0
    for n in notas_aluno:
        n.exibir()
        soma += n.calcular_media()

    print("\nDisciplinas cursadas:", len(notas_aluno))
    print("Disciplinas aprovadas:", contar_aprovacoes(aluno))
    print("Média geral: %.2f" % (soma / len(notas_aluno)))


# ---------- 6. LISTAGENS ----------
def listar(lista, titulo, mensagem_vazia):
    """Lista qualquer uma das listas chamando o método exibir() de cada objeto."""
    print("\n=== " + titulo + " ===")
    if len(lista) == 0:
        print(mensagem_vazia)
    else:
        for i in range(len(lista)):
            lista[i].exibir()


# ---------- 7. MENU PRINCIPAL ----------
def menu():
    while True:
        print("\n==============================")
        print("   SISTEMA ACADÊMICO - A3")
        print("==============================")
        print("1 - Cadastrar curso")
        print("2 - Cadastrar disciplina")
        print("3 - Cadastrar professor")
        print("4 - Cadastrar aluno")
        print("5 - Listar cursos")
        print("6 - Listar disciplinas")
        print("7 - Listar professores")
        print("8 - Listar alunos")
        print("9 - Registrar notas")
        print("10 - Boletim do aluno")
        print("11 - Listar todas as notas")
        print("0 - Sair")

        opcao = ler_inteiro("Escolha uma opção: ", 0, 11)

        if opcao == 1:
            cadastrar_curso()
        elif opcao == 2:
            cadastrar_disciplina()
        elif opcao == 3:
            cadastrar_professor()
        elif opcao == 4:
            cadastrar_aluno()
        elif opcao == 5:
            listar(cursos, "CURSOS CADASTRADOS", "Nenhum curso cadastrado.")
        elif opcao == 6:
            listar(disciplinas, "DISCIPLINAS CADASTRADAS", "Nenhuma disciplina cadastrada.")
        elif opcao == 7:
            listar(professores, "PROFESSORES CADASTRADOS", "Nenhum professor cadastrado.")
        elif opcao == 8:
            listar(alunos, "ALUNOS CADASTRADOS", "Nenhum aluno cadastrado.")
        elif opcao == 9:
            registrar_nota()
        elif opcao == 10:
            boletim_aluno()
        elif opcao == 11:
            listar(notas, "NOTAS REGISTRADAS", "Nenhuma nota registrada.")
        else:
            print("Encerrando o sistema. Até logo!")
            break


# ---------- 8. INÍCIO DO PROGRAMA ----------
if __name__ == "__main__":
    menu()
