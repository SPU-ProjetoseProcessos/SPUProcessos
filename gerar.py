"""Gera o processos.json do site a partir da base, pela porta de fora.

Lê a visão pública com a CHAVE PUBLICÁVEL — a mesma que o navegador usa. Assim o
arquivo gerado nunca pode conter o que o anônimo não poderia ler: não é promessa
do script, é a política de acesso da base que garante. A chave de serviço não
aparece aqui e não deve aparecer nunca.

    python3 gerar.py <pasta-de-destino>

Roda no GitHub Actions por agenda e a pedido. Sem argumentos, escreve ao lado.
"""
import json
import os
import sys
import urllib.parse
import urllib.request

BASE = os.environ.get("SUPABASE_URL", "https://yamixtmtgeockzxmmnsb.supabase.co")
CHAVE = os.environ.get("SUPABASE_KEY", "sb_publishable_8WzmTmKmNaAcxq1MnBqEcg_hgI3ldDm")

OBRIGATORIOS = ("id", "nome", "codigo", "macroNome", "macroTipo", "mapeado", "unidade")


def buscar(caminho, params):
    """Pega todas as páginas de uma tabela ou visão da API REST."""
    saida, de = [], 0
    while True:
        q = dict(params)
        q["offset"] = de
        q["limit"] = 1000
        url = BASE + "/rest/v1/" + caminho + "?" + urllib.parse.urlencode(q)
        req = urllib.request.Request(url, headers={
            "apikey": CHAVE,
            "Authorization": "Bearer " + CHAVE,
            "Accept": "application/json",
        })
        with urllib.request.urlopen(req, timeout=60) as r:
            lote = json.loads(r.read().decode("utf-8"))
        saida.extend(lote)
        if len(lote) < 1000:
            return saida
        de += len(lote)


def dia(iso):
    """A base guarda aaaa-mm-dd; a tela mostra dd/mm/aaaa."""
    if not iso:
        return None
    ano, mes, d = iso.split("-")
    return d + "/" + mes + "/" + ano


def montar():
    linhas = buscar("processos_publicos", {"select": "*", "order": "nome"})
    normas = buscar("processo_normas", {"select": "processo_id,titulo,url,ordem", "order": "ordem"})
    artefatos = buscar("processo_artefatos", {"select": "processo_id,titulo,url,ordem", "order": "ordem"})

    def itens(fonte, pid):
        return [{"t": x["titulo"], "u": x["url"]} for x in fonte if x["processo_id"] == pid]

    catalogo = []
    for r in linhas:
        catalogo.append({
            "id": r["id"],
            "codigo": r["codigo_antigo"],
            "nome": r["nome"],
            "descricao": r["descricao"],
            "macroNome": r["macroprocesso"],
            "macroTipo": r["tipo"],
            "mapeado": r["status_mapeamento"],
            # A Secretaria / Gabinete não tem sigla, por decisão de Juarez: nela o
            # nome é o rótulo. O catálogo mostrava "GABINETE", que não era sigla
            # de nada.
            "unidade": r["unidade_sigla"] or r["unidade"],
            # Dono vazio quer dizer "ligado diretamente à unidade", e as páginas
            # sabem ler isso. Não inventar sigla aqui.
            "dono": r["dono_sigla"],
            "categoria": r["categoria"],
            "vigencia": "Vigente" if r["vigente"] else "Não Vigente",
            "priorizacao": "Priorizado" if r["priorizado"] else "Não priorizado",
            "validado": "Sim" if r["validado"] else "Não",
            "versao": r["versao"],
            "publicacaoV1": dia(r["data_publicacao_fluxo"]),
            "atualizacao": dia(r["data_atualizacao_fluxo"]),
            "linkWeb": r["link_fluxo"],
            "pdf": r["pdf_fluxo"],
            "normas": itens(normas, r["id"]),
            "artefatos": itens(artefatos, r["id"]),
        })
    return catalogo


def conferir(catalogo):
    erros, vistos = [], set()
    for r in catalogo:
        for campo in OBRIGATORIOS:
            if r.get(campo) in (None, ""):
                erros.append(str(r.get("id")) + " sem " + campo)
        if r["id"] in vistos:
            erros.append("id repetido: " + str(r["id"]))
        vistos.add(r["id"])
    if not catalogo:
        erros.append("a base devolveu zero processos")
    return erros


if __name__ == "__main__":
    pasta = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    catalogo = montar()
    erros = conferir(catalogo)
    if erros:
        raise SystemExit("não gerei. " + str(len(erros)) + " problema(s):\n  " + "\n  ".join(erros[:20]))
    destino = os.path.join(pasta, "processos.json")
    with open(destino, "w", encoding="utf-8") as f:
        json.dump(catalogo, f, ensure_ascii=False, indent=1)
    print(str(len(catalogo)) + " processos gerados da base")
