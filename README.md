# Real Park Residence · Apto 1101 — anúncio com tour 3D

Site publicado: **https://leandrofurtado.github.io/realpark-1101**
(GitHub Pages, branch `main`, pasta raiz. Cada `git push` atualiza o site em 1–2 min.)

## O que há no site
- `index.html`: anúncio de aluguel com capa (vista da varanda), valor, destaques, botão "Fazer o tour 3D", galeria por cômodo, planta, texto, endereço e WhatsApp com mensagem pronta.
- `3d.html`: tour 3D mobiliado. Inclui o modo de fotos reais (arrastar para olhar em volta, setas nas portas para trocar de cômodo, "◀ Cômodo anterior" / "◀ Sair das fotos"), o botão "◀ Voltar ao anúncio" e o botão "Ocultar/Mostrar painéis". **É gerado**: não edite à mão, edite `_fonte/3d-fonte.js` e rode `_fonte/build.sh`.
- `fotos/`: fotos do anúncio (`*-p.jpg` = miniaturas). `planta.jpg`, `modelo-3d.jpg`, `og.jpg` (prévia do link no WhatsApp).

## Como alterar
- Textos e fotos do anúncio: editar `index.html` (lista de fotos no array `G` do script, no fim do arquivo).
- Tour 3D (móveis, nomes, botões): editar `_fonte/3d-fonte.js` → `bash _fonte/build.sh` → confere → commit e push.
- Planta (`planta.jpg`): a cena está em `_fonte/planta-render.html` (nomes no mapa `NOMES`). Para re-renderizar, servir a raiz do repo com `python3 -m http.server 8765`, rodar `python3 _fonte/render_planta.py _fonte/planta.json` (Playwright + Chromium) e converter `planta.png` em `planta.jpg`. Os móveis da planta ficam no trecho "MÓVEIS CONFORME AS FOTOS" desse arquivo e precisam ser mudados igualmente no `3d-fonte.js`.

## Decisões do proprietário (manter)
- Metragem: destaque "≈105 m² de área privativa" (medido pela planta com paredes) + "86,98 m² úteis" (soma das áreas internas da planta). Trocar pelo número da escritura/IPTU se ele informar.
- Cômodos: **suíte + quarto + closet** (nunca "3 quartos"). Nomes no site e no 3D: Suíte, Quarto, Closet.
- A **cama da suíte** e a **mesa de jantar** não ficam no apartamento.
- Valor: R$ 5.500/mês com condomínio. **Não aparece na prévia do link** (título/descrição do WhatsApp); aparece dentro da página.
- Contato: WhatsApp (63) 98401-5283.
- Privacidade: sem fotos com pessoas, quadro do casal desfocado, sem o nome da filha, página fora do Google (`noindex`).
- Link: fica `leandrofurtado.github.io/realpark-1101` (ele não quis encurtar). Para forçar a prévia nova no WhatsApp, usar `/?v=3`, `/?v=4`…

## Situação
- Projeto concluído e aprovado pelo proprietário (03/11/2026). Sem pendências.
