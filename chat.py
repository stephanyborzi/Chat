import flet as ft 
#Criando a página principal
def main(pagina):
    texto = ft.Text("ZapZap")
    texto_novo = ft.Text("O melhor da comunicação digital!")
    nome_usuario = ft.TextField(label = "Escreva seu nome")
    chat = ft.Column()

    def tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
    
    pagina.pubsub.subscribe(tunel)

    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{nome_usuario.value}:{campo_mensagem.value}"
        pagina.pubsub.send_all(texto_campo_mensagem)
        campo_mensagem.value = " "
        pagina.update()
    campo_mensagem = ft.TextField(label = "Escreva sua mensagem", 
                                  on_submit=enviar_mensagem)
    botao_mensagem = ft.ElevatedButton("Enviar", on_click = enviar_mensagem)

    def entrar_chat(evento):
        #fechar o popup
        popup.open = False
        #tirar o botão iniciar
        pagina.remove(botao_iniciar)
        #chat
        pagina.add(chat)
        linha_mensagem  = ft.Row(
            [campo_mensagem,botao_mensagem])
        pagina.add(linha_mensagem)
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all (texto)
        pagina.update()

    popup = ft.AlertDialog(
        open = False, 
        modal = True, 
        title = ft.Text("ZapZap"), 
        content = nome_usuario,
        actions = [ft.ElevatedButton("Entrar", on_click = entrar_chat)],
        )      
    
    #Botão
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click = iniciar_chat )
    
    pagina.add(texto)
    pagina.add(texto_novo)
    pagina.add(botao_iniciar)

ft.app(main, view=ft.WEB_BROWSER)
