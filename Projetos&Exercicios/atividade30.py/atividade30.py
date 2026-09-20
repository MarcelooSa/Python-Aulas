# Peça ao usuário que digite uma linguagem de programação (Python, Java ou C#). Exiba uma breve descrição sobre o uso dessa linguagem, como “Python é muito usado em IA e análise de dados.”

linguagem = str(input("Digite 'P' para Python, 'J' para Java e 'C' para C#: "))
python = "Python é uma linguagem de programação de alto nível, interpretada e de código aberto, conhecida pela sua sintaxe simples e fácil leitura, o que a torna ideal para iniciantes."
java = "Java é uma linguagem de programação e plataforma utilizada para desenvolver uma vasta gama de aplicações, incluindo softwares empresariais, aplicativos Android, sistemas web e aplicações desktop."
c = "C# é uma linguagem de programação orientada a objetos, moderna e versátil, criada pela Microsoft para a plataforma .NET, utilizada para desenvolver uma ampla gama de aplicações como jogos, aplicações web, desktop e mobile, além de soluções na nuvem e IoT."
if (linguagem == "P"):
    print(python)
elif (linguagem == "J"):
    print(java)
elif (linguagem == "C"):
    print(c)
else: 
    print("Digite uma opção válida.")