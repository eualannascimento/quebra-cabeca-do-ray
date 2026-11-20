# 🧩 Quebra Cabeça do Ray — Plataforma Offline em HTML5 Canvas

> ⚠️ **AVISO LEGAL / USO ACADÊMICO E EXPERIMENTAL**  
> Este projeto foi desenvolvido **exclusivamente para fins acadêmicos, educacionais e de estudo experimental**, **sem fins lucrativos** e **sem qualquer finalidade comercial**.  
> Trata-se de uma implementação independente em HTML5 Canvas, JavaScript puro e CSS, criada para estudo de arquitetura frontend offline, otimização de renderização 2D (HiDPI, frustum culling, cache de tabuleiro) e acessibilidade para computadores modestos. Não possui qualquer vínculo, afiliação ou endosso de plataformas comerciais terceiras.

---

## 🎯 Objetivo do Projeto

Oferecer uma plataforma simples, responsiva e **100% offline** de montagem de quebra-cabeças (puzzles), pensada para funcionar diretamente pelo navegador (via arquivo local `quebra-cabeca.html`) mesmo em ambientes sem acesso estável à internet e em computadores Windows 10 modestos.

---

## ✨ Funcionalidades Principais

- **🎨 Design Clean Estilo Things 3 + 3 Temas:** Visual minimalista inspirado no Things 3 com alternância instantânea entre **☀️ Claro**, **🌙 Escuro** e **⬛ Black (OLED)**, aproveitando 100% da largura da tela e rolando apenas o bloco de quebra-cabeças.
- **🔍 Galeria Offline com 1.260 Imagens & Legendas em Português:** Fotografias organizadas em categorias com contagem ao vivo e separação automática entre **✨ Novos para Montar** (padrão) e **📌 Já Criados** (*Natureza*, *Lugares & Cidades*, *Carros & Marcas*, *Café, Vinho & Churrasco*, *Animais*, *Flores*, *Arte & Pinturas*, *Construção, Redes & Casas*, *Aeroportos & Aviação*, *Esportes*, *Planetas & Espaço*, *Onde Está / Música* e *Fotografia*), com busca tolerante a acentos e variações.
- **📁 Suas Próprias Fotos:** Carregue ou arraste qualquer imagem do computador direto para a janela.
- **⏳ Múltiplos Jogos em Andamento:** Inicie vários quebra-cabeças e alterne livremente entre eles, acompanhando o progresso em peças (`X de Y`) e porcentagem (`%`).
- **📊 Contas Locais Editáveis & Analytics:** Crie e edite contas da família (nome e avatar), acompanhe métricas simples (*puzzles concluídos*, *peças encaixadas*, *tempo total*, *maior puzzle* e *ritmo médio*) e exporte/restaure cópias em `.JSON`.
- **🧩 Jogabilidade Fluida e Otimizada:**
  - Suporte de **12 até 1000 peças**, nos modos **Clássico** e **Desafio** (com rotação via `Q` / `E`).
  - Peças com encaixe clássico (pescoço fino + cabeça redonda), formato levemente diferente em cada peça, relevo suave e emendas invisíveis no tabuleiro; texturas em alta resolução com nitidez leve.
  - **Bolso de Peças (Botão Direito):** Recolha várias peças no cursor e solte onde desejar.
  - **💡 Dica Visual:** Pisca suavemente uma peça solta e seu local exato no tabuleiro.
  - **Animações:** Pulsos de encaixe, onda luminosa ao concluir e confetes comemorativos.
  - **Controles Acessíveis:** zoom `➕` / `➖`, pinça no trackpad e no toque, rolagem suave sem "disparar", menu de ferramentas recolhido (só `← Voltar` e `☰ Ferramentas` ficam visíveis), Tela Cheia (`⛶`) e reset (`🧹 Zerar Aplicação`).
  - **Atalhos:** setas / `W A S D` movem a mesa, `+` / `-` zoom, `H` dica, `O` organizar, `K` misturar, `Esc` fecha janelas. Arrastar uma peça até a beirada da tela rola a mesa sozinha.
  - **Blocos montados fora do tabuleiro:** peças vizinhas se encaixam entre si antes de ir ao lugar; "Organizar" e "Misturar" respeitam os blocos já formados.
- **💾 Retomar de Onde Parou:** salvamento automático (a cada jogada, a cada 20 s e ao fechar/esconder a janela) em IndexedDB + localStorage. Ao reabrir o HTML aparece **"Bem-vindo de volta"** com botão **Continuar**. O jogo se adapta se a janela mudar de tamanho; cor da mesa e som também são lembrados. Atalho: `quebra-cabeca.html?continuar=1` abre direto o último jogo.
- **⏱️ Cronômetro Justo:** pausa sozinho quando a aba está escondida ou após 1 minuto sem interação.

---

## 🚀 Como Executar Localmente

1. Baixe ou clone este repositório.
2. **No Windows:** Dê duplo clique em `Jogar-Quebra-Cabeca.bat` para abrir em modo de janela dedicada (ou abra `quebra-cabeca.html` diretamente no navegador).
3. **No macOS / Linux:** Abra `quebra-cabeca.html` diretamente no seu navegador padrão.

---

## 📸 Créditos das Imagens & Licença

- **Código-fonte:** Distribuído sob a licença **MIT** (veja [`LICENSE`](LICENSE)), exclusivamente para fins acadêmicos, experimentais e não comerciais.
- **Acervo Fotográfico (`imagens/`):** Composto por fotografias de domínio público e licenças abertas obtidas via **Wikimedia Commons** (*Quality Images* / *Featured Pictures*) e **Unsplash / Picsum**, utilizadas estritamente para demonstração educacional e não comercial neste projeto experimental.
