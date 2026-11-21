# 🧩 Quebra Cabeça do Ray: Plataforma Offline em HTML5 Canvas

> ⚠️ **AVISO LEGAL / USO ACADÊMICO E EXPERIMENTAL**  
> Este projeto foi desenvolvido **exclusivamente para fins acadêmicos, educacionais e de estudo experimental**, **sem fins lucrativos** e **sem qualquer finalidade comercial**.  
> Trata-se de uma implementação independente em HTML5 Canvas, JavaScript puro e CSS, criada para estudo de arquitetura frontend offline, otimização de renderização 2D (HiDPI, frustum culling, cache de tabuleiro) e acessibilidade para computadores modestos. Não possui qualquer vínculo, afiliação ou endosso de plataformas comerciais terceiras.

---

## 🎯 Objetivo do Projeto

Oferecer uma plataforma simples, responsiva e **100% offline** de montagem de quebra-cabeças (puzzles), pensada para funcionar diretamente pelo navegador (via arquivo local `quebra-cabeca.html`) mesmo em ambientes sem acesso estável à internet e em computadores Windows 10 modestos.

---

## ✨ Funcionalidades Principais

- **🎨 Design Clean Estilo Things 3 + 3 Temas + Multiplataforma:** Visual minimalista com alternância de tema em 1 ícone (**☀️ Claro**, **🌙 Escuro**, **⬛ Black OLED**), botão de Tela Cheia na extremidade direita, avatar ampliado com foto de pessoa na extremidade esquerda e layout responsivo adaptado para computador, **iPad Pro**, **iPhone 15** e **Galaxy Note 10 / 20** (`100dvh`, áreas seguras `safe-area-inset` e suporte a toque/pinça).
- **🔍 Descobrir com Menu Lateral Dobrável em 2 Níveis & 4.261 Imagens:** Começa em **🧩 Todos** e traz grupos dobráveis para **⭐ Seus Gostos** (*Jeep Renegade, Ford Bronco, BYD, Jeep, Mercedes-Benz, BMW, Vila Camilópolis / Nagumo / Santo André-SP, Pesqueira-PE, Minas Gerais / Serra da Canastra, Queijos, Foz do Iguaçu, Paraguai, Argentina, Cachorros, Natal, Presidentes do Brasil e EUA, Café & Expresso, Vinhos, Churrasco, Mercados & Farmácias, Construção DIY, Cabeamento & Redes, Prédios, Aeroportos, Onde Está / Cenas, Música*) e **🗂️ Categorias Gerais**, com contagem em tempo real e marcador visual nos quebra-cabeças já criados.
- **⏳ Em Andamento & 🏆 Concluídos com Prévia em Tela Cheia:** Abas separadas com contadores, exibição detalhada de **Tempo Atuando**, **Tempo Parado**, **Tempo Total / Até o momento**, **Cliques** e **Ritmo (peças/min)**, além de visualização em **tela cheia** tanto da foto completa quanto de **como o tabuleiro está montado no momento**.
- **📊 Perfil com Foto Real & Analytics Geral:** Acesso direto pelo avatar no canto esquerdo, edição protegida pelo botão **✏️ Editar** (aceitando upload de imagem/foto de pessoa), analytics detalhado (concluídos, em andamento, peças, tempo atuando, tempo parado, tempo total, cliques, ritmo médio, melhor ritmo, média de peças, cliques por peça, média por vitória, taxa de foco ativo e distribuição por temas) e opções discretas de cópia/restauração `.json`.
- **⚡ Motor & Mesa Otimizados (Windows 10 i5 3ª Geração + Toque):**
  - Renderização com **Dirty-Rect** no arraste, **loop `requestAnimationFrame` sob demanda**, escala `dpr = 1`, atlas pré-renderizado e gravação assíncrona em IndexedDB.
  - **Avatar ampliado + `← Voltar`** no canto superior esquerdo, **menu `☰ Ferramentas` autoexplicativo** no canto superior direito (fixo ao abrir por padrão, com alternância para modo Dropdown que fecha ao clicar fora), e **Timer + Percentual em destaque logo acima das cores de fundo** no canto inferior direito.
  - **Pausa automática aos 30 segundos** sem mover o mouse/interagir (contabilizando o tempo parado separado do tempo atuando).
  - Suporte de **12 até 1000 peças**, escolha em tela cheia, **Bolso de Peças (Botão Direito)**, **💡 Dica Visual**, pinça no trackpad/toque e atalhos (`W A S D` / setas, `+` / `-`, `H`, `O`, `K`, `X`, `F`, `R`).
- **☁️ Pronto para Web / Vercel:** Inclui `vercel.json` com rewrite de `/` para `/quebra-cabeca.html` e cache longo em `/imagens/*` (observando que as 4.261 imagens locais somam ~545 MB, acima da cota gratuita Hobby de deploy estático direto na Vercel sem hospedagem externa das imagens).
- **💾 Retomar de Onde Parou:** salvamento automático (a cada jogada, a cada 20 s e ao fechar/esconder a janela) em IndexedDB + localStorage. Ao reabrir o HTML aparece **"Bem-vindo de volta"** com botão **Continuar**. Atalho: `quebra-cabeca.html?continuar=1` abre direto o último jogo.
- **⏱️ Cronômetro Justo:** pausa sozinho quando a aba está escondida ou após **30 segundos** sem mexer o mouse/interagir.

---

## 🚀 Como Executar Localmente

1. Baixe ou clone este repositório.
2. **No Windows:** Dê duplo clique em `Jogar-Quebra-Cabeca.bat` para abrir em modo de janela dedicada (ou abra `quebra-cabeca.html` diretamente no navegador).
3. **No macOS / Linux:** Abra `quebra-cabeca.html` diretamente no seu navegador padrão.

---

## 📸 Créditos das Imagens & Licença

- **Código-fonte:** Distribuído sob a licença **MIT** (veja [`LICENSE`](LICENSE)), exclusivamente para fins acadêmicos, experimentais e não comerciais.
- **Acervo Fotográfico (`imagens/`):** Composto por fotografias de domínio público e licenças abertas obtidas via **Wikimedia Commons** (*Quality Images* / *Featured Pictures*) e **Unsplash / Picsum**, utilizadas estritamente para demonstração educacional e não comercial neste projeto experimental.
