# ✈️ Flight Price Tracker

Monitorização automática de preços de voos com alertas inteligentes sempre que surgem tarifas mais baixas para destinos definidos. O sistema analisa múltiplas datas de partida dentro de um intervalo configurado e identifica a melhor oportunidade disponível.

## 📌 Visão Geral

O projeto permite acompanhar preços de voos de forma contínua, evitando verificações manuais e garantindo que o utilizador é notificado quando aparece uma oferta mais vantajosa. A lógica baseia‑se em três pilares: recolha de destinos, pesquisa de voos e envio de alertas.

## 🗂️ Gestão de Destinos

Os destinos monitorizados são obtidos a partir de uma folha remota. Cada entrada inclui:
- cidade  
- código IATA  
- preço mínimo registado  

Sempre que é encontrada uma tarifa inferior, o valor é atualizado automaticamente.

## 🔍 Pesquisa de Voos

O sistema consulta um serviço externo para obter voos disponíveis entre duas datas. Para cada destino, são analisadas várias datas de partida dentro do intervalo definido, permitindo identificar a opção mais económica.

## 🧠 Seleção do Melhor Voo

Entre todas as opções encontradas, o sistema determina:
- o preço mais baixo  
- o aeroporto de origem  
- o aeroporto de destino  
- a data de partida  

Esta informação é consolidada num objeto que representa o voo mais barato encontrado no período analisado.

## 📢 Notificações

Quando é detetada uma tarifa inferior ao valor registado, o utilizador recebe uma notificação automática com:
- destino  
- novo preço  
- rota  
- data de partida  

As notificações são enviadas através de um canal previamente configurado.

## 🔄 Fluxo de Funcionamento

1. Obter lista de destinos e preços atuais.  
2. Pesquisar voos ao longo do intervalo definido.  
3. Identificar o voo mais barato encontrado.  
4. Comparar com o preço registado.  
5. Atualizar o valor caso seja inferior.  
6. Enviar alerta ao utilizador.

## 🎯 Benefícios

- Monitorização contínua e automática.  
- Alertas imediatos quando surgem oportunidades reais.  
- Comparação eficiente entre múltiplas datas.  
- Redução significativa do tempo gasto a procurar voos. 
