# ✈️ Flight Price Tracker

Sistema automatizado que monitoriza preços de voos e identifica oportunidades reais de viagem. Analisa múltiplas datas de partida, encontra a tarifa mais baixa disponível e envia alertas personalizados aos utilizadores.

## 📌 Visão Geral

O projeto acompanha preços de voos de forma contínua, cruzando dados de uma folha remota com pesquisas diárias. Sempre que surge uma tarifa inferior ao valor registado, o sistema atualiza o preço e notifica todos os clientes subscritos.

## 🗂️ Gestão de Destinos

Os destinos são obtidos a partir de uma folha remota que contém:
- cidade  
- código IATA  
- preço mínimo registado  

Quando é encontrada uma tarifa mais baixa, o valor é atualizado automaticamente.

## 🔍 Pesquisa de Voos

O sistema consulta um serviço externo para obter voos só de ida. Para cada destino, analisa um intervalo de datas e recolhe:
- preço  
- número de escalas  
- rota completa (aeroportos de partida, escala e chegada)  
- data do voo  

Todos os voos diretos e com escalas são considerados, sendo selecionada sempre a opção mais económica.

## 🧠 Seleção do Melhor Voo

Entre todas as datas analisadas, o sistema determina:
- a tarifa mais baixa  
- a rota completa  
- o número de escalas  
- a data de partida  

Esta informação é encapsulada num objeto que representa o melhor voo encontrado.

## 📢 Notificações

Quando é detetada uma tarifa inferior ao valor registado:
- o preço é atualizado na folha remota  
- todos os clientes recebem um alerta por email  
- o utilizador principal recebe também uma notificação via Telegram  

As mensagens incluem:
- preço  
- rota  
- data  
- indicação se o voo é direto ou com escalas  

## 🔄 Fluxo de Funcionamento

1. Obter destinos e preços atuais.  
2. Pesquisar voos ao longo do intervalo definido.  
3. Identificar o voo mais barato.  
4. Comparar com o preço registado.  
5. Atualizar o valor caso seja inferior.  
6. Enviar alertas por email e Telegram.

## 🎯 Benefícios

- Monitorização contínua e automática.  
- Alertas imediatos quando surgem oportunidades reais.  
- Rota completa incluída em cada alerta.  
- Notificações enviadas a todos os clientes subscritos.  
- Redução significativa do tempo gasto a procurar voos.