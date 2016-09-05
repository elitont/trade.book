# Tradebook: Site de troca e empréstimo de livros entre a comunidade acadêmica
============

Universidade Federal da Fronteira Sul

Trabalho da disciplina de Planejamento e Gestão de Projetos

Comandos:
	- Compilar (~/plone/zinstance): sudo -u plone_buildout bin/buildout
	- Rodar (~/plone/zinstance): sudo ./bin/plonectl [start | fg]
Plugin:
	- Salve a pasta "trade.book" em ~/plone/zinstance/src
	- Edite o arquivo buildout.cfg em ~/plone/zinstance:
		Acrescente:
			[...]
			 eggs=
			 		...
			 		trade.book
			 [...]
			 develop =
			 		...
			 		src/trade.book
	Compile e rode o Plone.

Importação do banco:
	- Substitua o arquivo blobstorage de ~/plone/zinstance/var/ pelo arquivo do github
	- Salve o arquivo Tradebook.zexp em ~/plone/zinstance/var/instance/import
	- Compile e rode o plone
	- Acesse: http://localhost:8080/manage_main
	- Clique em "import/export" e importe o arquivo Tradebook.zexp 

**Colaboradores:**
Eliton Traverssini
Ivair Puerari
João Carlos Becker
Marco Aurélio Alves Puton
