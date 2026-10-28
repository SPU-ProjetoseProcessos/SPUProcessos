# SPUProcessos

Catálogo dos processos de trabalho mapeados da Secretaria do Patrimônio da União.

Site estático, sem dependências de servidor. Três páginas e um arquivo de dados.

## O que tem aqui

- **`index.html`** — o catálogo: busca por nome, código ou descrição e filtros por tipo,
  macroprocesso, dono do processo, unidade e status do mapeamento. Traz também a página
  "Como ler um fluxo", em `index.html#ajuda`.
- **`processo.html?id=N`** — a ficha de um processo: identificação, situação, fluxo
  publicado, normas relacionadas e documentos correlatos. É página de verdade, com
  endereço próprio: dá para guardar, mandar por mensagem e abrir em nova aba.
- **`painel.html`** — o painel do mapeamento: quanto já tem fluxo publicado, quanto está
  em elaboração, quanto falta, por diretoria, por dono do processo e por macroprocesso.
- **`processos.json`** — os dados. As três páginas leem daqui.

## Como atualizar

Troque o `processos.json`. Nenhuma página carrega dados embutidos, então atualizar o
catálogo é trocar um arquivo só.

O `id` de cada processo vem da base de cadastro e **não muda**: é por ele que a ficha é
endereçada. Nunca renumere.

Por enquanto o JSON é mantido à mão. Quando o cadastro no Supabase cobrir todos os campos,
um workflow do GitHub Actions passa a gerá-lo a partir da base.

---

CGGES — Escritório de Processos / Secretaria do Patrimônio da União
