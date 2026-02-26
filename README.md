# 📡 Django Blog API - Automação, Testes e Serialização REST

Este projeto evolui o motor de blog para uma arquitetura de API robusta. Utilizando o **Django REST Framework**, implementei a camada de serialização que expõe os dados automatizados por signals para o consumo de aplicações externas, mantendo a integridade através de testes rigorosos.

---

# 📝 Resumo (Resume)
Neste projeto, fechei o ciclo de desenvolvimento de uma API profissional. O sistema utiliza **Signals** para automação de Slugs, garantindo URLs amigáveis sem esforço manual. Implementei o **ProdutoSerializer**, que mapeia o modelo `Post` para JSON, permitindo que campos como `status` e `data_criacao` sejam entregues de forma padronizada. A segurança e a funcionalidade do sistema são validadas por uma suíte de **Testes Unitários**, assegurando que a lógica de negócio permaneça intacta mesmo com a adição da camada REST.



## 🚀 Tecnologias e Ferramentas (Tech Stack)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-A30000?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)

## 📋 Funcionalidades em Destaque
* **Serialização Model-Driven:** Uso de `ModelSerializer` para transformar instâncias do banco de dados em JSON, respeitando as escolhas de `status` e formatos de data.
* **Signals de Ciclo de Vida:** Automação total na geração de slugs via `pre_save`, garantindo que a API sempre entregue URLs válidas para cada postagem.
* **Testes de Regressão:** Suíte de testes automatizados que verifica se a criação via API ou via Admin mantém a integridade dos campos obrigatórios.
* **Campos Prepopulados e Editáveis:** Customização avançada do Admin para facilitar a gestão de conteúdo com edição rápida em lista (`list_editable`).
* **Tipagem e Escolhas (Choices):** Implementação de enums para o campo `status`, garantindo que a API aceite apenas valores válidos (Rascunho/Publicado).
* **Documentação de Dados:** Estruturação de campos de auditoria (`data_criacao` e `data_publicacao`) para transparência no consumo da API.



---

# 👨‍💻 Sobre mim (About Me)
Olá, meu nome é **Kaio**, tenho 22 anos. Como meu foco é o **Back-End com Python**, entendo que o Serializer é o contrato entre mim e o desenvolvedor Front-End. No Front, eu consumia APIs; agora, eu as construo com camadas de proteção (Testes), automação (Signals) e padronização (DRF). Essa visão 360º me permite projetar APIs que não apenas funcionam, mas são seguras, performáticas e fáceis de integrar com qualquer interface moderna.

### Entre em contato (Contact me)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=092E20)](https://linkedin.com/in/kaio-grativol-baldo-071a74150/)
[![Instagram](https://img.shields.io/badge/Instagram-000?style=for-the-badge&logo=instagram&logoColor=092E20)](https://www.instagram.com/kaiull__/)
[![GitHub](https://img.shields.io/badge/Github-000?style=for-the-badge&logo=github&logoColor=092E20)](https://github.com/SeuUsuarioAqui)

---
*Projeto desenvolvido para consolidar a integração entre modelos automatizados e serialização REST no ecossistema Django.*
