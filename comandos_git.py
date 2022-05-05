'''
             ###   Termos e Comandos básicos do Git   ###

git config --global user.name "Kurt Cobain" - alterar usuário
git config --global user.e-mail "exemplo@gmail.com" - alterar e-mail
git config --global core.editor "pycharm" - alterar editor
git config user.name - mostra usuário cadastrado
git config user.e-mail - mostra e-mail cadastrado
git config core.editor - mostra editor de texto cadastrado
git config --list - mostra tudo que está cadastrado
cd - navega nas pastas do sistema. ex.: cd Users/Raul
obs. se iniciar a digitar nome da pasta e apertar tab a palavra autocompleta
ls - lista arquivos dentro da pasta
dir - monta árvore de arquivos da pasta
cd .. - volta um diretório
C:/Users/minhapasta/.git/ - caminho minha pasta github
git init - inicializa repositório no github
branch - versões diferentes do sistema; master - versão principal do sistema;
commit - Alterações de sistema (criar, deletar, modificar) - acompanhado de comentário com explicação;
git status - indica arquivos que foram alterados
git add -A - Adiciona para o empacotamento todos os arquivos alterados
git add README.md - Adiciona um por um
git commit -m "Commit de introdução ao repositório curso em vídeo" - comando para commits seguido de explicação do commit entre ""
git log - lista os commits realizados
git branch - lista todos os branchs do projeto, * demonstra a branch que está no momento.
commit -am "modificação do README"
git reset -- retorna a commit anterior inserindo codigo de identificação do commit (4c26d9d5d2e13e2639c574ef1c95b60eb23a274d)
git reset --soft - volta a commit anterior com alterações preparadas (sem commit)
git reset --mixed - faz o mesmo mas alterações ainda não estão preparadas
git reset --hard -Ignora tudo feito anteriormente
git branch teste - cria nova branch
git checkout teste - muda para branch criada
git dif - mostra quais foram as alterações realizadas
git diff --name-only - Mostra nome dos arquivos que foram modificados.
git diff README.md - Mostra tudo que foi alterado no arquivo especificado
git checkout HEAD -- style.css - Apaga as alterações realizadas apenas do arquivo atual preservando as alterações anteriores.
git remote -v - Mostra opções de envio remoto
fetch - leva arquivos do repositório remoto para local
push - leva arquivos do repositório local para o remoto
git push -u origin master - envia p repositório remoto (master é a especificação da branch)
'''








