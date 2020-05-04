<p align="center">
  <img src="https://i.ibb.co/862ppDm/Sem-t-tulo.png" alt="arte" border="0">
<p>
  
> _“Uma imagem vale mais que mil palavras”_ </br>
> – Confúcio

<br>

## Descrição

Este é um simples script que modifica o papel de parede do smartphone através do aplicativo Termux.

## Instruções 
### Começando

1. Instale os aplicativos [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=pt_BR) e o [Termux API](https://play.google.com/store/apps/details?id=com.termux.api&hl=pt_BR).
2. Abra o aplicativo do Termux e atualize os pacotes e fontes com o comando:
```
pkg update && pkg upgrade
```
3. Instale as depedências necessárias para o aplicativo funcionar:
```
pkg install python termux-api
```
4. Para finalizar, dê permissão de acesso ao armazenamento para o Termux nas configuraçẽos do seu smartphone.

### Uso

Utilize o Python para executar o script:
```
python main.py
```
Na primeira vez em que o script for iniciado seŕá solicitado o caminho de uma pasta, infome a pasta onde estão localizados seus papéis de parede. 
Caso queira alterar a pasta escolhida posteriomente utilize a flag _-c_ ou _--change-dir_:

```
python main.py --change-dir
```


