//Este arquivo roda no navegador (cliente)
//Ele nao fala com o neon, chama as rotas /api do nosso server.js

const lista = document.getElementById('lista=categorias')
const formulario = document.getElementById('form-categoria')
const campoDescricao = document.getElementById('descricao')
const mensagem = document.getElementById('mensagem')

async function carregarCategorias() {
    

    try {
        const resposta = await fetch('/apt/categorias')
        const categoriaResposta  = await fetch('/apt/categorias')

    
}

function montarLista(dados) 
(
    lista.immerHTML = '<li>Carregando....</li>'
    if(dados.lenght === 0)
(
    listalenHTML