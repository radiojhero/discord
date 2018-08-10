import discord
from discord.ext.commands import Bot
from discord.ext import commands
import requests
import xml.etree.cElementTree as et
import xml.dom.minidom
from xml.dom.minidom import Node

Client = discord.Client()
bot_prefix="~"
client=commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Ruu... Ruu... Ruu...")
    print("Ruukoto serve {}".format(client.user.name))
    print("ID {}".format(client.user.id))

@client.command(pass_context=True)
async def programa(ctx):
    URL = "http://radiojhero.com/player.xml"
    response = requests.get(URL)
    with open('programa.xml', 'wb') as file:
        file.write(response.content)
        
    URL2 = "http://stm1.mastercast.com.br:8008/currentsong?sid=1"
    response = requests.get(URL2)
    with open('atual.xml', 'wb') as file:
        file.write(response.content)
        
    fd = open('programa.xml', 'r+', encoding='iso-8859-1')
    linhas=fd.readlines()
    programa=linhas[8]
    programa2=programa.replace("<nome_programa>", "")
    programa3=programa2.replace("</nome_programa>", "")
    locutor=linhas[9]
    locutor2=locutor.replace("<locutor>", "")
    locutor3=locutor2.replace("</locutor>", "")

    ff=open('atual.xml')
    linha2=ff.readlines()
    musica=linha2[0]
    
    await client.say('Está tocando o programa{}No ar está o{}Tocando a música {} '.format(programa3,locutor3, musica))
    #doc = xml.dom.minidom.parse("programa.xml")
    #for node in doc.getElementsByTagName("locucao"):
    #    nome_programa=node.getAttribute("nome_programa")
    #    locutor=node.getAttribute("locutor")
    #    await client.say('Está tocando o programa {} '.format(nome_programa[0]))

    #programa=locucao.nome_programa
    #locutor=locucao.locutor
    #musatual=stream.SONGTITLE
    #musprox=stream.NEXTTITLE

    #await client.send_message(message.channel, 'Está tocando o programa {} com o {}'.format(programa,locutor))
    #await client.send_message(message.channel, 'Está tocando a música:  {}'.format(musatual))
    #if(str!=None):
    #    await client.send_message(message.channel, 'Em seguida teremos: {}'.format(musprox))
    #await client.say("".format(l,locucao['locutor']))
    #await client.say("Está tocando a música:  {}".format(stream['SONGTITLE']))
    #if(stream['NEXTTITLE']!=None):
    #    await client.say('Em seguida teremos: {}'.format(stream['NEXTTITLE']))


@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong")

@client.command(pass_context=True)
async def pedido(ctx):
    await client.say("Para fazer seu pedido é muito simples! Vá em http://radiojhero.com, e abaixo da foto do DJ clique em Pedido \n Coloque seu nome, cidade, pedido e uma dedicatória bem bacana e clique em enviar pedido \n E assim que o DJ puder, ele tocará seu pedido.")

@client.command(pass_context=True)
async def facebook(ctx):
    await client.say("Ei, nós temos uma página no Facebook, sabia? \n Acesse http://facebook.com/radiojhero e se divirta conosco!")

@client.command(pass_context=True)
async def camiseta(ctx):
    await client.say("Como assim você não tem a camiseta oficial da Rádio J-Hero? \n Acesse http://radiojhero.com/nossa-camiseta e compre a sua! \n Nos apoie e mostre que você é um otaku!")

@client.command(pass_context=True)
async def dev(ctx):
    await client.say("Ruukoto 0.0.1 alpha \n Desenvolvida em Python por @Koakuma#7025 \n edward@radiojhero.com \n Bitcoin: 39V8GHESEuHdvNyT5NAApf7VymuUF6gmtN* \n \n _ps: os comandos iniciados por . são constantes da bot Nadeko_ \n _https://github.com/Kwoth/NadekoBot_")

@client.command(pass_context=True)
async def twitter(ctx):
    await client.say("Ei, também estamos no Twitter! \n http://twitter.com/radiojhero \n Tente, comente e Twitte com a gente!")

@client.command(pass_context=True)
async def parceiros(ctx):
    await client.say("Conheça nossos parceiros: http://radiojhero.com/parceiros \n Tem um site, blog, pagina do facebook, canal do youtube e quer fechar parceria? \n Então acesse http://radiojhero.com/parceria e converse conosco!")

@client.command(pass_context=True)
async def team(ctx):
    await client.say("Conheça a nossa equipe: http://radiojhero.com/equipe \n Essa é a equipe que trabalha dia e noite pra lhe trazer o melhor da cultura oriental, 24 horas por dia, 7 dias por semana (ou quase isso ^^>)")
    
@client.command(pass_context=True)
async def recrutamento(ctx):
    await client.say("Quer produzir programas com uma temática oriental do seu jeito? \n Não quer vir ao microfone, mas ama escrever e quer desenvolver suas ideias em matérias do seu gosto? \n Curte interagir com os ouvintes no facebook, twitter, instagram, amino ou qualquer rede que seja? Topa fazer algo mais bem trabalhado, produzindo vídeos ou colaborando com a J-Hero em eventos? \n Então venha participar da nossa seleção de DJs, Redatores e Colaboradores \n Acesse http://radiojhero.com/trabalhe-conosco e venha fazer parte da família J-Hero!")
   
@client.command(pass_context=True)
async def replay(ctx):
    await client.say("Perdeu o programa do seu DJ favorito? \n Não se desespere, venha para o Replay Maniac J-Hero \n Todas as Seguntas, Terças, Quintas e Sextas das 8 da manhã ao meio dia \nE nos finais de semana das 2 da madrugada às 8 da manhã")


@client.command(pass_context=True)
async def facegrupo(ctx):
    await client.say("Nós também temos um grupo no Facebook! \n https://www.facebook.com/groups/radiojhero \n Vem e participa, porque isso é uma ordem! (pelo menos foi o que a Musa disse)")

@client.command(pass_context=True)
async def tchau(ctx):
    await client.say("Autodestruindo em 3... 2... 1...")
    quit()
    

client.run("token")
