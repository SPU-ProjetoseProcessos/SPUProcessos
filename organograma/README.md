# Organograma da SPU — versão pública

Quem está onde na Secretaria do Patrimônio da União: a estrutura do SIORG, a chefia de cada
unidade, quem está lotado e a competência regimental. Site estático, sem servidor.

## Fontes

- **Estrutura, competências e cargos:** SIORG.
- **Pessoas:** **Portal da Transparência — dados abertos**, extração mensal
  `Servidores_SIAPE`, com o mês de referência estampado no cabeçalho e no rodapé.

Tudo o que aparece nesta versão já é publicado pelo Portal da Transparência.

## O que traz, por pessoa

Nome, cargo e função comissionada, quando houver. Nada além disso.

Não traz situação funcional, escolaridade, abono de permanência, programa de gestão nem órgão de
origem. Não traz CPF nem matrícula — que, aliás, o próprio Portal já publica mascarados.

**Não tem painel**, logo não há microdado de perfil nem filtro por atributo de pessoa.

O corte é feito no gerador, não na tela: o arquivo desta pasta **não contém** os campos
retirados. Confira em `dados-organograma.js`, no bloco `META_ORG.camposDaPessoa`.

Estagiários não aparecem porque o dado aberto só traz servidores.

## Arquivos

- `index.html` — organograma gráfico, lista e busca.
- `dados-organograma.js` — os dados.

## Como atualizar

Na pasta do projeto, rode `gerar_competencias_gerais.py` e depois
`gerar_dados_organograma.py`. Os dois arquivos desta pasta são regerados.

---

CGGES — Escritório de Processos / Secretaria do Patrimônio da União
