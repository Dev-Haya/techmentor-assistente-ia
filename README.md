# TechMentor 🚀 - Agente de Mentoria em TI

Este projeto implementa o **TechMentor**, um Agente de Inteligência Artificial focado em orientar profissionais em transição de carreira para a área de Tecnologia.

Diferente de chatbots tradicionais, este projeto adota a arquitetura de **Agentes Baseados em Harness**, definindo personas, conhecimentos e skills (habilidades) estruturadas via Markdown, que podem ser interpretadas por ferramentas como Claude Code, Cursor ou Google Antigravity.

## 📁 Estrutura da Arquitetura Avançada
- `AGENTS.md`: O cérebro do projeto. Arquivo principal que instrui o LLM sobre seu papel.
- `agent/persona.md`: Definição de tom de voz, comportamento e travas de segurança.
- `agent/knowledge/`: Base de dados (RAG local) contendo os currículos das trilhas de tecnologia.
- `skills/`: Fluxos de execução passo a passo (ex: como entrevistar o aluno antes de sugerir uma trilha).
- `docs/`: Documentação de métricas e pitch para avaliação estrutural.

##  Como testar este agente
Para interagir com o TechMentor, você precisa de um "Harness" (um terminal de IA).
1. Clone este repositório.
2. Abra a pasta do projeto em uma IDE com IA (como o [Cursor](https://cursor.com/)) ou utilize o terminal via Claude Code / Google Antigravity.
3. Ao abrir, a IA lerá automaticamente o `AGENTS.md`. Basta digitar: *"Quero montar um plano de estudos"* para ver o agente acionar suas skills.
