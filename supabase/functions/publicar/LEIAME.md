# publicar

Função do Supabase que pede ao GitHub para gerar o catálogo agora, em vez de
esperar a vaga da agenda.

**Por que ela existe:** a página não pode guardar o token do GitHub — quem abrisse
o código-fonte o teria. Aqui o token fica nos segredos do projeto, no servidor, e
a página só diz "por favor, gere agora".

**Quem pode chamar:** só quem está com sessão aberta na área da equipe. O Supabase
confere a assinatura do token, mas a chave publicável também é um token válido e
está na página — por isso a função olha o papel e exige `authenticated`.

**Segredo necessário:** `TOKEN_GITHUB`, um token fine-grained do GitHub com
permissão **Actions: Read and write** no repositório `SPUProcessos`. Sem ele a
função responde dizendo exatamente isso, e a agenda continua funcionando.

O código implantado está no painel do Supabase, em Edge Functions. Esta pasta
existe para o código não viver só lá.
