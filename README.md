# SPUProcessos

Catálogo dos processos de trabalho mapeados da Secretaria do Patrimônio da União.

Site estático, sem dependências de servidor: todo o catálogo está no `index.html`.
Abre também por duplo clique, sem internet, salvo pelas fontes.

## O que tem aqui

- Os processos da base, com busca por nome, código ou descrição e filtros por tipo,
  macroprocesso, dono, unidade e status do mapeamento.
- A ficha de cada processo, com identificação, situação e histórico de datas.
- Link direto para o fluxo publicado de cada processo mapeado.
- Uma página explicando como ler um fluxo em BPMN, para quem consulta.

## Como atualizar

O conteúdo vem do export da lista de processos. Hoje os dados estão embutidos no
`index.html`. Quando o cadastro existir, a ideia é separá-los num `processos.json`
ao lado, para atualizar o catálogo trocando só o JSON.

---

CGGES — Escritório de Processos / Secretaria do Patrimônio da União
